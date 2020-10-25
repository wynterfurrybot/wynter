import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'cookie',
			cooldown: 5,
			usage: '[member]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Coooookiesssss!')
					.setDescription(
						`${msg.author} here's your cookie!\n\nJust like the ones mama used to make`,
					)
					.setThumbnail(
						'https://images-gmi-pmc.edge-generalmills.com/087d17eb-500e-4b26-abd1-4f9ffa96a2c6.jpg',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('Coooookiesssss!')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a cookie!`)
						.setThumbnail(
							'https://images-gmi-pmc.edge-generalmills.com/087d17eb-500e-4b26-abd1-4f9ffa96a2c6.jpg',
						),
				);
			});

			return msg;
		}
	}
}
