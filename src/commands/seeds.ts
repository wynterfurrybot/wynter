import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'seeds',
			cooldown: 5,
			usage: '[member]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.mentions || msg.mentions.users.size === 0) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Birb!')
					.setDescription(`${msg.author} here's your seeds!`)
					.setThumbnail(
						'https://cdn.bmstores.co.uk/images/hpcProductImage/imgFull/275212-277654-Glennwood-Wild-Bird-Seed-Mix1.jpg',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('Birb!')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> some seeds!`)
						.setThumbnail(
							'https://cdn.bmstores.co.uk/images/hpcProductImage/imgFull/275212-277654-Glennwood-Wild-Bird-Seed-Mix1.jpg',
						),
				);
			});

			return msg;
		}
	}
}
