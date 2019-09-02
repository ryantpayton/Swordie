package net.swordie.ms.constants;

/**
 * Created on 2-8-2018.
 */
public class BossConstants {

    //  Lotus ----------------------------------------------------------------------------------------------------------
    public final static int LOTUS_MOBID = 8950000;
    public static final long[][] LOTUS_HP_PHASE_DIFFICULTY = {{400000000000L, 1600000000000L}, {400000000000L, 7000000000000L}, {700000000000L, 24000000000000L}};
    public static final int LOTUS_BOUNCING_BALL_DURATION = 20000;
    //      Obstacle Atoms
    public static final int LOTUS_OBSTACLE_ATOM_VELOCITY = 15; // Velocity at which the Obstacle Atoms fall down.

    public static final int LOTUS_BLUE_ATOM_EXECUTION_DELAY = 1500; // in ms. Delay between method executions
    public static final int LOTUS_BLUE_ATOM_AMOUNT = 3; // max amount of Atoms spawning attempts in 1 call
    public static final int LOTUS_BLUE_ATOM_PROP = 30; // % chance of actually spawning in
    public static final int LOTUS_BLUE_ATOM_DAMAGE = 25; // % of Max HP

    public static final int LOTUS_YELLOW_ATOM_EXECUTION_DELAY = 1750; // in ms. Delay between method executions
    public static final int LOTUS_YELLOW_ATOM_AMOUNT = 3; // max amount of Atoms spawning attempts in 1 call
    public static final int LOTUS_YELLOW_ATOM_PROP = 25; // % chance of actually spawning in
    public static final int LOTUS_YELLOW_ATOM_DAMAGE = 50; // % of Max HP

    public static final int LOTUS_PURPLE_ATOM_EXECUTION_DELAY = 2000; // in ms. Delay between method executions
    public static final int LOTUS_PURPLE_ATOM_AMOUNT = 3; // max amount of Atoms spawning attempts in 1 call
    public static final int LOTUS_PURPLE_ATOM_PROP = 20; // % chance of actually spawning in
    public static final int LOTUS_PURPLE_ATOM_DAMAGE = 100; // % of Max HP
    //      Stage 3
    public static final int LOTUS_ROBOT_ATOM_EXECUTION_DELAY = 2000; // in ms. Delay between method executions
    public static final int LOTUS_ROBOT_ATOM_AMOUNT = 2; // max amount of Atoms spawning attempts in 1 call
    public static final int LOTUS_ROBOT_ATOM_PROP = 15; // % chance of actually spawning in
    public static final int LOTUS_ROBOT_ATOM_DAMAGE = 100; // % of Max HP

    public static final int LOTUS_CRUSHER_ATOM_EXECUTION_DELAY = 4000; // in ms. Delay between method executions
    public static final int LOTUS_CRUSHER_ATOM_AMOUNT = 1; // max amount of Atoms spawning attempts in 1 call
    public static final int LOTUS_CRUSHER_ATOM_PROP = 40; // % chance of actually spawning in
    public static final int LOTUS_CRUSHER_ATOM_DAMAGE = 100; // % of Max HP



    //  Magnus ---------------------------------------------------------------------------------------------------------

    //      General
    public static final int MAGNUS_TIME = 20  *60; // 20 minutes
    public static final int MAGNUS_DEATHCOUNT = 20; // 20 death count


    //      Obstacle Atoms
    public static final int MAGNUS_OBSTACLE_ATOM_VELOCITY = 5; // Velocity at which the Obstacle Atoms fall down.

    public static final int MAGNUS_GREEN_ATOM_EXECUTION_DELAY = 1000; // in ms. Delay between method executions
    public static final int MAGNUS_GREEN_ATOM_AMOUNT = 4; // max amount of Atoms spawning attempts in 1 call
    public static final int MAGNUS_GREEN_ATOM_PROP = 35; // % chance of actually spawning in
    public static final int MAGNUS_GREEN_ATOM_DAMAGE = 25; // % of Max HP

    public static final int MAGNUS_BLUE_ATOM_EXECUTION_DELAY = 750; // in ms. Delay between method executions
    public static final int MAGNUS_BLUE_ATOM_AMOUNT = 4; // max amount of Atoms spawning attempts in 1 call
    public static final int MAGNUS_BLUE_ATOM_PROP = 30; // % chance of actually spawning in
    public static final int MAGNUS_BLUE_ATOM_DAMAGE = 50; // % of Max HP

    public static final int MAGNUS_PURPLE_ATOM_EXECUTION_DELAY = 2000; // in ms. Delay between method executions
    public static final int MAGNUS_PURPLE_ATOM_AMOUNT = 3; // max amount of Atoms spawning attempts in 1 call
    public static final int MAGNUS_PURPLE_ATOM_PROP = 25; // % chance of actually spawning in
    public static final int MAGNUS_PURPLE_ATOM_DAMAGE = 100; // % of Max HP


    //  Horntail -------------------------------------------------------------------------------------------------------

    //      General
    public static final int EASY_HORNTAIL_TIME = 75 * 60; // 1 hr, 15 min timer
    public static final int CHAOS_HORNTAIL_TIME = 150 * 60; // 2 hrs, 30 min timer

//  Hilla --------------------------------------------------------------------------------------------------------------

    //      General
    public static final int EASY_HILLA_TIME = 30 * 60; // 1 hr, 15 min timer
    public static final int NORMAL_HILLA_TIME = 150 * 60; // 2 hrs, 30 min timer

//  Von Leon -----------------------------------------------------------------------------------------------------------
    public static final int VON_LEON_TIME = 30 * 60; // 30 min timer

//  Cygnus -------------------------------------------------------------------------------------------------------------
    public static final int CYGNUS_TIME = 30 * 60; // 30 min timer

//  Cygnus -------------------------------------------------------------------------------------------------------------
    public static final int ARKARIUM_TIME = 30 * 60; // 30 min timer



//  Demian -------------------------------------------------------------------------------------------------------------
    public static final int BRAND_OF_SACRIFICE = 80001974; // Skill ID
    public static final long DEMIAN_HP = 840000000000L;
    public static final int DEMIAN_NORMAL_TEMPLATE_ID = 8880110;

    // Sword
    public static final int DEMIAN_SWORD_VELOCITY = 30; // default velocity
    public static final int DEMIAN_SWORD_TARGETING_VELOCITY = 60; // default velocity when targeting

    // Stigma
    public static final int DEMIAN_MAX_STIGMA = 7; // max stigma
    public static final int DEMIAN_PASSIVE_STIGMA_TIME = 30 * 1000; // Every 30 seconds, users are hit with +1 stigma
    public static final int DEMIAN_STIGMA_INCINERATE_OBJECT_RESPAWN_TIME = 20 * 1000; // Stigma Pillar spawns every 20seconds
    public static final int DEMIAN_STIGMA_INCINERATE_OBJECT_DURATION_TIME = 10 * 1000; // Stigma Pillar lasts 10 seconds

    //  Gollux ---------------------------------------------------------------------------------------------------------
    public static final int[][] GOLLUX_HP_MULTIPLIERS = {{1, 60, 300, 500}, {1, 10, 150, 3000}, {1, 10, 300, 30000}};
    public static final int GOLLUX_FIRST_MAP = 863010100;
    public static final int GOLLUX_RIGHT_SHOULDER = 863010330;
    public static final int GOLLUX_LEFT_SHOULDER = 863010430;
    public static final int GOLLUX_ABDOMEN = 863010240;
    public static final int[] GOLLUX_RIGHT_HAND_SKILLS = new int[]{3, 5, 6, 8, 10};
    public static final int[] GOLLUX_LEFT_HAND_SKILLS = new int[]{2, 4, 7, 9, 11};
    public static final int GOLLUX_BREATH_ATTACK = 1;
    public static final int GOLLUX_DROP_STONE_CHANCE = 25;


    // TODO More bosses to be noted down...
}
