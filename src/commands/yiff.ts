import { MessageEmbed } from 'discord.js';
import { Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	constructor() {
		super({
			name: 'yiff',
      aliases:['fuck'],
			cooldown: 5,
			usage: '<member>',
		});
	}
	public async run(msg: Message) {
    // @ts-ignore
    if(msg.channel.nsfw === false){
      msg.channel.send(
  			new MessageEmbed()
  				.setColor(0x00ff00)
  				.setTitle('Not A NSFW Channel')
  				.setDescription(
  					`The channel you just ran the command in is not NSFW!`,
  				)
  				.setThumbnail(
  					'https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png',
  				),
  		);
    }
		msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Yiff!')
				.setDescription(
					`${msg.author} has yiffed ${msg.mentions.users.first()} hard!`,
				)
				.setThumbnail(
					'https://ci.phncdn.com/videos/201812/04/195030881/original/(m=eaAaGwObaaaa)(mh=0KDlKJW31QShbuqU)14.jpg',
				),
		);
	}
}
