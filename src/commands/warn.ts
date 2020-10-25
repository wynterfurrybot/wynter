import { Message, MessageEmbed, TextChannel } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'warn',
			cooldown: 5,
			usage: '<toggle>',
		});
	}

	public async run(msg: Message, args: string[]): Promise<Message> {
		if (!msg.member!.hasPermission('KICK_MEMBERS')) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('No permissions')
					.setDescription(
						`You do not have permissions to kick people on ${
							msg.guild!.name
						} - thus you cannot warn this user.`,
					)
					.setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
			);
		}
		const member = msg.mentions.members!.first() ?? (await msg.guild!.members.fetch(args[0]));

		try {
			member!.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('WARNING:')
					.setDescription(
						`You have been warned on ${msg.guild!.name}. The reasoning can be found below: \n\n${
							msg.content
						}`,
					)
					.setThumbnail(
						'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
					),
			);
		} catch (err) {
			// NOT EMPTY
		}

		const channel = msg.guild!.channels.cache.find((channel) => channel.name === 'case_logs');

		const embed = new MessageEmbed()
			// Set the title of the field
			.setTitle('Warn')
			// Set the color of the embed
			.setColor(0xff0000)
			// Set the main content of the embed
			.setDescription(
				`${msg.author} has warned ${member} (${member.user.username}#${member.user.discriminator}) for the following reason: \n\n${msg.content}`,
			);

		(channel as TextChannel).send(embed);

		msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Member Warned')
				.setDescription('Successfully warned a user')
				.setThumbnail(
					'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
				),
		);

		return msg.delete();
	}
}
