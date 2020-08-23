import { MessageEmbed, Message } from 'discord.js';
import { Guilds } from '../lib/Models/guild';

import Command from '../lib/structures/Command';
import updateGuild from '../lib/DatabaseWrapper/UpdateGuild';

export default class extends Command {
	public constructor() {
		super({
			name: 'swearfilter',
			cooldown: 5,
			usage: '<toggle>',
		});
	}

	public async run(msg: Message, args: string[]): Promise<Message> {
		if (!msg.member!.hasPermission('ADMINISTRATOR')) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('No permissions')
					.setDescription('You do not have permissions to toggle the swearfilter')
					.setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
			);
		}

		if (args.includes('on')) {
			const guildDB = new Guilds();
			guildDB.blacklistedWords = [
				'fuck',
				'shit',
				'cunt',
				'bastard',
				'bitch',
				'prick',
				'nigga',
				'nigger',
				'nignog',
				'n1gga',
				'n1gger',
				'nugger',
				'slut',
				'twat',
				'wanker',
				'faggot',
				'fag',
				'whore',
				'dickhead',
				'nibba',
				'f-u-c-k',
				'f-uck',
				's-hit',
				'frick',
				'sh1t',
				'b1tch',
				'ni:b::b:a',
				'fück',
				'dick',
				'fruck',
				'niggggggaaaaaa',
				'cock',
				'cocksucker',
				'pussy',
				'nibber',
				'niqqer',
			];

			updateGuild(msg.guild!.id, guildDB);
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Fuck!')
					.setDescription('Swearfilter has been enabled')
					.setThumbnail(
						'https://p.kindpng.com/picc/s/81-816452_censor-bars-messages-sticker-0-censor-bar-transparent.png',
					),
			);
		} else if (args.includes('off')) {
			const guildDB = new Guilds();
			guildDB.blacklistedWords = ['none'];
			updateGuild(msg.guild!.id, guildDB);
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('You may now.. kiss my ass!')
					.setDescription('Swearfilter has been disabled')
					.setThumbnail(
						'https://p.kindpng.com/picc/s/81-816452_censor-bars-messages-sticker-0-censor-bar-transparent.png',
					),
			);
		}

		return msg;
	}
}
