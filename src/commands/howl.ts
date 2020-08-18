import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'howl',
			cooldown: 5,
			usage: '',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (msg.mentions.users.array() === undefined || msg.mentions.users.array().length === 0) {
			return msg.channel.send(
				new MessageEmbed().
					setColor(0x00ff00).
					setTitle('AwooooOooooo!').
					setDescription(`${msg.author} has let out a big howl!`).
					setThumbnail(
						'https://d.facdn.net/art/windwo1f/1484617505/1484617505.windwo1f_wintie_s_howl.png',
					),
			);
		} else {
			return msg.channel.send(
				new MessageEmbed().
					setColor(0x00ff00).
					setTitle('AwooooOooooo!').
					setDescription(`${msg.author} howls at ${msg.mentions.users.first()}!`).
					setThumbnail(
						'https://d.facdn.net/art/windwo1f/1484617505/1484617505.windwo1f_wintie_s_howl.png',
					),
			);
		}
	}
}
