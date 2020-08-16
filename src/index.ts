import { Invite, MessageEmbed, Collection, TextChannel } from 'discord.js';
import { readdirSync } from 'fs';

import { DanteClient } from './lib/DanteClient';
import Command, { CommandUseIn } from './lib/structures/Command';

const client = new DanteClient();
const invites: Record<string, Collection<string, Invite>> = {};
const commandFiles = readdirSync('./dist/commands').filter((file: string) => file.endsWith('.js'));
const regex = RegExp(/[^a-zA-Z\d\s:]/g);

for (const file of commandFiles) {
	const cmdFile = require(`./commands/${file}`).default;

	const command: Command = new cmdFile();

	client.commands.set(command.name, command);
}

client.on('ready', () => {
	console.log(`Logged in as ${client.user!.tag}!`);
	client.user!.setActivity(`Eating Pi | !help`);

	client.guilds!.cache.forEach((g) => {
		g.fetchInvites().then((guildInvites) => {
			invites[g.id] = guildInvites;
		});
	});
});

client.on('guildMemberRemove', (member) => {
	if (member.guild.id === '667466143585402900') {
		client.channels.fetch('667495189832794162').then((channel) => {
			(channel as TextChannel).send(member.user!.username + ' has left, they will be missed');
		});
	}
});

client.on('guildMemberAdd', (member) => {
	if (member.guild.id === '736969969404870688') {
		member.send(
			"Welcome to the elite server of european furries! \n\nJust so you know, we operate a strict no robot policy here! \n\nTo verify you're not one, please go to https://verify.furrycentr.al/ef/ and log in with discord.",
		);
	}

	if (member.guild.id === '667466143585402900') {
		client.channels.fetch('667495189832794162').then((channel) => {
			(channel as TextChannel).send('<@' + member.id + '> has joined the server!');
		});

		member.send(
			`Hello ${
				member.user!.username
			} and welcome to Cuddle Club! Please answer these small questions and post them in the initiation (<#667495506251087902>) channel within the server! \n\nName:\nAge:\nPronouns:\nTimezone:\nA little bit about yourself:\nHow you found the server:\n\nOnce you fill this out please give staff 24 hours to review and approve you`,
		);
	}

	if (
		member.guild.id === '462041783438934036' ||
		member.guild.id === '667466143585402900' ||
		member.guild.id === '736969969404870688'
	) {
		member.guild.fetchInvites().then((guildInvites) => {
			try {
				const ei = invites[member.guild.id];

				invites[member.guild.id] = guildInvites;

				const invite = guildInvites.find((i) => ei.get(i.code)!.uses! < i.uses!);

				const inviter = client.users.cache.get(invite!.inviter!.id);

				if (member.guild.id === '736969969404870688') {
					client.channels.fetch('736981136164782171').then((channel) => {
						const embed = new MessageEmbed()
							// Set the title of the field
							.setTitle('New Joiner')
							// Set the color of the embed
							.setColor(0xff0000)
							// Set the main content of the embed
							.setDescription(
								`${member.user!.username} Joined using invite code ${invite!.code} made by <@${
									invite!.inviter!.id
								}> (${inviter!.username})`,
							);

						(channel as TextChannel).send(embed);
					});
				} else if (member.guild.id === '667466143585402900') {
					client.channels.fetch('713624679671136306').then((channel) => {
						const embed = new MessageEmbed()
							// Set the title of the field
							.setTitle('New Joiner')
							// Set the color of the embed
							.setColor(0xff0000)
							// Set the main content of the embed
							.setDescription(
								`${member.user!.username} Joined using invite code ${invite!.code} made by <@${
									invite!.inviter!.id
								}> (${inviter!.username})`,
							);

						(channel as TextChannel).send(embed);
					});
				} else if (member.guild.id === '462041783438934036') {
					client.channels.fetch('539917043886063636').then((channel) => {
						const embed = new MessageEmbed()
							// Set the title of the field
							.setTitle('New Joiner')
							// Set the color of the embed
							.setColor(0xff0000)
							// Set the main content of the embed
							.setDescription(
								`${member.user!.username} Joined using invite code ${invite!.code} made by <@${
									invite!.inviter!.id
								}> (${inviter!.username})`,
							);

						(channel as TextChannel).send(embed);
					});
				}
			} catch {
				if (member.guild.id === '667466143585402900') {
					client.channels.fetch('713624679671136306').then((channel) => {
						const embed = new MessageEmbed()
							// Set the title of the field
							.setTitle('New Joiner')
							// Set the color of the embed
							.setColor(0xff0000)
							// Set the main content of the embed
							.setDescription(
								`I can't quite figure out how ${
									member.user!.username
								} joined the server. \n\nMaybe they used a temporary invite?`,
							);

						(channel as TextChannel).send(embed);
					});
				} else if (member.guild.id === '736969969404870688') {
					client.channels.fetch('736981136164782171').then((channel) => {
						const embed = new MessageEmbed()
							// Set the title of the field
							.setTitle('New Joiner')
							// Set the color of the embed
							.setColor(0xff0000)
							// Set the main content of the embed
							.setDescription(
								`I can't quite figure out how ${
									member.user!.username
								} joined the server. \n\nMaybe they used a temporary invite?`,
							);

						(channel as TextChannel).send(embed);
					});
				} else if (member.guild.id === '462041783438934036') {
					client.channels.fetch('539917043886063636').then((channel) => {
						const embed = new MessageEmbed()
							// Set the title of the field
							.setTitle('New Joiner')
							// Set the color of the embed
							.setColor(0xff0000)
							// Set the main content of the embed
							.setDescription(
								`I can't quite figure out how ${
									member.user!.username
								} joined the server. \n\nMaybe they used a temporary invite?`,
							);

						(channel as TextChannel).send(embed);
					});
				}
			}
		});
	}

	if (member.user!.username.match(regex)) {
		console.log('Username matched filter');

		try {
			console.log('Attempted change');

			if (member.guild.id === '462041783438934036') {
				client.channels.fetch('462044318421745664').then((channel) => {
					(channel as TextChannel).send(
						`<@&462043912169586699> Please check the latest name for <@${member.id}>`,
					);
				});
			} else {
				client.channels.fetch('634061513635790858').then((channel) => {
					(channel as TextChannel).send(
						`<@&634061152456015872> Please check the latest name for <@${member.id}>`,
					);
				});
			}
		} catch (err) {
			console.log(err);

			if (member.guild.id === '462041783438934036') {
				client.channels.fetch('462044318421745664').then((channel) => {
					(channel as TextChannel).send(
						`<@&462043912169586699> Please check the latest name for <@${member.id}>`,
					);
				});
			} else {
				client.channels.fetch('634061513635790858').then((channel) => {
					(channel as TextChannel).send(
						`<@&634061152456015872> Please check the latest name for <@${member.id}>`,
					);
				});
			}
			member.setNickname('Please change');
		}
	}

	if (member.guild.id != '462041783438934036') return;
	member.send(
		"Welcome to The Floof Hotel! \n\nJust so you know, we operate a strict no robot policy here! \n\nTo verify you're not one, please go to https://verify.furrycentr.al/ and log in with discord.",
	);
});

client.on('guildMemberUpdate', (oldMem, newMem) => {
	if (regex.test(newMem.user!.username) && oldMem.user!.username != newMem.user!.username) {
		console.log('Username matched filter');
		try {
			console.log('Attempted change');
			if (newMem.guild.id === '462041783438934036') {
				client.channels.fetch('462044318421745664').then((channel) => {
					(channel as TextChannel).send(
						`<@&462043912169586699> Please check the latest name for <@${newMem.id}>`,
					);
				});
			} else {
				client.channels.fetch('634061513635790858').then((channel) => {
					(channel as TextChannel).send(
						`<@&634061152456015872> Please check the latest name for <@${newMem.id}>`,
					);
				});
			}
		} catch (err) {
			console.log(err);
			if (newMem.guild.id === '462041783438934036') {
				client.channels.fetch('462044318421745664').then((channel) => {
					(channel as TextChannel).send(
						'<@&462043912169586699> Please check the latest name for <@' + newMem.id + '>',
					);
				});
			} else {
				client.channels.fetch('634061513635790858').then((channel) => {
					(channel as TextChannel).send(
						`<@&634061152456015872> Please check the latest name for <@${newMem.id}>`,
					);
				});
			}

			newMem.setNickname('Please change');
		}
	}

	if (regex.test(newMem.nickname!) && oldMem.nickname != newMem.nickname) {
		console.log('Username matched filter');
		try {
			console.log('Attempted change');
			if (newMem.guild.id === '462041783438934036') {
				client.channels.fetch('462044318421745664').then((channel) => {
					(channel as TextChannel).send(
						`<@&462043912169586699> Please check the latest name for <@${newMem.id}>`,
					);
				});
			} else {
				client.channels.fetch('634061513635790858').then((channel) => {
					(channel as TextChannel).send(
						`<@&634061152456015872> Please check the latest name for <@${newMem.id}>`,
					);
				});
			}
		} catch (err) {
			console.log(err);
			if (newMem.guild.id === '462041783438934036') {
				client.channels.fetch('462044318421745664').then((channel) => {
					(channel as TextChannel).send(
						`<@&462043912169586699> Please check the latest name for <@${newMem.id}>`,
					);
				});
			} else {
				client.channels.fetch('634061513635790858').then((channel) => {
					(channel as TextChannel).send(
						`<@&634061152456015872> Please check the latest name for <@${newMem.id}>`,
					);
				});
			}

			newMem.setNickname('Please change');
		}
	}

	let hasMember = false;

	oldMem.roles.cache.forEach((role) => {
		if (
			role.id === '462042250612965386' ||
			role.id === '725462565852938301' ||
			role.id === '667472170926080011' ||
			role.id === '736971909362614362'
		) {
			hasMember = true;
		}
	});

	newMem.roles.cache.forEach((role) => {
		if (role.id === '736971909362614362' && hasMember === false) {
			client.channels.fetch('736979363362373642').then((channel) => {
				(channel as TextChannel).send('<a:wel:742119488366837780><a:come:742119500068946084>');
				(channel as TextChannel).send(
					`Welcome <@${newMem.id}> to the most elite group of european furs!\n\nI hope you enjoy your stay here, and here's a free cookie to welcome you! :cookie:`,
				);
			});
		} else if (role.id === '725462565852938301' && hasMember === false) {
			client.channels.fetch('725476791858495508').then((channel) => {
				(channel as TextChannel).send('<a:wel:742119488366837780><a:come:742119500068946084>');
				(channel as TextChannel).send(
					`Welcome <@${newMem.id}> to the coolest club around! Club Floof! \n\nFeel free to go ahead and grab some roles in <#742103877582848173>!\n\nI hope you enjoy your stay here, and here's a free cookie to welcome you! :cookie: \n\n<@&736666911189893170> Please welcome the above user!`,
				);
			});
		} else if (role.id === '462042250612965386' && hasMember === false) {
			client.channels.fetch('629056060803645453').then((channel) => {
				(channel as TextChannel).send('<a:wel:742119488366837780><a:come:742119500068946084>');
				(channel as TextChannel).send(
					`<@${newMem.id}>, Welcome, welcome! We hope you enjoy your stay at The Floof Hotel!  *hands room card* \n\nYour room number is ' +
							Math.floor(Math.random() * 5670) +
							'\n\nOn the desk is a free :cookie:, should you need us at any point, feel free to ping a member of staff! Should you have any feedback about anything, feel free to visit <#681616342733815825>! \n\nFeel free to tell us about you and your fursona in <#552957610899275776> \n\n<@&463088144292511764> Please welcome the above user!`,
				);
			});
		} else if (role.id === '667472170926080011' && hasMember === false) {
			client.channels.fetch('667466143585402903').then((channel) => {
				(channel as TextChannel).send('<a:wel:742119488366837780><a:come:742119500068946084>');
				(channel as TextChannel).send(
					`Welcome <@${newMem.id}> to cuddle club! \n\nPlease accept a free cookie, on me! :cookie:`,
				);
			});
		}
	});
});

client.on('messageUpdate', (msg, newMsg) => {
	if (newMsg.content!.includes('dark') && newMsg.content!.includes('cute')) {
		newMsg.channel.send('Dark is the cutest person in the world!');
	}

	if (
		msg.channel.id === '717430439396245577' ||
		msg.channel.id === '721808001098448896' ||
		msg.channel.id === '717858360430428160'
	) {
		// On receive message, (Given string `msg`) from channel #awoo
		if (!/^(\*|_)*awo+f?(!|\*|_)*( ?(:3|<3|owo|uwu))?( ?❤️)?(\*|_)*$/iu.test(newMsg.content!)) {
			newMsg.delete();
			newMsg.author!.send(`I see you.. No ${msg.content} only awoo!`);
		}
	}

	if (newMsg.author!.bot) {
		return;
	}

	if (newMsg.attachments) {
		var a = newMsg.attachments;
		a.forEach(function (b) {
			newMsg.content = newMsg.content + ' -- ' + b.url;
		});
	}
	try {
		var channel = newMsg.guild!.channels.cache.find((channel) => channel.name === 'message_logs');
		(channel as TextChannel).send({
			embed: {
				color: 3447003,
				description: `A message sent by ${newMsg.author!.username} was edited!\n\nOld message:\n${
					msg.content
				}\nNew message:\n${newMsg.content}\n\nChannel: <#${newMsg.channel.id}>`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.on('message', async (msg) => {
	const prefix = '!';
	const cooldownBypass = ['512608629992456192', '370535760757260289'];

	if (msg.content!.includes('dark') && msg.content!.includes('cute')) {
		msg.channel.send('Dark is the cutest person in the world!');
	}

	if (msg.channel.id === '462044347794456605' && msg.author.id === '155149108183695360') {
		msg.channel.send('<@&462043912169586699> Please check the latest dyno case log.');
	}

	if (msg.author.bot === true) return;

	if (msg.channel.id === '629075452723462154') {
		// Repost advertisement!
		msg.delete();

		client.channels
			.fetch('629073904882810910')
			.then((channel) =>
				(channel as TextChannel).send(`OP: <@${msg.author.id}>\n\n${msg.content}`),
			);

		msg.channel.send(
			`<@${msg.author.id}>, I've reposted your advertisement to <#629073904882810910> - it shall be displayed for 3 days.\n\n<@&462043912169586699>`,
		);
	}

	if (
		msg.channel.id === '717430439396245577' ||
		msg.channel.id === '721808001098448896' ||
		msg.channel.id === '717858360430428160'
	) {
		// On receive message, (Given string `msg`) from channel #awoo
		if (!/^(\*|_)*awo+f?(!|\*|_)*( ?(:3|<3|owo|uwu))?( ?❤️)?(\*|_)*$/iu.test(msg.content)) {
			msg.delete();
			msg.author.send(`No ${msg.content}, only awoo!`);
		}
	}

	if (!msg.content.startsWith(prefix) || msg.author.bot) return;

	const args = msg.content.slice(prefix.length).trim().split(/ +/);
	const commandName = args.shift()!.toLowerCase();

	if (!client.commands.has(commandName)) return;

	const command =
		client.commands.get(commandName) ||
		client.commands.find((cmd) => cmd.aliases && cmd.aliases.includes(commandName));

	if (!command) return;

	if (!cooldownBypass.includes(msg.author.id)) {
		if (!client.commandCooldowns.has(command!.name)) {
			client.commandCooldowns!.set(command!.name, new Collection());
		}

		const now = Date.now();
		const timestamps = client.commandCooldowns.get(command!.name);
		const cooldownAmount = command!.cooldown * 1000;

		if (timestamps!.has(msg.author.id)) {
			const expirationTime = timestamps!.get(msg.author.id)! + cooldownAmount;

			if (now < expirationTime) {
				const timeLeft = (expirationTime - now) / 1000;
				return msg.reply(
					`please wait ${timeLeft.toFixed(1)} more second(s) before reusing the \`${
						command!.name
					}\` command.`,
				);
			}
		}

		timestamps!.set(msg.author.id, now);
		setTimeout(() => timestamps!.delete(msg.author.id), cooldownAmount);
	}

	try {
		if (command!.useIn === CommandUseIn.guild && msg.channel.type !== 'text') {
			await msg.reply('you can only run this command in server text channels!');
		} else if (command!.useIn === CommandUseIn.dm && msg.channel.type !== 'dm') {
			await msg.reply('you can only run this command in DMs!');
		} else {
			await command!.run(msg, args);
		}
	} catch (error) {
		console.error(error);
		await msg.reply('there was an error trying to execute that command!');
	}

	return;
});

client.on('messageDelete', (messageDelete) => {
	if (messageDelete.author!.bot) {
		return;
	}

	if (messageDelete.attachments) {
		var a = messageDelete.attachments;
		a.forEach(function (b) {
			messageDelete.content = messageDelete.content + ' -- ' + b.url;
		});
	}

	try {
		// send to local message channel
		var channel = messageDelete.guild!.channels.cache.find(
			(channel) => channel.name === 'message_logs',
		);

		(channel as TextChannel).send({
			embed: {
				color: 16726088,
				description: `A message sent by ${
					messageDelete.author!.username
				} was removed!\n\nContent:\n${messageDelete.content}\n\nChannel: <#${
					messageDelete.channel.id
				}>`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.on('channelCreate', (channel) => {
	try {
		var c = (channel as TextChannel).guild.channels.cache.find((c) => c.name === 'channel_logging');
		(c as TextChannel).send({
			embed: {
				color: 3447003,
				description: `A new channel (${(channel as TextChannel).name}) was created!`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.on('channelDelete', (channel) => {
	try {
		var c = (channel as TextChannel).guild.channels.cache.find((c) => c.name === 'channel_logging');
		(c as TextChannel).send({
			embed: {
				color: 16726088,
				description: `Channel (${(channel as TextChannel).name}) was deleted!`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.on('guildMemberAdd', (member) => {
	try {
		var channel = member.guild.channels.cache.find((channel) => channel.name === 'user_logs');
		(channel as TextChannel).send({
			embed: {
				color: 3447003,
				description: `A new member (${member.user!.username}) has joined!`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.on('guildMemberRemove', (member) => {
	try {
		var channel = member.guild.channels.cache.find((channel) => channel.name === 'user_logs');
		(channel as TextChannel).send({
			embed: {
				color: 16726088,
				description: `Member <@${member.id}> (${member.user!.username}) has left!`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.on('guildBanAdd', (guild, member) => {
	try {
		var channel = guild.channels.cache.find((channel) => channel.name === 'case_logs');
		(channel as TextChannel).send({
			embed: {
				color: 16726088,
				description: `Member <@${member.id}> (${member!.username}) has been banned!`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.on('guildBanRemove', (guild, member) => {
	try {
		var channel = guild.channels.cache.find((channel) => channel.name === 'user_logs');
		(channel as TextChannel).send({
			embed: {
				color: 16726088,
				description: `Member <@${member.id}> ban revoked`,
			},
		});

		var channel = guild.channels.cache.find((channel) => channel.name === 'case_logs');
		(channel as TextChannel).send({
			embed: {
				color: 16726088,
				description: `Member <@${member.id}> ban revoked`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.login('NTEzMjkyMzg1ODE2Njc0MzIw.Xf0k6A.YrhY22ZuUz6htdYC9JOcWyz2c0k');
