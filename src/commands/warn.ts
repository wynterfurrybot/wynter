import { MessageEmbed, Message, TextChannel } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'warn',
			cooldown: 5,
			usage: '<toggle>',
		});
	}

	public async run(msg: Message) {
    // @ts-ignore
    if(!msg.member.hasPermission('KICK_MEMBERS'))
    {
      msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('No permissions') // @ts-ignore
					.setDescription(`You do not have permissions to kick people on ${msg.guild.name} - thus you cannot warn this user.`)
					.setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
			);
      return;
    }
    // @ts-ignore
    var member = msg.mentions.members.first();
    // @ts-ignore
    member.send(new MessageEmbed()
      .setColor(0x00ff00)
      .setTitle('WARNING:')
      .setDescription(//@ts-ignore
        `You have been warned on ${msg.guild.name}. The reasoning can be found below: \n\n${msg.content}`,
      )
      .setThumbnail(
        'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
      ),
    );

    var channel = msg.guild!.channels.cache.find((channel) => channel.name === 'case_logs');

      const embed = new MessageEmbed()
        // Set the title of the field
        .setTitle('Warn')
        // Set the color of the embed
        .setColor(0xff0000)
        // Set the main content of the embed
        .setDescription(// @ts-ignore
          `${msg.author} has warned ${msg.mentions.users.first()} (${msg.mentions.users.first().username}#${msg.mentions.users.first().discriminator}) for the following reason: \n\n${msg.content}`,
        );

      (channel as TextChannel).send(embed);

      msg.channel.send(
        new MessageEmbed()
          .setColor(0x00ff00)
          .setTitle('Member Warned')
          .setDescription(
            `Successfully warned a user`,
          )
          .setThumbnail(
            'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
          ),
      );
    msg.delete();
	}
}
