import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'hug',
			aliases: ['cuddle', 'hugs'],
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message) {
		if (msg.mentions.users.first()!.id === msg.author!.id) {
			msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Hug!')
					.setDescription(`${msg.author} has hugged themselves, what a loner!`)
					.setThumbnail(
						'https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg',
					),
			);
		} else {
			msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Hug!')
					.setDescription(`${msg.author} has given ${msg.mentions.users.first()} a hug!`)
					.setThumbnail(
						'https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg',
					),
			);
		}
	}
}
