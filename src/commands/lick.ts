import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'lick',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		return msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Slurp!')
				.setDescription(
					`${msg.author} has licked ${msg.mentions.users.first()}, giving them a bath!`,
				)
				.setThumbnail(
					'https://i.pinimg.com/originals/d3/83/57/d383575a560d2cdc413d5945ea608286.png',
				),
		);
	}
}
