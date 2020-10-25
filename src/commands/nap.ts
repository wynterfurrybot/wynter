import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'nap',
			cooldown: 5,
			usage: '[member]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (msg.mentions.users.array() === undefined || msg.mentions.users.array().length === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Zzz!')
					.setDescription(`${msg.author} has took a nap!`)
					.setThumbnail('https://i.redd.it/snul7u43bsm11.jpg'),
			);
		} else {
			if (msg.author.id === msg.mentions.users.first()!.id) return msg;
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Zzz!')
					.setDescription(
						`${msg.author} has decided to fall asleep on ${msg.mentions.users.first()}!`,
					)
					.setThumbnail('https://i.redd.it/snul7u43bsm11.jpg'),
			);
		}
	}
}
