import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';
import axios from 'axios';

export default class extends Command {
	public constructor() {
		super({
			name: 'kiss',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		axios
			.get('https://api.furrycentr.al/sfw/kiss')
			.then(function (response) {
				console.log(response.data.result.imgUrl);
				return msg.channel.send(
					`**${msg.member!.displayName}** has kissed **${
						msg.mentions.members!.first()!.displayName
					}** on their cheek!`,
					new MessageEmbed()
						.setColor(0x00ff00)
						.setDescription(`[Direct Image](${response.data.result.imgUrl})`)
						.setImage(response.data.result.imgUrl),
				);
			})
			.catch(function (error) {
				console.log(error);
				return msg.channel.send(
					`**${msg.member!.displayName}** has kissed **${
						msg.mentions.members!.first()!.displayName
					}** on their cheek!`,
					new MessageEmbed()
						.setColor(0x00ff00)
						.setDescription(
							'[Direct Image](https://external-preview.redd.it/Au9jfafmj8FSCgkzvu1odMbw7tLRaye5hWXv5z-Ezus.png?auto=webp&s=bdd727bc7ae09d71521e6d8cec18ef1f69d0a207)',
						)
						.setFooter('Wynter API is down | Showing static image.')
						.setImage(
							'https://external-preview.redd.it/Au9jfafmj8FSCgkzvu1odMbw7tLRaye5hWXv5z-Ezus.png?auto=webp&s=bdd727bc7ae09d71521e6d8cec18ef1f69d0a207',
						),
				);
			});

		return msg;
	}
}
