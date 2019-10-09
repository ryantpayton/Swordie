package net.swordie.ms.client.character.items;

import net.swordie.ms.enums.ScrollStat;
import net.swordie.ms.util.container.Tuple;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class SetEffect {
    private HashMap<Integer, List<Object>> effectsByLevel = new HashMap<>();

    public void addScrollStat(int level, ScrollStat ss, int amount) {
        if (effectsByLevel.get(level) == null) {
            effectsByLevel.put(level, new ArrayList<Object>());
        }
        effectsByLevel.get(level).add(new Tuple<>(ss, amount));
    }

    public void addOption(int level, ItemOption io) {
        if (effectsByLevel.get(level) == null) {
            effectsByLevel.put(level, new ArrayList<Object>());
        }
        effectsByLevel.get(level).add(io);
    }

    public HashMap<Integer, List<Object>> getEffectsToLevel() {
        return effectsByLevel;
    }

    public List<Object> getStatsByLevel (int level) {
        return effectsByLevel.get(level);
    }
}
