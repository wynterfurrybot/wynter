import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'ship',
			cooldown: 5,
			usage: '<member> [member]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Error')
					.setDescription('Please mention at least one user!'),
			);
		}

		if (msg.mentions.users.size === 1) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Ship!')
					.setDescription(`${msg.member} has shipped themselves with ${msg.mentions.users.first()}!\n\nThey got a score of${Math.floor(Math.random() * 101)}`),
			);
		}

		if (msg.mentions.users.size === 2) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Ship!')
					.setDescription(`${msg.member} has shipped ${msg.mentions.users.first()} with ${msg.mentions.users.last()}!\n\nThey got a score of${Math.floor(Math.random() * 101)}`),
			);
		}

		return msg;
	}
}
