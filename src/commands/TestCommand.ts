import { Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	constructor() {
		super({
			name: 'test',
		});
	}
	public async run(msg: Message) {
		msg.channel.send('HELLO!');
	}
}
