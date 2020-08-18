import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'flop',
			cooldown: 5,
			usage: '',
		});
	}

	public async run(msg: Message) {
		if (msg.mentions.users.array() === undefined || msg.mentions.users.array().length == 0) {
			msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Flop!')
					.setDescription(`${msg.author} has flopped on the ground!`)
					.setThumbnail('https://i.redd.it/snul7u43bsm11.jpg'),
			);
		} else {
			// @ts-ignore
			if(msg.author.id === msg.mentions.users.first().id) {return;}
			msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Flop!')
					.setDescription(`${msg.author} has flopped on ${msg.mentions.users.first()}!`)
					.setThumbnail('https://i.redd.it/snul7u43bsm11.jpg'),
			);
		}
	}
}
