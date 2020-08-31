import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: '8ball',
			cooldown: 5,
			usage: '[question]',
		});
	}

	public async run(msg: Message, args: string[]): Promise<Message> {
		const responses = [
			'As I see it, yes',
			'Ask again later',
			'Better not tell you now',
			'I cannot predict this right now',
			'Concentrate and ask again.',
			'Don’t count on it.',
			'It is certain.',
			'It is decidedly so.',
			'Most likely.',
			'My reply is no.',
			'My sources say no.',
			'Outlook not so good.',
			'Outlook pawsitive.',
			'Reply hazy, try again.',
			'Signs point to yes.',
			'Very doubtful.',
			'Without a doubt.',
			'Yes.',
			'Yes – definitely.',
			'You may rely on it.',
		];
		let question = '';
		args.forEach((arg) => {
			question = question + ' ' + arg;
		});

		return msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Magic 8Ball says...')
				.setDescription(
					`Question: ${question} \n Response: ${
						responses[Math.floor(Math.random() * (responses.length - 0) + 0)]
					}`,
				)
				.setThumbnail('http://www.otcpas.com/wp-content/uploads/magic-eight-ball.jpg'),
		);
	}
}
