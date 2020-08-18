import { MessageEmbed, Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
  public constructor() {
    super({
      name: 'clear',
      cooldown: 5,
      usage: '<num>',
    });
  }

  public async run(msg: Message, args: string[]) {
    // @ts-ignore
    if(!msg.member.hasPermission('MANAGE_MESSAGES'))
    {
      msg.channel.send(
        new MessageEmbed()
        .setColor(0x00ff00)
        .setTitle('No permissions') // @ts-ignore
        .setDescription(`You do not have permissions manage messages on ${msg.guild.name}`)
        .setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
      );
      return;
    }
    var deleteCount = parseInt(args[0]);
    deleteCount = deleteCount +1;

    if(deleteCount > 100){
      deleteCount = 100;
    }

    if (!deleteCount || deleteCount < 3 || deleteCount > 100)
    return msg.reply("Please provide a number between 2 and 100 for the number of messages to delete");

    const fetched = await msg.channel.messages.fetch({
      limit: deleteCount
    })
    msg.channel.bulkDelete(fetched)
    .catch(error => msg.reply(`Couldn't delete messages because of: ${error}`));


          msg.channel.send(
            new MessageEmbed()
              .setColor(0x00ff00)
              .setTitle('Messages Deleted')
              .setDescription(
                `Successfully deleted ${deleteCount} messages`,
              )
              .setThumbnail(
                'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
              ),
          );
          return null;
  }
}
