import { Message } from 'discord.js';

import Command from '../lib/structures/Command';
import findGuild from '../lib/DatabaseWrapper/FindGuild';
import updateGuild from '../lib/DatabaseWrapper/UpdateGuild';

export default class extends Command {
	public constructor() {
		super({
			name: 'prefix',
			cooldown: 5,
			usage: '[prefix]',
		});
	}

	public async run(msg: Message, args: string[]): Promise<Message> {
		if (args.length === 0) {
			return msg.channel.send(
				`The current server prefix is \`${(await findGuild(msg.guild!.id))!.prefix}\``,
			);
		} else {
			await updateGuild(msg.guild!.id, {
				prefix: args[0],
			});

			return msg.channel.send(
				`I have updated the prefix to \`${(await findGuild(msg.guild!.id))!.prefix}\``,
			);
		}
	}
}
