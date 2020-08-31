import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'stats',
			cooldown: 5,
			usage: '',
		});
	}

	public async run(msg: Message): Promise<Message> {
		const guilds = this.client.guilds.cache.array();
		let guildcount = 0;
		let members = 0;
		let channels = 0;
		guilds.forEach((guild) => {
			guildcount = guildcount + 1;
			members = members + guild.memberCount;
			const gchannels = guild.channels.cache.array();
			gchannels.forEach(() => {
				channels = channels + 1;
			});
		});
		msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Statistics')
				.setDescription(
					`Guild Count: ${guildcount} \nTotal Members: ${members} \nTotal channels: ${channels}`,
				)
				.setThumbnail('https://miro.medium.com/max/720/0*UjBJ_iTNESi6Zevk.jpg'),
		);

		return msg;
	}
}
