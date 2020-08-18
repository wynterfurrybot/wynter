import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'bap',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message) {
		msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Bad furry!')
				.setDescription(
					`${msg.author} has bapped ${msg.mentions.users.first()} on the nose with a newspaper!`,
				)
				.setThumbnail('https://i.ytimg.com/vi/dNrwSeMY-bk/hqdefault.jpg'),
		);
	}
}
