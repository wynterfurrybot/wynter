import { Message, MessageEmbed } from 'discord.js';

import Command from '../lib/structures/Command';
import FindUser from '../lib/DatabaseWrapper/Twitter/FindTwitter';
import Twitter from 'twitter';

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

        if(tweet.length > 280){
            return msg.channel.send(
                new MessageEmbed()
                    .setColor(0x00ff00)
                    .setTitle('Tweet failed')
                    .setDescription(
                        `error: too many characters`,
                    )
                    .setThumbnail('https://static01.nyt.com/images/2014/08/10/magazine/10wmt/10wmt-articleLarge-v4.jpg?quality=75&auto=webp&disable=upscale'),
            );
        }
        
        const user = await FindUser(msg.author.id);
        if (!user){
            return msg.channel.send(
                new MessageEmbed()
                    .setColor(0x00ff00)
                    .setTitle('No Twitter Account Linked!')
                    .setDescription(
                        'I cannot tweet when you have no account linked!',
                    )
                    .setThumbnail('https://static01.nyt.com/images/2014/08/10/magazine/10wmt/10wmt-articleLarge-v4.jpg?quality=75&auto=webp&disable=upscale'),
            ); 
        }

        var client = new Twitter({
            consumer_key: 'xPWq1OE6AcEH7tZhnWqHenEwD',
            consumer_secret: 'l3rFsIA5HDqr2uOtRcrYm8tfOVhsE6rl0UiVhuZr0I0gPxsi54',
            access_token_key: user.token,
            access_token_secret: user.secret
          });

          client.post('statuses/update', {status: tweet},  function(error) {
            if(error){
                return msg.channel.send(
                    new MessageEmbed()
                        .setColor(0x00ff00)
                        .setTitle('Tweet failed')
                        .setDescription(
                            `error: ${error} - you may be able to report this using the -report command`,
                        )
                        .setThumbnail('https://static01.nyt.com/images/2014/08/10/magazine/10wmt/10wmt-articleLarge-v4.jpg?quality=75&auto=webp&disable=upscale'),
                );
            }
            else{
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
