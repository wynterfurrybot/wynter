import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'menu',
			cooldown: 5,
			usage: '',
		});
	}

	public async run(msg: Message): Promise<Message> {
		return msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Menu')
				.setDescription(
					'**__Food__** \nCookie, Pineapple, Sandwich, Steak, Pizza, Muffin \n\n**__Alcohol__** \nWhiskey, Vodka, Martini, Beer, Rum, Pina Colada \n\n**__Non-alcoholic drinks__** \nCoke, Tea, Coffee',
				),
		);
	}
}
