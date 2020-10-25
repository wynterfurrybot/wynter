import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'bite',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (msg.author.id === msg.mentions.users.first()!.id) return msg;
		return msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Bite!')
				.setDescription(`${msg.author} has nibbled at ${msg.mentions.users.first()}'s ear!'`)
				.setThumbnail(
					'https://i.pinimg.com/originals/d3/83/57/d383575a560d2cdc413d5945ea608286.png',
				),
		);
	}
}
