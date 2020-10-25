import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'martini',
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
					.setDescription(`${msg.author} here's your martini! \n\nDon't get too drunk`)
					.setThumbnail(
						'https://www.liquor.com/thmb/SXyXRSEiNlSIWioGE8GOMb7arPM=/735x0/__opt__aboutcom__coeus__resources__content_migration__liquor__2018__09__05093330__dry-martini-720x720-recipe-8a80821c4ca944849690af8cda90cc03.jpg',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						// eslint-disable-next-line quotes
						.setTitle('It\'s time to get drunk!')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a bottle of martini!`)
						.setThumbnail(
							'https://www.liquor.com/thmb/SXyXRSEiNlSIWioGE8GOMb7arPM=/735x0/__opt__aboutcom__coeus__resources__content_migration__liquor__2018__09__05093330__dry-martini-720x720-recipe-8a80821c4ca944849690af8cda90cc03.jpg',
						),
				);
			});

			return msg;
		}
	}
}
