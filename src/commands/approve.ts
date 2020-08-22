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
			// eslint-disable-next-line @typescript-eslint/no-non-null-asserted-optional-chain
			oldRole = msg.guild?.roles.cache.find((r) => r.name === 'New Floof')!;
			// eslint-disable-next-line @typescript-eslint/no-non-null-asserted-optional-chain
			newRole = msg.guild?.roles.cache.find((r) => r.name === 'Verified Floof')!;

			member!.roles.remove(oldRole);
			member!.roles.add(newRole);
		} else if (msg.guild!.id === '514478309678120960') {
			// eslint-disable-next-line @typescript-eslint/no-non-null-asserted-optional-chain
			newRole = msg.guild?.roles.cache.find((r) => r.name === 'Member')!;
			member!.roles.add(newRole);
		}

		await msg.channel.send('Approved');

		return msg.delete();
	}
}
