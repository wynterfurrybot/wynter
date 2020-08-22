import { MessageEmbed, Message, TextChannel } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'unmute',
			cooldown: 5,
			usage: '<member> [reason]',
		});
	}

	public async run(msg: Message): Promise<Message> {
		if (!msg.member!.hasPermission('KICK_MEMBERS')) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('No permissions')
					.setDescription(`You do not have permissions to unmute people on ${msg.guild!.name}`)
					.setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
			);
		}

		const muteRole = msg.guild!.roles.cache.find((r) => r.name === ('Muted' || 'muted'));

		if (!muteRole) {
			return await msg.channel!.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Error!')
					.setDescription('Unable to find a role name `Muted`! Please make one and try again'),
			);
		}

		const member = msg.mentions.members!.first();

		await member!.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('UNMUTE!')
				.setDescription(
					`You have been unmuted on ${msg.guild!.name}. The reasoning can be found below: \n\n${
						msg.content
					}`,
				)
				.setThumbnail(
					'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
				),
		);

		if (msg.guild!.id === '725201209358549012') {
			const cfRole = msg.guild!.roles.cache.find((r) => r.name === 'Verified Floof');
			member!.roles.add(cfRole!);
		}

		member!.roles.remove(muteRole);

		const channel = msg.guild!.channels.cache.find((channel) => channel.name === 'case_logs');

		const embed = new MessageEmbed()
			// Set the title of the field
			.setTitle('Unmute')
			// Set the color of the embed
			.setColor(0xff0000)
			// Set the main content of the embed
			.setDescription(
				`${msg.author} has unmuted ${msg.mentions.users.first()} (${
					msg.mentions.users.first()!.username
				}#${msg.mentions.users.first()!.discriminator}) for the following reason: \n\n${
					msg.content
				}`,
			);

		(channel as TextChannel).send(embed);

		msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Member Unmuted')
				.setDescription('Successfully Unmuted a user')
				.setThumbnail(
					'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
				),
		);

		return msg.delete();
	}
}
