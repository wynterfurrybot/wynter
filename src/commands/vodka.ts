import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'vodka',
			cooldown: 5,
			usage: '[member]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					// eslint-disable-next-line quotes
					.setTitle("It's time to get drunk!")
					.setDescription(`${msg.author} has ordered some vodka to drown their sorrows.`)
					.setThumbnail(
						'https://www.solavia.co.uk/ekmps/shops/solavia2012/images/shot-vodka-glass-pack-of-6-35ml-163-1-p.jpg',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						// eslint-disable-next-line quotes
						.setTitle("It's time to get drunk!")
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a bottle of vodka!`)
						.setThumbnail(
							'https://www.solavia.co.uk/ekmps/shops/solavia2012/images/shot-vodka-glass-pack-of-6-35ml-163-1-p.jpg',
						),
				);
			});

			return msg;
		}
	}
}
