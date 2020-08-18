import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'userinfo',
			cooldown: 5,
			usage: '<user>',
		});
	}

	public async run(msg: Message) {
		if (msg.mentions.users.array() === undefined || msg.mentions.users.array().length == 0) {//@ts-ignore
      var user = msg.guild.members.fetch(msg.author.id);
			msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('User Info!') //@ts-ignore
					.setDescription(`Please mention a user`) //@ts-ignore,
			);
		} else {
			// @ts-ignore
      var user = msg.mentions.members.first();
      msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('User Info!') //@ts-ignore
					.setDescription(`${user} \n\nUsername: ${user.user.username} \nUser Created:${user.user.createdAt} \nJoined the server: ${user.joinedAt}`)//@ts-ignore
					.setThumbnail(msg.author.avatarURL()),
			);
		}
	}
}
