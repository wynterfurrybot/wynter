import { Message, MessageEmbed } from 'discord.js';
import Twitter from 'twitter';

import config from '../../config.json';

import Command from '../lib/structures/Command';
import FindUser from '../lib/DatabaseWrapper/Twitter/FindTwitter';

export default class extends Command {
	public constructor() {
		super({
			name: 'tweet',
			cooldown: 5,
			usage: '[tweet]',
		});
	}

	public async run(msg: Message, args: string[]): Promise<Message> {
		let tweet = '';
		args.forEach((arg) => {
			tweet = tweet + ' ' + arg;
		});

		if (tweet.length > 280) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Tweet failed')
					.setDescription(
						'error: too many characters',
					)
					.setThumbnail('https://static01.nyt.com/images/2014/08/10/magazine/10wmt/10wmt-articleLarge-v4.jpg?quality=75&auto=webp&disable=upscale'),
			);
		}

		// eslint-disable-next-line @typescript-eslint/no-explicit-any
		let user: any;

		if(msg.channel.id === '778794459562508298'){
			user = await FindUser('1');
			if (!user) {
				return msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('No Twitter Account Linked!')
						.setDescription(
							'I cannot tweet when you have no account linked! \nPlease link an account by going to https://furrycentr.al/twitter',
						)
						.setThumbnail('https://static01.nyt.com/images/2014/08/10/magazine/10wmt/10wmt-articleLarge-v4.jpg?quality=75&auto=webp&disable=upscale'),
				);
			}
		} else{
			user = await FindUser(msg.author.id);
			if (!user) {
				return msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('No Twitter Account Linked!')
						.setDescription(
							'I cannot tweet when you have no account linked! \nPlease link an account by going to https://furrycentr.al/twitter',
						)
						.setThumbnail('https://static01.nyt.com/images/2014/08/10/magazine/10wmt/10wmt-articleLarge-v4.jpg?quality=75&auto=webp&disable=upscale'),
				);
			}
		}

		const client = new Twitter({
			// eslint-disable-next-line camelcase
			consumer_key: config.twitter.key,
			// eslint-disable-next-line camelcase
			consumer_secret: config.twitter.secret,
			// eslint-disable-next-line camelcase
			access_token_key: user.token,
			// eslint-disable-next-line camelcase
			access_token_secret: user.secret,
		});

		client.post('statuses/update', { status: tweet }, function(error) {
			if (error) {
				return msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('Tweet failed')
						.setDescription(
							`error: ${error} - you may be able to report this using the -report command`,
						)
						.setThumbnail('https://static01.nyt.com/images/2014/08/10/magazine/10wmt/10wmt-articleLarge-v4.jpg?quality=75&auto=webp&disable=upscale'),
				);
			} else {
				return msg.channel.send(
					new MessageEmbed()
						.setColor(0x00ff00)
						.setTitle('New Tweet Posted!')
						.setDescription(
							`${user!.username}: ${tweet} \nPosted now`,
						)
						.setThumbnail('https://static01.nyt.com/images/2014/08/10/magazine/10wmt/10wmt-articleLarge-v4.jpg?quality=75&auto=webp&disable=upscale'),
				);
			}
		});

		return msg;
	}
}
