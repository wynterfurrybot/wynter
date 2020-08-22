import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'tea',
			cooldown: 5,
			usage: '[member]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Hot drink')
					.setDescription(`${msg.author} here's your tea!`)
					.setThumbnail(
						'https://www.telegraph.co.uk/content/dam/health-fitness/2020/01/09/TELEMMGLPICT000169578515_trans%2B%2BbTl4D02iCM3NuMfK2RT0HTjsyN2j3JnAYXPi059mk8g.jpeg',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('Hot drink')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a cup of tea!`)
						.setThumbnail(
							'https://www.telegraph.co.uk/content/dam/health-fitness/2020/01/09/TELEMMGLPICT000169578515_trans%2B%2BbTl4D02iCM3NuMfK2RT0HTjsyN2j3JnAYXPi059mk8g.jpeg',
						),
				);
			});

			return msg;
		}
	}
}
