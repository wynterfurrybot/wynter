import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'throwdict',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (msg.author.id === msg.mentions.users.first()!.id) return msg;
		return msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Do u even knowledge?')
				.setDescription(
					`${
						msg.author
					} has thrown a dictonary at ${msg.mentions.users.first()}, landing softly on their head!`,
				)
				.setThumbnail('https://i.imgur.com/n58IlmY.png'),
		);
	}
}
