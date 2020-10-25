import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'coffee',
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
					.setDescription(`${msg.author} here's your coffee!`)
					.setThumbnail(
						'https://www.gannett-cdn.com/-mm-/b2b05a4ab25f4fca0316459e1c7404c537a89702/c=0-0-1365-768/local/-/media/2019/01/18/USATODAY/usatsports/gettyimages-500740897.jpg?width=660&height=372&fit=crop&format=pjpg&auto=webp',
					),
			);
		} else {
			msg.mentions.members!.forEach((member) => {
				msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('Hot drink')
						.setDescription(`<@${msg.author.id}> has given <@${member.id}> a cup of coffee!`)
						.setThumbnail(
							'https://www.gannett-cdn.com/-mm-/b2b05a4ab25f4fca0316459e1c7404c537a89702/c=0-0-1365-768/local/-/media/2019/01/18/USATODAY/usatsports/gettyimages-500740897.jpg?width=660&height=372&fit=crop&format=pjpg&auto=webp',
						),
				);
			});

			return msg;
		}
	}
}
