import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'pinacolada',
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
					.setTitle("It's time to get drunk!")
					.setDescription(`${msg.author} here's your pina colada, don't get too drunk!`)
					.setThumbnail(
						'https://www.liquor.com/thmb/zPl7fCzXHeHD8uBo4z194OFRabA=/735x0/__opt__aboutcom__coeus__resources__content_migration__liquor__2019__02__13090826__pina-colada-720x720-recipe-253f1752769447f6998afd2b9469c24e.jpg',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						// eslint-disable-next-line quotes
						.setTitle("It's time to get drunk!")
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a pina colada!`)
						.setThumbnail(
							'https://www.liquor.com/thmb/zPl7fCzXHeHD8uBo4z194OFRabA=/735x0/__opt__aboutcom__coeus__resources__content_migration__liquor__2019__02__13090826__pina-colada-720x720-recipe-253f1752769447f6998afd2b9469c24e.jpg',
						),
				);
			});

			return msg;
		}
	}
}
