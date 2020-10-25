import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'rum',
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
					.setTitle('It\'s time to get drunk!')
					.setDescription(`${msg.author} here's your rum! \n\nDon't get too drunk`)
					.setThumbnail(
						'https://shop.rammstein.de/img/original/katalog/1617/396/flasche-rum-null-2.jpg',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						// eslint-disable-next-line quotes
						.setTitle('It\'s time to get drunk!')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a bottle of rum!`)
						.setThumbnail(
							'https://shop.rammstein.de/img/original/katalog/1617/396/flasche-rum-null-2.jpg',
						),
				);
			});

			return msg;
		}
	}
}
