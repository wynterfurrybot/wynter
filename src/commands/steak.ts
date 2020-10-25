import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'steak',
			cooldown: 5,
			usage: '[member]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Steak!')
					.setDescription(`${msg.author} here's your steak!`)
					.setThumbnail(
						'https://foremangrillrecipes.com/wp-content/uploads/2013/06/featured-ribeye-steak-foreman-grill.jpg',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('Steak!')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> some steak!`)
						.setThumbnail(
							'https://foremangrillrecipes.com/wp-content/uploads/2013/06/featured-ribeye-steak-foreman-grill.jpg',
						),
				);
			});

			return msg;
		}
	}
}
