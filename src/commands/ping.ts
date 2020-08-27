import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'ping',
			cooldown: 5,
			usage: '',
		});
	}

	public async run(msg: Message): Promise<Message> {
		return msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Pong')
				.setDescription(`Response got in ${Math.round(this.client.ws.ping)} ms`),
		);
	}
}
