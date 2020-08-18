import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'help',
			cooldown: 5,
			usage: '',
		});
	}

	public async run(msg: Message) {
    msg.channel.send(
      new MessageEmbed()
        .setColor(0x00ff00)
        .setTitle('Wynter v1.0')
        .setDescription(
          `Commands: https://docs.furrycentr.al/commands \n\nMade by Darkmane Arweinydd | Ported to ts by Relms & Darkmane Arweinydd \n\nBeta Testers: Alex Malebogh, May, Hunter`,
        ),
    );
	}
}
