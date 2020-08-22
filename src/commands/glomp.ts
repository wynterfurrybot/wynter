import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'glomp',
			aliases: ['tacklehug'],
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		return msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Glomp!')
				.setDescription(`${msg.author} has flopped on top of ${msg.mentions.users.first()}!'`)
				.setThumbnail('https://d.facdn.net/art/zaezar/1502813432/1502813432.zaezar_glomp.png'),
		);
	}
}
