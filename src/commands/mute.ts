import { MessageEmbed, Message, TextChannel } from 'discord.js';

import FindGuild from '../lib/DatabaseWrapper/FindGuild';

import Command, { CommandUseIn } from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'mute',
			cooldown: 5,
			usage: '<member> [reason]',
			useIn: CommandUseIn.guild,
		});
	}

	public async run(msg: Message, args: string[]): Promise<Message> {
		if (!msg.member!.hasPermission('KICK_MEMBERS')) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('No permissions')
					.setDescription(`You do not have permissions to mute people on ${msg.guild!.name}`)
					.setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
			);
		}

		const muteRole = await msg.guild!.roles.fetch((await FindGuild(msg.guild!.id))!.muteRole!);

		if (!muteRole) {
			return await msg.channel!.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Error!')
					.setDescription(
						`Please run \`${
							(await FindGuild(msg.guild!.id))!.prefix
						}muterole set <roleid/@mention>\` to set the mute role and try again!`,
					),
			);
		}

		const member = msg.mentions.members!.first() ?? (await msg.guild!.members.fetch(args[0]));

		try {
			await member!.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('MUTE!')
					.setDescription(
						`You have been muted on ${msg.guild!.name}. The reasoning can be found below: \n\n${
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

		if (msg.guild!.id === '725201209358549012') {
			const cfRole = msg.guild!.roles.cache.find((r) => r.id === '725462565852938301');
			member!.roles.remove(cfRole!);
		}

		member!.roles.add(muteRole);

		const channel = msg.guild!.channels.cache.find((channel) => channel.name === 'case_logs');

		const embed = new MessageEmbed()
			// Set the title of the field
			.setTitle('Mute')
			// Set the color of the embed
			.setColor(0xff0000)
			// Set the main content of the embed
			.setDescription(
				`${msg.author} has muted ${member} (${member.user.username}#${member.user.discriminator}) for the following reason: \n\n${msg.content}`,
			);

		(channel as TextChannel).send(embed);

		msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Member Muted')
				.setDescription('Successfully Muted a user')
				.setThumbnail(
					'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
				),
		);

		return msg.delete();
	}
}
