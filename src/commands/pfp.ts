import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'pfp',
			cooldown: 5,
			usage: '<user>',
			aliases: ['avatar'],
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (msg.mentions.users.array() === undefined || msg.mentions.users.array().length === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('User PFP!')
					.setDescription('Please mention a user'),
			);
		} else {
			const user = msg.mentions.members!.first();
			let pfp = user!.user.avatarURL();
			pfp = pfp + '?size=512';

			return msg.channel.send(
				new MessageEmbed().setColor(0x00ff00).setTitle('User PFP!').setImage(pfp),
			);
		}
	}
}
