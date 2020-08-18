import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'snowball',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		return msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Snowball!')
				.setDescription(
					`${msg.author} has thrown a snowball directly at ${msg.mentions.users.first()}`,
				)
				.setThumbnail(
					'http://d.facdn.net/art/olypixandstuff/1265692624/1265692624.olypixandstuff_1263408058.sapphwolf_snowballfight2.png',
				),
		);
	}
}
