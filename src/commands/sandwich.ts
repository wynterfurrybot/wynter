import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'sandwich',
			cooldown: 5,
			usage: '[member]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Sandwich!')
					.setDescription(`${msg.author} here's your Sandwich!`)
					.setThumbnail(
						'https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/egg-cress-club-sandwich_0.jpg',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('Sandwich!')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a sandwich!`)
						.setThumbnail(
							'https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/egg-cress-club-sandwich_0.jpg',
						),
				);
			});

			return msg;
		}
	}
}
