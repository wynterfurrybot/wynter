import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';
import axios from 'axios';

export default class extends Command {
	public constructor() {
		super({
			name: 'dog',
			cooldown: 5,
			usage: '<member>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		axios
			.get('https://api.furrycentr.al/sfw/dog')
			.then(function (response) {
				console.log(response.data.result.imgUrl);
				return msg.channel.send(
					`**${msg.member!.displayName}** Here's your doggo!`,
					new MessageEmbed()
						.setColor(0x00ff00)
						.setDescription(`[Direct Image](${response.data.result.imgUrl})`)
						.setImage(response.data.result.imgUrl),
				);
			})
			.catch(function (error) {
				console.log(error);
				return msg.channel.send(
					`**${msg.member!.displayName}** Here's your doggo!`,
					new MessageEmbed()
						.setColor(0x00ff00)
						.setDescription(
							'[Direct Image](https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=640:*)',
						)
						.setImage(
							'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=640:*',
						),
				);
			});

		return msg;
	}
}
