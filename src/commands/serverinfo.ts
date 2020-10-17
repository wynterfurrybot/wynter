import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'serverinfo',
			cooldown: 5,
			usage: '',
		});
	}

	public async run(msg: Message): Promise<Message> {
		const guild = msg.guild;
		let users = 0;
		let bots = 0;
		// eslint-disable-next-line @typescript-eslint/ban-ts-comment
		//@ts-ignore
		const mem = guild.members.cache.array();
		mem.forEach(async function (u) {
			if (u.user.bot) {
				// Add to bot count
				bots = bots + 1;
			} else {
				users = users + 1;
			}
		});

		return msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Server Info!')
				.setDescription(
					`${msg.guild!.name} \n\nOwner: ${msg.guild!.owner} \n\nCreated at: ${
						msg.guild!.createdAt
					} \nRegion: ${msg.guild!.region} \nMembers: ${users} \nBots: ${bots}`,
				)
				.setThumbnail(msg.guild!.iconURL()!),
		);
	}
}
