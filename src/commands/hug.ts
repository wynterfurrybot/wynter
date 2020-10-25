import { Message, MessageEmbed } from 'discord.js';
import Command from '../lib/structures/Command';
import axios from 'axios';

export default class extends Command {
	public constructor() {
		super({
			name: 'hug',
			aliases: ['cuddle', 'hugs'],
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		axios
			.get('https://api.furrycentr.al/sfw/hug')
			.then(function(response) {
				console.log(response.data.result.imgUrl);
				if (msg.mentions.users.first()!.id === msg.author!.id) {
					return msg.channel.send(
						`**${msg.member!.displayName}** has hugged themselves, what a loner!`,
						new MessageEmbed()
							.setColor(0x00ff00)
							.setDescription(`[Direct Image](${response.data.result.imgUrl})`)
							.setImage(response.data.result.imgUrl),
					);
				} else {
					return msg.channel.send(
						`**${msg.member!.displayName}** has given **${
							msg.mentions.members!.first()!.displayName
						}** a hug!`,
						new MessageEmbed()
							.setColor(0x00ff00)
							.setDescription(`[Direct Image](${response.data.result.imgUrl})`)
							.setImage(response.data.result.imgUrl),
					);
				}
			})
			.catch(function(error) {
				console.log(error);
				if (msg.mentions.users.first()!.id === msg.author!.id) {
					return msg.channel.send(
						`**${msg.member!.displayName}** has hugged themselves, what a loner!`,
						new MessageEmbed()
							.setColor(0x00ff00)
							.setDescription(
								'[Direct Image](https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg)',
							)
							.setFooter('Wynter API is down | Showing static image.')
							.setImage(
								'https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg',
							),
					);
				} else {
					return msg.channel.send(
						`**${msg.member!.displayName}** has given **${
							msg.mentions.members!.first()!.displayName
						}** a hug!`,
						new MessageEmbed()
							.setColor(0x00ff00)
							.setDescription(
								'[Direct Image](https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg)',
							)
							.setFooter('Wynter API is down | Showing static image.')
							.setImage(
								'https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg',
							),
					);
				}
			});

		return msg;
	}
}
