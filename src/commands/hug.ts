import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

import axios from "axios";

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

		axios.get('https://api.furry.bot/v2/furry/hug')
		.then(function (response) {
		  console.log(response.data.images[0].url);
		  if (msg.mentions.users.first()!.id === msg.author!.id) {
			return msg.channel.send(`**${msg.author.username}** has hugged themselves, what a loner!`,
				new MessageEmbed()
				.setColor(0x00ff00)
				.setDescription(`[Direct Image](${response.data.images[0].url}) \n[Report Image](${response.data.images[0].reportURL})`)
				.setImage(
					response.data.images[0].url,
				),
			);
		} else {
			return msg.channel.send(`**${msg.author.username}** has given **${msg.mentions.users.first()!.username}** a hug!`,
				new MessageEmbed()
				.setColor(0x00ff00)
				.setDescription(`[Direct Image](${response.data.images[0].url}) \n[Report Image](${response.data.images[0].reportURL})`)
				.setImage(
					response.data.images[0].url,
				),
			);
		}
		})
		.catch(function (error) {
		  console.log(error);
		  if (msg.mentions.users.first()!.id === msg.author!.id) {
			return msg.channel.send(`**${msg.author.username}** has hugged themselves, what a loner!`,
				new MessageEmbed()
				.setColor(0x00ff00)
				.setDescription(`[Direct Image](https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg)`)
				.setFooter('furry.bot API is down | Showing static image.')
				.setImage(
					'https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg',
				),
			);
		} else {
			return msg.channel.send(`**${msg.author.username}** has given **${msg.mentions.users.first()!.username}** a hug!`,
				new MessageEmbed()
				.setColor(0x00ff00)
				.setDescription(`[Direct Image](https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg)`)
				.setFooter('furry.bot API is down | Showing static image.')
				.setImage(
					'https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg',
				),
			);
		}
		});
	  
		return msg;
		
	}
}
