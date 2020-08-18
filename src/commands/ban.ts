import { MessageEmbed, Message, TextChannel } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'ban',
			cooldown: 5,
			usage: '<toggle>',
		});
	}

	public async run(msg: Message) {
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
    // @ts-ignore
    var member = msg.mentions.members.first();
    //@ts-ignore
    if(!member.bannable){
      msg.channel.send(
        new MessageEmbed()
          .setColor(0x00ff00)
          .setTitle('Error')
          .setDescription(
            `The member mentioned cannot be banned from the server. \n\nMaybe they have a higher role than me?`,
          )
          .setThumbnail(
            'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
          ),
      );
      return;
    }
    // @ts-ignore
    await member.send(new MessageEmbed()
      .setColor(0x00ff00)
      .setTitle('KICK:')
      .setDescription(//@ts-ignore
        `You have been banned on ${msg.guild.name}. The reasoning can be found below: \n\n${msg.content}`,
      )
      .setThumbnail(
        'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
      ),
    );
    // @ts-ignore
    member.ban();

    var channel = msg.guild!.channels.cache.find((channel) => channel.name === 'case_logs');

      const embed = new MessageEmbed()
        // Set the title of the field
        .setTitle('Ban')
        // Set the color of the embed
        .setColor(0xff0000)
        // Set the main content of the embed
        .setDescription(// @ts-ignore
          `${msg.author} has banned ${msg.mentions.users.first()} (${msg.mentions.users.first().username}#${msg.mentions.users.first().discriminator}) for the following reason: \n\n${msg.content}`,
        );

      (channel as TextChannel).send(embed);

      msg.channel.send(
        new MessageEmbed()
          .setColor(0x00ff00)
          .setTitle('Member Banned')
          .setDescription(
            `Successfully banned a user`,
          )
          .setThumbnail(
            'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
          ),
      );
    msg.delete();
	}
}
