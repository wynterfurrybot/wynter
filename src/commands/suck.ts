import { MessageEmbed, Message, TextChannel } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'suck',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if ((msg.channel as TextChannel).nsfw === false) {
			return msg.channel.send(
				new MessageEmbed().
					setColor(0x00ff00).
					setTitle('Not A NSFW Channel').
					setDescription('The channel you just ran the command in is not NSFW!').
					setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
			);
		}
		
		return msg.channel.send(
			new MessageEmbed().
				setColor(0x00ff00).
				setTitle('Spitters are quitters.').
				setDescription(
					`${msg.author} has sucked off ${msg.mentions.users.first()}, swallowing their cum`,
				).
				setThumbnail(
					'https://w1680.luscious.net/laise/342630/frrbq_22_01DBK73R7KYGJDX9X3D0972X8A.1680x0.jpg',
				),
		);
	}
}
