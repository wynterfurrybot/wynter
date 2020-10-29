import { Message, MessageEmbed } from 'discord.js';

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
			if (!msg.member!.hasPermission('MANAGE_GUILD')) {
				return msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('No permissions')
						.setDescription(`You do not have permissions to update the prefix in ${msg.guild!.name}`)
						.setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
				);
			}

			await updateGuild(msg.guild!.id, {
				prefix: args[0],
			});

			return msg.channel.send(
				`I have updated the prefix to \`${(await findGuild(msg.guild!.id))!.prefix}\``,
			);
		}
	}
}
