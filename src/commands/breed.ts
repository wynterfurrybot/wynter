import { TextChannel } from 'discord.js';
import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'breed',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if ((msg.channel as TextChannel).nsfw === false) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Not A NSFW Channel')
					.setDescription('The channel you just ran the command in is not NSFW!')
					.setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
			);
		}

		if(msg.author.id === msg.mentions.users.first()!.id) return msg;

		return msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('GIVE ME YOUR CUBS!')
				.setDescription(
					`${
						msg.author
					} has impregnated ${msg.mentions.users.first()}, giving them a healthy litter!`,
				)
				.setThumbnail(
					'https://us.rule34.xxx//images/364/3db9b8b409f5100aafc62f6352d31db1c60f3c64.png',
				),
		);
	}
}
