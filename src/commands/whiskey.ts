import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'whiskey',
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
					.setDescription(`${msg.author} here's your whiskey! \n\nDon't get too drunk!`)
					.setThumbnail(
						'https://cdn.britannica.com/71/192771-050-CEF9CEC3/Glass-scotch-whiskey-ice.jpg',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						// eslint-disable-next-line quotes
						.setTitle("It's time to get drunk!")
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a bottle of whiskey!`)
						.setThumbnail(
							'https://cdn.britannica.com/71/192771-050-CEF9CEC3/Glass-scotch-whiskey-ice.jpg',
						),
				);
			});

			return msg;
		}
	}
}
