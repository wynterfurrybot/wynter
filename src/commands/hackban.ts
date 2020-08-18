import { MessageEmbed, Message, TextChannel } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'hackban',
			cooldown: 5,
			usage: '<user>',
		});
	}

	public async run(msg: Message, args: string[]) {
    // @ts-ignore
    if(!msg.member.hasPermission('BAN_MEMBERS'))
    {
      msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('No permissions') // @ts-ignore
					.setDescription(`You do not have permissions to ban people on ${msg.guild.name}`)
					.setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
			);
      return;
    }

    var bannedmems = 0;

    args.forEach(arg => {
      bannedmems = bannedmems +1;
      try{ // @ts-ignore
        msg.guild.members.ban(arg);
      }
      catch{
        bannedmems = bannedmems -1;
      }

    });



    var channel = msg.guild!.channels.cache.find((channel) => channel.name === 'case_logs');

      const embed = new MessageEmbed()
        // Set the title of the field
        .setTitle('Ban')
        // Set the color of the embed
        .setColor(0xff0000)
        // Set the main content of the embed
        .setDescription(// @ts-ignore
          `${msg.author} has hackbanned ${bannedmems} users`,
        );

      (channel as TextChannel).send(embed);

      msg.channel.send(
        new MessageEmbed()
          .setColor(0x00ff00)
          .setTitle('Member hackbanned')
          .setDescription(
            `Successfully hackbanned ${bannedmems} users`,
          )
          .setThumbnail(
            'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
          ),
      );
    msg.delete();
	}
}
