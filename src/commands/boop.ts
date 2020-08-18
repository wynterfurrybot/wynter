import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'boop',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message) {
		// @ts-ignore	
		if(msg.author.id === msg.mentions.users.first().id) {return;}
		msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Boop!')
				.setDescription(
					`${msg.author} has booped ${msg.mentions.users.first()} right on their snoot!`,
				)
				.setThumbnail(
					'https://i.pinimg.com/originals/4c/02/bd/4c02bdb8056ef9bb3883f38eb59d4b8e.jpg',
				),
		);
	}
}
