import { Message } from 'discord.js';

export default abstract class Command {
	public name: string;
	public usage: string;
	public useIn: CommandUseIn;
	public cooldown: number;
	public aliases: string[];
	public constructor(options?: CommandOptions) {
		this.name = options!.name ?? __filename;
		this.usage = options!.usage ?? '';
		this.useIn = options!.useIn ?? CommandUseIn.both;
		this.cooldown = options!.cooldown ?? 0;
		this.aliases = options!.aliases ?? [];
	}

	public abstract run(msg: Message, args: string[]): Promise<Message | void | null>;
}

export interface CommandOptions {
	name?: string;
	usage?: string;
	useIn?: CommandUseIn;
	cooldown?: number;
	aliases?: string[];
}

export enum CommandUseIn {
	guild,
	dm,
	both,
}
