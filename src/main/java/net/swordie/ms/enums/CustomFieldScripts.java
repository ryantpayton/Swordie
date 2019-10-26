package net.swordie.ms.enums;

import net.swordie.ms.constants.BossConstants;

import java.util.Arrays;

/**
 * Created on 1-12-2018.
 *
 * @author Asura
 */
public enum CustomFieldScripts { // Custom Field Scripts
    easy_zakum_enter(BossConstants.ZAKUM_EASY_ALTAR),
    hard_zakum_enter(BossConstants.ZAKUM_HARD_ALTAR),
    chaos_zakum_enter(BossConstants.ZAKUM_CHAOS_ALTAR),
    ;
    private int id;

    CustomFieldScripts(int val) {
        this.id = val;
    }

    public int getVal() {
        return id;
    }

    public static CustomFieldScripts getByVal(int id) {
        return Arrays.stream(values()).filter(cfs -> cfs.getVal() == id).findAny().orElse(null);
    }
}
