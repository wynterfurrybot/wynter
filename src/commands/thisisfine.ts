import { Message } from 'discord.js';
import config from '../../config.json';
import axios from 'axios';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'thisisfine',
			cooldown: 5,
			usage: '[meme]',
		});
    }


	public async run(msg: Message, args: string[]): Promise<Message> {
        let username = config.imgflip.username;
        let password = config.imgflip.password;

        let meme = '';
		args.forEach((arg) => {
			meme = meme + ' ' + arg;
		});

        axios
			.get('https://api.imgflip.com/caption_image?text0=' + meme + '&username=' + username +'&password=' + password +'&template_id=55311130')
			.then(function(response) {
                console.log(response.data.data.url);
                return msg.channel.send(response.data.data.url);
            })
            .catch(function(error) {
                return msg.channel.send(`An error occured, see below: ${error}`)
            })
            return msg;
    }
}