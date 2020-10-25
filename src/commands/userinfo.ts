import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'userinfo',
			cooldown: 5,
			usage: '<user>',
			aliases: ['profile'],
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (msg.mentions.users.array() === undefined || msg.mentions.users.array().length === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('User Info!')
					.setDescription('Please mention a user'),
			);
		} else {
			const user = msg.mentions.members!.first();

			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('User Info!')
					.setDescription(
						`${user} \n\nUsername: ${user!.user.username} \nUser Created:${
							user!.user.createdAt
						} \nJoined the server: ${user!.joinedAt}`,
					)
					.setThumbnail(user!.user.avatarURL()!),
			);
		}
	}
}
