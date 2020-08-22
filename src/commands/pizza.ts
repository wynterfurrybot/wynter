import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'pizza',
			cooldown: 5,
			usage: '[member]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Pizzzzzaaaaaa!')
					.setDescription(`${msg.author} has fed themselves pizza!`)
					.setThumbnail(
						'https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/08/02/16/istock-938742222.jpg',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('Pizzzzzaaaaaa!')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a box of pizza!`)
						.setThumbnail(
							'https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/08/02/16/istock-938742222.jpg',
						),
				);
			});

			return msg;
		}
	}
}
