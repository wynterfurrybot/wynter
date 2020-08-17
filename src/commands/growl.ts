import { MessageEmbed } from 'discord.js';
import { Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
  constructor() {
    super({
      name: 'growl',
      cooldown: 5,
      usage: '',
    });
  }
  public async run(msg: Message) {

    if(msg.mentions.users.array() === undefined || msg.mentions.users.array().length == 0){
      msg.channel.send(
        new MessageEmbed()
        .setColor(0x00ff00)
        .setTitle('A light growl was heard!')
        .setDescription(
          `${msg.author} has let out a light growl!`,
        )
        .setThumbnail(
          'https://pm1.narvii.com/6219/8faceb03db01e5c8e64b87dc8fa6d3e18a08011e_hq.jpg',
        ),
      );
    }
  else{
    msg.channel.send(
      new MessageEmbed()
      .setColor(0x00ff00)
      .setTitle('A light growl was heard!')
      .setDescription(
        `${msg.author} growls at ${msg.mentions.users.first()}!`,
      )
      .setThumbnail(
        'https://pm1.narvii.com/6219/8faceb03db01e5c8e64b87dc8fa6d3e18a08011e_hq.jpgg',
      ),
    );
  }

  }
}
