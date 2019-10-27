package net.swordie.ms.client.character.commands;

public abstract class PlayerCommand implements ICommand {

    public PlayerCommand(){
    }

    public static char getPrefix() {
        return '@';
    }
}
