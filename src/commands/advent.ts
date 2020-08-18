import { Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'advent',
			cooldown: 5,
			usage: '',
		});
	}

	public async run(msg: Message) {
		const items = [
			'Chocolate Reindeer',
			'Chocolate Snowflake',
			'Chocolate Elf',
			'Chocolate Santa',
			'Chocolate Christmas Tree',
		];

		const today = new Date(Date.now());

		if (today.getMonth() == 12 && today.getDay() <= 25) {
			const days = 25 - today.getDay();
			await msg.author.send(`There are ${days} day(s) left until christmas!`);
			await msg.author.send(`You got a ${items[Math.random() * (items.length - 1 - 0) + 0]}`);
		} else {
			await msg.author.send('It is not december yet - or is past christmas!');
		}
	}
}
