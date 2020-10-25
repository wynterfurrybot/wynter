import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';
import axios from 'axios';

export default class extends Command {
	public constructor() {
		super({
			name: 'boop',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		axios
			.get('https://api.furrycentr.al/sfw/boop')
			.then(function(response) {
				console.log(response.data.result.imgUrl);
				if (msg.author.id === msg.mentions.users.first()!.id) return msg;
				return msg.channel.send(
					`**${msg.member!.displayName}** has booped **${
						msg.mentions.members!.first()!.displayName
					}** right on their snoot!`,
					new MessageEmbed()
						.setColor(0x00ff00)
						.setDescription(`[Direct Image](${response.data.result.imgUrl})`)
						.setImage(response.data.result.imgUrl),
				);
			})
			.catch(function(error) {
				console.log(error);
				if (msg.author.id === msg.mentions.users.first()!.id) return msg;
				return msg.channel.send(
					`**${msg.member!.displayName}** has booped **${
						msg.mentions.members!.first()!.displayName
					}** right on their snoot!`,
					new MessageEmbed()
						.setColor(0x00ff00)
						.setDescription(
							'[Direct Image](https://i.pinimg.com/originals/4c/02/bd/4c02bdb8056ef9bb3883f38eb59d4b8e.jpg)',
						)
						.setFooter('Wynter API is down | Showing static image.')
						.setImage(
							'https://i.pinimg.com/originals/4c/02/bd/4c02bdb8056ef9bb3883f38eb59d4b8e.jpg',
						),
				);
			});

		return msg;
	}
}
