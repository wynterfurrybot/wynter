import { MessageEmbed, Message, TextChannel } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'yiff',
			aliases: ['fuck'],
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
		if (msg.author.id === msg.mentions.users.first()!.id) return msg;
		return msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Yiff!')
				.setDescription(`${msg.author} has yiffed ${msg.mentions.users.first()} hard!`)
				.setThumbnail(
					'https://ci.phncdn.com/videos/201812/04/195030881/original/(m=eaAaGwObaaaa)(mh=0KDlKJW31QShbuqU)14.jpg',
				),
		);
	}
}
