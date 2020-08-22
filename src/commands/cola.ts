import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'cola',
			cooldown: 5,
			usage: '[member]',
			aliases: ['coke'],
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Soft drink')
					.setDescription(`${msg.author} chugs some coke!`)
					.setThumbnail(
						'https://i.pinimg.com/originals/33/4d/a7/334da791a8e7df928905484fdab19262.jpg',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('Soft drink')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a bottle of coke!`)
						.setThumbnail(
							'https://i.pinimg.com/originals/33/4d/a7/334da791a8e7df928905484fdab19262.jpg',
						),
				);
			});

			return msg;
		}
	}
}
