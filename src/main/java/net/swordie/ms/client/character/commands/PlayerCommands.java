package net.swordie.ms.client.character.commands;

import net.swordie.ms.client.character.Char;
import net.swordie.ms.client.character.items.Equip;
import net.swordie.ms.client.character.items.Inventory;
import net.swordie.ms.client.character.items.Item;
import net.swordie.ms.connection.packet.Effect;
import net.swordie.ms.connection.packet.UserPacket;
import net.swordie.ms.constants.ItemConstants;
import net.swordie.ms.enums.AccountType;
import net.swordie.ms.enums.BaseStat;
import net.swordie.ms.loaders.ItemData;
import net.swordie.ms.loaders.containerclasses.ItemInfo;
import net.swordie.ms.scripts.ScriptManagerImpl;
import net.swordie.ms.scripts.ScriptType;
import net.swordie.ms.util.Util;
import net.swordie.ms.world.event.InGameEventManager;
import org.apache.log4j.LogManager;

import java.util.*;
import java.util.stream.Collectors;

import static net.swordie.ms.enums.ChatType.Mob;
import static net.swordie.ms.enums.ChatType.Notice2;

public class PlayerCommands {
    static final org.apache.log4j.Logger log = LogManager.getRootLogger();

    @Command(names = {"check", "dispose", "fix"}, requiredType = AccountType.Player)
    public static class Dispose extends PlayerCommand {
        public static void execute(Char chr, String[] args) {
            chr.dispose();
            Map<BaseStat, Integer> basicStats = chr.getTotalBasicStats();
            StringBuilder sb = new StringBuilder();
            List<BaseStat> sortedList = Arrays.stream(BaseStat.values()).sorted(Comparator.comparing(Enum::toString)).collect(Collectors.toList());
            for (BaseStat bs : sortedList) {
                sb.append(String.format("%s = %d, ", bs, basicStats.getOrDefault(bs, 0)));
            }
            chr.chatMessage(Mob, String.format("X=%d, Y=%d, Stats: %s", chr.getPosition().getX(), chr.getPosition().getY(), sb));
            ScriptManagerImpl smi = chr.getScriptManager();
            // all but field
            smi.stop(ScriptType.Portal);
            smi.stop(ScriptType.Npc);
            smi.stop(ScriptType.Reactor);
            smi.stop(ScriptType.Quest);
            smi.stop(ScriptType.Item);
        }
    }

    @Command(names = {"event"}, requiredType = AccountType.Player)
    public static class JoinEvent extends PlayerCommand {
        public static void execute(Char chr, String[] args) {
            InGameEventManager.getInstance().joinPublicEvent(chr);
        }
    }

    @Command(names = {"roll"}, requiredType = AccountType.Player)
    public static class OneArmedBandit extends PlayerCommand {
        public static void execute(Char chr, String[] args) {

            String[] str = new String[]{
                    "Map/Effect.img/miro/frame",
                    "Map/Effect.img/miro/RR1/" + Util.getRandom(4),
                    "Map/Effect.img/miro/RR2/" + Util.getRandom(4),
                    "Map/Effect.img/miro/RR3/" + Util.getRandom(4)
            };

            for (String s : str) {
                chr.write(UserPacket.effect(Effect.effectFromWZ(s, false, 0, 4, 0)));
            }
        }
    }

    @Command(names = {"sell"}, requiredType = AccountType.Player)
    public static class SellAllEquipmentInventory extends PlayerCommand {
        public static void execute(Char chr, String[] args) {
            if (chr == null) {
                // might not happen, BUT better safe than sorry
                chr.chatMessage(Notice2, "Something went wrong. Please contact Clueless Cow on discord");
                chr.dispose();
                return;
            }

            Inventory eqInventory = chr.getEquipInventory();
            List<Item> soldItems = new ArrayList<Item>();
            byte numOfSlots = eqInventory.getSlots();
            byte startIndex = 1, endIndex = numOfSlots;
            int totalMesos = 0;
            String startIndexOutOfRangeMessage = String.format("<startIndex> must be between 1 and %d", numOfSlots);
            String endIndexOutOfRangeMessage = String.format("<endIndex> must be between <startIndex> and %d", numOfSlots);

            if (args.length > 1) {
                // process startIndex
                String start = args[1];
                if (start != null && Util.isNumber(start)) {
                    startIndex = Byte.parseByte(start);
                    if (startIndex < 1 || startIndex > numOfSlots) { // startIndex out of range
                        chr.chatMessage(Notice2, startIndexOutOfRangeMessage);
                        chr.dispose();
                        return;
                    }
                }
                // process endIndex
                if (args.length > 2) {
                    String end = args[2];
                    if (end != null && Util.isNumber(end)) {
                        endIndex = Byte.parseByte(end);
                        if (endIndex <= startIndex || endIndex > numOfSlots) { // endIndex out of range
                            chr.chatMessage(Notice2, endIndexOutOfRangeMessage.replace("<startIndex>", String.valueOf(startIndex + 1)));
                            chr.dispose();
                            return;
                        }
                    }
                }
            }

            // start selling process
            for (int i = startIndex; i <= endIndex; i++) {
                // get item by slot index
                Item item = eqInventory.getItemBySlot(i);
                // no item found at slot, skip
                if (item == null) continue;

                // item found
                // calculating item's price
                int itemId = item.getItemId();
                int quantity = item.getQuantity();
                int cost = 0;
                if (ItemConstants.isEquip(itemId)) {
                    cost = ((Equip) item).getPrice();
                } else {
                    ItemInfo itemInfo = ItemData.getItemInfoByID(itemId);
                    if (itemInfo == null) continue;
                    cost = itemInfo.getPrice() * quantity;
                }
                totalMesos += (quantity * cost);
                soldItems.add(item);
            }

            // no items found in range
            if (soldItems.size() == 0) {
                chr.chatMessage("No items found");
                chr.dispose();
                return;
            }
            // mesos cap
            if (!chr.canAddMoney(totalMesos)) {
                chr.chatMessage(String.format("You've reach the mesos cap. Please deposit at least %d mesos and run the command again!", totalMesos));
                chr.dispose();
                return;
            }
            // remove sold items from inventory
            for (Item eq : soldItems) {
                chr.consumeItem(eq);
            }
            chr.addMoney(totalMesos);
            chr.chatMessage(String.format("You've received %d mesos by selling items", totalMesos));
            chr.dispose();
        }
    }
}
