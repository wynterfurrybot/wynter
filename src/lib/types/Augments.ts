import Command from '../structures/Command';

declare module 'discord.js' {
	export interface Client {
		commands: Collection<string, Command>;
		commandCooldowns: Collection<string, Collection<string, number>>;
	}
}
