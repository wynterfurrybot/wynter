import { TextChannel } from 'discord.js';
import { MessageEmbed, Message, Role } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'approve',
			cooldown: 5,
			usage: '<user>',
		});
	}

	public async run(msg: Message): Promise<Message> {
		let oldRole: Role;
		let newRole: Role;

		if (!msg.member!.hasPermission('KICK_MEMBERS')) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('No permissions')
					.setDescription(`You do not have permissions to approve people on ${msg.guild!.name}`)
					.setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
			);
		}

		const member = msg.mentions.members!.first();

		if (msg.guild!.id === '725201209358549012') {
			oldRole = msg.guild!.roles.cache.find((r) => r.name === 'New Floof')!;
			newRole = msg.guild!.roles.cache.find((r) => r.name === 'Verified Floof')!;

			member!.roles.remove(oldRole);
			member!.roles.add(newRole);

			this.client.channels.fetch('763159605479079956').then((channel) => {
				(channel as TextChannel).send('<a:wel:742119488366837780><a:come:742119500068946084>');
				(channel as TextChannel).send(
					`Welcome <@${
						member!.id
					}> to the coolest club around! Club Floof! \n\nFeel free to go ahead and grab some roles in <#763548893195534377>!\n\nI hope you enjoy your stay here, and here's a free cookie to welcome you! :cookie: \n\n<@&736666911189893170> Please welcome the above user!`,
				);
			});
		} else if (msg.guild!.id === '514478309678120960') {
			// eslint-disable-next-line @typescript-eslint/no-non-null-asserted-optional-chain
			newRole = msg.guild?.roles.cache.find((r) => r.name === 'Member')!;
			member!.roles.add(newRole);
		}

		await msg.channel.send('Approved');

		return msg.delete();
	}
}
