import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'howgay',
			cooldown: 5,
			usage: '[member]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					// eslint-disable-next-line quotes
					.setTitle("You're fucking gay!")
					.setDescription(`${msg.author} is ${Math.floor(Math.random() * 101)}% gay`)
					.setThumbnail('https://static1.e926.net/data/7b/4e/7b4ef041d3104368dcb0a40ba9e6fb93.png'),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						// eslint-disable-next-line quotes
						.setTitle("You're fucking gay")
						.setDescription(`<@${member.id}> is ${Math.floor(Math.random() * 101)}% gay`)
						.setThumbnail(
							'https://static1.e926.net/data/7b/4e/7b4ef041d3104368dcb0a40ba9e6fb93.png',
						),
				);
			});

			return msg;
		}
	}
}
