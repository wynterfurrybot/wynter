import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'kiss',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		return msg.channel.send(
			new MessageEmbed().
				setColor(0x00ff00).
				setTitle('Kiss!').
				setDescription(`${msg.author} has given ${msg.mentions.users.first()} a kiss on the cheek`).
				setThumbnail(
					'https://external-preview.redd.it/Au9jfafmj8FSCgkzvu1odMbw7tLRaye5hWXv5z-Ezus.png?auto=webp&s=bdd727bc7ae09d71521e6d8cec18ef1f69d0a207',
				),
		);
	}
}
