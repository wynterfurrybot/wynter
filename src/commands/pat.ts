import { MessageEmbed } from 'discord.js';
import { Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	constructor() {
		super({
			name: 'pat',
      aliases:['pet'],
			cooldown: 5,
			usage: '<member>',
		});
	}
	public async run(msg: Message) {
		msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Pat!')
				.setDescription(
					`${msg.author} has pat ${msg.mentions.users.first()} softly on the head!`,
				)
				.setThumbnail(
					'https://d.facdn.net/art/itsmekurisu/1550247117/1550247117.itsmekurisu_corrina.png',
				),
		);
	}
}
