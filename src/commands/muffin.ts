import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'muffin',
			cooldown: 5,
			usage: '[member]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('I wanna die!')
					.setDescription(`${msg.author} It's muffin time! \n\n*gives you a muffin*`)
					.setThumbnail(
						'https://modworkshop.net/mydownloads/previews/preview_3168_1542481291_794f87346e5f426c4c45c7ab3a0711ec.png',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('I wanna die!')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a muffin!`)
						.setThumbnail(
							'https://modworkshop.net/mydownloads/previews/preview_3168_1542481291_794f87346e5f426c4c45c7ab3a0711ec.png',
						),
				);
			});

			return msg;
		}
	}
}
