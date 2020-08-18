import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'blep',
			cooldown: 5,
			usage: '',
		});
	}

	public async run(msg: Message): Promise<Message> {
		return msg.channel.send(
			new MessageEmbed().
				setColor(0x00ff00).
				setTitle('Blep!').
				setDescription(`${msg.author} has done a blep!`).
				setThumbnail('https://i.redd.it/o49rv5hjacm21.png'),
		);
	}
}
