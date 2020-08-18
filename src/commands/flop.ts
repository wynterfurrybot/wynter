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

	public async run(msg: Message): Promise<Message> {
		if (msg.mentions.users.array() === undefined || msg.mentions.users.array().length === 0) {
			return msg.channel.send(
				new MessageEmbed().
					setColor(0x00ff00).
					setTitle('Flop!').
					setDescription(`${msg.author} has flopped on the ground!`).
					setThumbnail('https://i.imgur.com/mZo6DnU.png'),
			);
		} else {
			return msg.channel.send(
				new MessageEmbed().
					setColor(0x00ff00).
					setTitle('Flop!').
					setDescription(`${msg.author} has flopped on ${msg.mentions.users.first()}!`).
					setThumbnail('https://i.imgur.com/mZo6DnU.png'),
			);
		}
	}
}
