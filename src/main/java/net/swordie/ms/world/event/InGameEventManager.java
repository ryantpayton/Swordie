package net.swordie.ms.world.event;

import net.swordie.ms.Server;
import net.swordie.ms.ServerConfig;
import net.swordie.ms.client.character.BroadcastMsg;
import net.swordie.ms.client.character.Char;
import net.swordie.ms.connection.packet.WvsContext;
import net.swordie.ms.enums.ChatType;
import net.swordie.ms.handlers.EventManager;
import net.swordie.ms.life.Life;
import net.swordie.ms.util.Randomizer;
import net.swordie.ms.world.Channel;
import net.swordie.ms.world.field.Field;

import java.util.*;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

public class InGameEventManager {

    private static InGameEventManager instance = new InGameEventManager();
    public static final int REGISTRATION_DURATION_MINS = ServerConfig.DEBUG_MODE ? 1 : 5; // devs want fast

    private List<InGameEvent> events = new ArrayList<>();
    private ScheduledFuture schedule;
    private ScheduledFuture reminderTimer;
    private InGameEventType previousEvent;
    private int remindersSent = 0;

    public static InGameEventManager getInstance() {
        return instance;
    }

    public InGameEventManager() {
        events.add(new RussianRouletteEvent());
        events.add(new PinkZakumEvent());
        // more to come...

        if (!ServerConfig.DEBUG_MODE)
            schedule = EventManager.addFixedRateEvent(this::doEvent, 5, 40, TimeUnit.MINUTES);
    }

    public void forceNextEvent() { // for testing only, this should not be used in prod
        if (ServerConfig.DEBUG_MODE) {
            doEvent();
        } // else notify character that server is in prod
    }

    private void doEvent() {
        clearForNextEvent(previousEvent);

        InGameEvent event = events.stream()
                .filter(e -> e.getEventType() != previousEvent)
                .findFirst()
                .orElse(events.get(0)); // this check ensure that even if theres only 1 total event it will select one

        previousEvent = event.getEventType();

        if (!ServerConfig.DEBUG_MODE) {
            reminderTimer = EventManager.addFixedRateEvent(this::sendReminder, 30, 60, TimeUnit.SECONDS);
        }

        Server.getInstance().getWorldById(ServerConfig.WORLD_ID)
                .broadcastPacket(WvsContext.broadcastMsg(BroadcastMsg.notice(event.getEventName() + " event registration has started! Registration will close in " + REGISTRATION_DURATION_MINS + " minutes.")));
        event.doEvent();
    }


    private void clearForNextEvent(InGameEventType type) {
        InGameEvent ige = getEvent(type);
        if (ige == null) {
            return;
        }

        ige.clear();
    }

    private void sendReminder() {
        Server.getInstance().getWorldById(ServerConfig.WORLD_ID)
                .broadcastPacket(WvsContext.broadcastMsg(BroadcastMsg.notice(getActiveEvent().getEventName() + " event registration is currently open and will begin soon!")));
        remindersSent += 1;
        if (remindersSent >= 4)
            reminderTimer.cancel(true);
    }

    public InGameEvent getOpenEvent() {
        InGameEvent e = null;
        for (InGameEvent ige : events) {
            if (ige.isOpen())
                e = ige;
        }
        return e;
    }

    public InGameEvent getActiveEvent() {
        InGameEvent e = null;
        for (InGameEvent ige : events) {
            if (ige.isActive())
                return ige;
        }
        return e;
    }

    public void joinPublicEvent(Char c) {
        InGameEvent e = getActiveEvent();

        if (e == null) {
            c.chatMessage(ChatType.SystemNotice, "There are no ongoing events. Please check back later!");
        } else if (!e.isOpen()) {
            c.chatMessage(ChatType.SystemNotice, "The event has closed for new entries.");
        } else {
            e.joinEvent(c);
        }
    }

    public InGameEvent getEvent(InGameEventType type) {
        return events.stream()
                .filter(c -> c.getEventType() == type)
                .findFirst().orElseGet(null); // it cannot return null since we put two events in in in the constructor
    }

    public boolean charInEventMap(int charId) {
        InGameEvent e = getActiveEvent();

        if (e == null) {
            return false;
        }

        return e.charInEvent(charId);
    }
}
