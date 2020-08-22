import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'pineapple',
			cooldown: 5,
			usage: '[member]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Pineapple!')
					.setDescription(`${msg.author} here's your pineapple slices!`)
					.setThumbnail('https://www.organicfacts.net/wp-content/uploads/pineapplecalories.jpg'),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('Pineapple!')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> some pineapple slices!`)
						.setThumbnail('https://www.organicfacts.net/wp-content/uploads/pineapplecalories.jpg'),
				);
			});

			return msg;
		}
	}
}
