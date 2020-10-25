import { Message, MessageEmbed, TextChannel } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	public constructor() {
		super({
			name: 'clear',
			cooldown: 5,
			usage: '<num>',
			aliases: ['clean', 'purge'],
		});
	}

	public async run(msg: Message, args: string[]): Promise<Message> {
		if (!msg.member!.hasPermission('MANAGE_MESSAGES')) {
			return msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('No permissions')
					.setDescription(`You do not have permissions manage messages on ${msg.guild!.name}`)
					.setThumbnail('https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png'),
			);
		}

		await msg.delete();

		let deleteCount = parseInt(args[0]);

		if (!deleteCount || deleteCount < 1 || deleteCount >= 100) {
			return msg.reply(
				'Please provide a number between 2 and 100 for the number of messages to delete',
			);
		}

		try {
			const pinnedMessages: Message[] = [];

			const fetchedMessages = await msg.channel.messages.fetch({
				limit: deleteCount,
			});

			// Ensure message is not pinned
			fetchedMessages.forEach((msg) => {
				if (msg.pinned) {
					pinnedMessages.push(msg);
					deleteCount--;
				}
			});

			// Iterate through pinned messages and remove it from the fetched messages
			if (pinnedMessages.length !== 0) {
				pinnedMessages.forEach((val) => {
					fetchedMessages.delete(val.id);
				});
			}

			const deletedMsgs = await (msg.channel as TextChannel).bulkDelete(fetchedMessages);

			const deleteSuccessMsg = await msg.channel.send(
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle('Messages Deleted')
					.setDescription(`Successfully deleted ${deletedMsgs.size} messages`)
					.setThumbnail(
						'https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg',
					),
			);

			setTimeout(async () => {
				await deleteSuccessMsg.delete();
			}, 5000);

			return msg;
		} catch (err) {
			return msg.reply(`Couldn't delete messages because of: ${err}`);
		}
	}
}
