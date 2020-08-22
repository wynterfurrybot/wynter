import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'pepsi',
			cooldown: 5,
			usage: '[member]',
			aliases: ['bepis'],
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Soft drink')
					.setDescription(`${msg.author} chugs some pepsi!`)
					.setThumbnail('https://www.drinkstuff.com/productimg/102915_large.jpg'),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('Soft drink')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a bottle of pepsi!`)
						.setThumbnail('https://www.drinkstuff.com/productimg/102915_large.jpg'),
				);
			});

			return msg;
		}
	}
}
