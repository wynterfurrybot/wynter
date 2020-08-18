import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'serverinfo',
			cooldown: 5,
			usage: '',
		});
	}

	public async run(msg: Message) {
			msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Server Info!') //@ts-ignore
					.setDescription(`${msg.guild.name} \n\nOwner: ${msg.guild.owner} \n\nCreated at: ${msg.guild.createdAt} \nRegion: ${msg.guild.region} \nMembers: ${msg.guild.memberCount}`) //@ts-ignore
          .setThumbnail(msg.guild.iconURL())
			);
	}
}
