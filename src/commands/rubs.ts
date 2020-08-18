import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'rubs',
			cooldown: 5,
			usage: '',
		});
	}

	public async run(msg: Message) {
		if (msg.mentions.users.array() === undefined || msg.mentions.users.array().length == 0) {
			msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Belly rubs')
					.setDescription(`${msg.author} demands belly rubs!`)
					.setThumbnail(
						'https://cdn1.cloudcanvas.website/media/sites/119/2018/01/26063531/Belly-rub.jpg',
					),
			);
		} else {
			// @ts-ignore	
			if(msg.author.id === msg.mentions.users.first().id) {return;}
			msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Flop!')
					.setDescription(
						`${
							msg.author
						} rubs ${msg.mentions.users.first()}'s belly softly, causing them to kick their leg from the pets!`,
					)
					.setThumbnail(
						'https://cdn1.cloudcanvas.website/media/sites/119/2018/01/26063531/Belly-rub.jpg',
					),
			);
		}
	}
}
