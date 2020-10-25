import { MessageEmbed, Message } from 'discord.js';

import FindGuild from '../lib/DatabaseWrapper/FindGuild';
import UpdateGuild from '../lib/DatabaseWrapper/UpdateGuild';

import Command, { CommandUseIn } from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'muterole',
			cooldown: 5,
			usage: '[set/remove] [role]',
			useIn: CommandUseIn.guild,
		});
	}

	public async run(msg: Message, args: string[]): Promise<Message> {
		if (!msg.member!.hasPermission('MANAGE_GUILD')) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('No permissions')
					.setDescription(`You do not have permissions to set the mute role in ${msg.guild!.name}`)
					.setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
			);
		}

		const guild = await FindGuild(msg.guild!.id);

		if (args[0] === 'set') {
			const role = msg.mentions.roles.first() ?? (await msg.guild!.roles.fetch(args[1]));

			if (!role) {
				return await msg.channel!.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('Error!')
						.setDescription('Please mention a role!'),
				);
			}

			await UpdateGuild(msg.guild!.id, {
				muteRole: role.id,
			});

			return await msg.channel!.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Success!')
					.setDescription('Successfully set the mute role!'),
			);
		} else if (args[0] === 'remove') {
			await UpdateGuild(msg.guild!.id, {
				muteRole: null,
			});

			return await msg.channel!.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Success!')
					.setDescription('Successfully removed the mute role!'),
			);
		} else {
			return await msg.channel!.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Success!')
					.setDescription(
						`The current mute role is ${await msg.guild!.roles.fetch(guild!.muteRole!)}`,
					),
			);
		}
	}
}
