import { Message, MessageEmbed, TextChannel } from 'discord.js';

import Command from '../lib/structures/Command';
import axios from 'axios';

export default class extends Command {
	public constructor() {
		super({
			name: 'gay',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!(msg.channel as TextChannel).nsfw) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Not A NSFW Channel')
					.setDescription('The channel you just ran the command in is not NSFW!')
					.setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
			);
		}
		axios
			.get('https://api.furrycentr.al/nsfw/yiff/gay')
			.then(function (response) {
				console.log(response.data.result.imgUrl);
				return msg.channel.send(
					`**${msg.member!.displayName}** Oh murr~`,
					new MessageEmbed()
						.setColor(0x00ff00)
						.setDescription(`[Direct Image](${response.data.result.imgUrl})`)
						.setImage(response.data.result.imgUrl),
				);
			})
			.catch(function (error) {
				console.log(error);
				return msg.channel.send(
					`**${msg.member!.displayName}** Oh murr~`,
					new MessageEmbed()
						.setColor(0x00ff00)
						.setDescription('Wynter API is down, try again later.'),
				);
			});

		return msg;
	}
}
