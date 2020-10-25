import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'nuzzle',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (msg.author.id === msg.mentions.users.first()!.id) return msg;
		return msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Nuzzle!')
				.setDescription(`${msg.author} has nuzzled ${msg.mentions.users.first()}!`)
				.setThumbnail(
					'https://pm1.narvii.com/6427/42cdd0b2870e26482cd6907bce2edca12a82286c_hq.jpg',
				),
		);
	}
}
