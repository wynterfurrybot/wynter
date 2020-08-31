import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';
import axios from 'axios';

export default class extends Command {
	public constructor() {
		super({
			name: 'lick',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		axios
			.get('https://api.furrycentr.al/sfw/lick')
			.then(function (response) {
				console.log(response.data.result.imgUrl);
				return msg.channel.send(
					`**${msg.member!.displayName}** has licked **${
						msg.mentions.members!.first()!.displayName
					}**, giving them a bath!`,
					new MessageEmbed()
						.setColor(0x00ff00)
						.setDescription(`[Direct Image](${response.data.result.imgUrl})`)
						.setImage(response.data.result.imgUrl),
				);
			})
			.catch(function (error) {
				console.log(error);
				return msg.channel.send(
					`**${msg.member!.displayName}** has licked **${
						msg.mentions.members!.first()!.displayName
					}**, giving them a bath!`,
					new MessageEmbed()
						.setColor(0x00ff00)
						.setDescription(
							'[Direct Image](https://static1.e926.net/data/sample/cc/91/cc9149350a917425d1438335bc3821ff.jpg)',
						)
						.setFooter('Wynter API is down | Showing static image.')
						.setImage(
							'https://static1.e926.net/data/sample/cc/91/cc9149350a917425d1438335bc3821ff.jpg',
						),
				);
			});

		return msg;
	}
}
