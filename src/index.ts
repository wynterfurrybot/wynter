import 'reflect-metadata';

import { Collection, Invite, MessageEmbed, TextChannel } from 'discord.js';
import { readdirSync } from 'fs';
import { createConnection } from 'typeorm';

import { db, token } from '../config.json';

import { DanteClient } from './lib/DanteClient';

import Command, { CommandUseIn } from './lib/structures/Command';

import { Guilds } from './lib/Models/Guilds';
import { BlacklistedWords } from './lib/Models/BlacklistedWords';
import { BypassChannels } from './lib/Models/BypassChannels';
import { Twitter } from './lib/Models/Twitter';
import { Punishments } from './lib/Models/Punishments';

import deleteGuild from './lib/DatabaseWrapper/DeleteGuild';
import addGuild from './lib/DatabaseWrapper/AddGuild';
import getGuild from './lib/DatabaseWrapper/FindGuild';
import FindGuild from './lib/DatabaseWrapper/FindGuild';

const client = new DanteClient({
	ws: {
		intents: 32509,
	},
});
const invites: Record<string, Collection<string, Invite>> = {};
const commandFiles = readdirSync('./dist/src/commands').filter((file: string) =>
	file.endsWith('.js'),
);
const regex = RegExp(/[^a-zA-Z\d\s:]/g);

/*Function getGuildsFromUser(user: UserResolvable, client: DanteClient) {
	return client.guilds.cache.filter((guild) => {
		console.log('getGuildFromUser: ' + guild.name + ', ' + guild.member(user));
		return guild.member(user) !== null;
	});
}*/

for (const file of commandFiles) {
	// eslint-disable-next-line @typescript-eslint/no-var-requires
	const cmdFile = require(`./commands/${file}`)['default'];

	const command: Command = new cmdFile();

	client.commands.set(command.name, command);
}

client.on('ready', async () => {
	console.log(`Logged in as ${client.user!.tag}!`);
	await client.user!.setActivity('Eating Pi | !help');

	client.guilds!.cache.forEach((g) => {
		g.fetchInvites().then((guildInvites) => {
			invites[g.id] = guildInvites;
		});
	});

	await createConnection({
		type: 'mysql',
		...db,
		database: 'wynter',
		// eslint-disable-next-line array-element-newline
		entities: [Guilds, BlacklistedWords, BypassChannels, Twitter, Punishments],
		logging: true,
		synchronize: true,
	});

	client.guilds.cache.forEach(async (guild) => {
		const findGuild = await FindGuild(guild.id);
		if (!findGuild) {
			const guildDB = new Guilds();

			guildDB.id = guild.id;
			guildDB.name = guild.name;
			guildDB.prefix = '!';
			guildDB.deleteInvLinks = false;
			guildDB.enableFAndXs = false;

			await addGuild(guildDB);
		}
	});
});

client.on('guildCreate', async (guild) => {
	await guild.owner!.send(
		'Thanks for adding Wynter to your guild! \n\nThe default prefix is `!` - Our documentation can be found at https://docs.furrycentr.al/ \n\nWe hope you have fun using Wynter!',
	);

	const guildDB = new Guilds();

	guildDB.id = guild.id;
	guildDB.name = guild.name;
	guildDB.prefix = '!';
	guildDB.deleteInvLinks = false;
	guildDB.enableFAndXs = false;

	await addGuild(guildDB);
});

client.on('guildDelete', async (guild) => {
	// Remove guild from database

	await deleteGuild(guild.id);
});

client.on('guildMemberRemove', (member) => {
	if (member.guild.id === '667466143585402900') {
		client.channels.fetch('667495189832794162').then((channel) => {
			(channel as TextChannel).send(member.user!.username + ' has left, they will be missed');
		});
	}
});

/* THIS SHIT IS HORRIBLY BROKEN RIGHT NOW, FOR THE LOVE OF GOD DO NOT USE IT. YOU WILL GET A HEADACHE AND PROBABLY BE ADMITTED
TO A MENTAL HEALTH WARD DUE TO INSANITY.

Client.on('userUpdate', (oldmember, newmember) => {
	try {
		const guilds = getGuildsFromUser(oldmember, client);
		x.log(guilds);

		guilds.forEach((g: { id: any }) => {
			x.database.query('SELECT * FROM guilds WHERE guild_id = ?', [g.id], function (
				err: { toString: () => { (): any; new (): any; red: any } },
				result: { userlogs: any }[],
				fields: any,
			) {
				if (err)
					x.log('ERROR: '.gray + ' Could not select from database '.red + err.toString().red);

				if (x.logging) x.log(' User Updated: '.cyan + oldmember.displayName);

				const embed = new Discord.MessageEmbed()
					.setTitle('Member Updated Details')
					.setAuthor('Dantè', 'https://i.imgur.com/FUUg9dM.png')
					/*
					 * Alternatively, use "#00AE86", [0, 174, 134] or an integer number.

					.setColor('#00FFFF')
					.setFooter(
						'User updated profile | ' +
							newmember.username +
							'#' +
							newmember.discriminator +
							' | Dantè Debugging Beta',
					)
					.setTimestamp();

				if (oldmember.username != newmember.username) {
					embed.setDescription(
						'Username changed: \nDetails: \n\nOld name: ' +
							oldmember.username +
							'\nNew name: ' +
							newmember.username,
					);
					try {
						x.client.channels
							.fetch(result[0].userlogs)
							.then(function (channel: { send: (arg0: { embed: any }) => void }) {
								channel.send({ embed });
							});
					} catch (err) {
						return;
					}
				}

				if (oldmember.avatarURL != newmember.avatarURL) {
					embed.setDescription('User updated their profile picture');
					embed.setThumbnail(oldmember.avatarURL);
					embed.setImage(newmember.avatarURL);
					try {
						if (newmember.bot) return;
						x.client.channels
							.fetch(result[0].userlogs)
							.then(function (channel: { send: (arg0: { embed: any }) => void }) {
								channel.send({ embed });
							});
					} catch (err) {
						x.log(err);
						return;
					}
				}
			});
		});
	} catch (err) {
		x.log('ERROR: ' + err);
	}
});*/

client.on('guildMemberAdd', (member) => {
	if (member.guild.id === '736969969404870688') {
		member.send(
			'Welcome to the elite server of european furries! \n\nJust so you know, we operate a strict no robot policy here! \n\nTo verify you\'re not one, please go to https://verify.furrycentr.al/ef/ and log in with discord.',
		);
	}

	if (member.guild.id === '754816860133916822') {
		client.channels.fetch('754817827789078658').then((channel) => {
			(channel as TextChannel).send(
				'Welcome <@' +
				member.id +
				'> to Fluff Paradise! Please type `-register` in chat to get started!',
			);
		});
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
		member.guild.id === '736969969404870688' ||
		member.guild.id === '725201209358549012'
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
				} else if (member.guild.id === '725201209358549012') {
					client.channels.fetch('763831343956099082').then((channel) => {
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
				} else if (member.guild.id === '754816860133916822') {
					client.channels.fetch('755115857222566028').then((channel) => {
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
				} else if (member.guild.id === '725201209358549012') {
					client.channels.fetch('763831343956099082').then((channel) => {
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
				} else if (member.guild.id === '754816860133916822') {
					client.channels.fetch('755115857222566028').then((channel) => {
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

	if (member.guild.id !== '462041783438934036') return;
	member.send(
		'Welcome to The Floof Hotel! \n\nJust so you know, we operate a strict no robot policy here! \n\nTo verify you\'re not one, please go to https://verify.furrycentr.al/ and log in with discord.',
	);
});

client.on('guildMemberUpdate', (oldMem, newMem) => {
	if (regex.test(newMem.user!.username) && oldMem.user!.username !== newMem.user!.username) {
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

	if (regex.test(newMem.nickname!) && oldMem.nickname !== newMem.nickname) {
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
			role.id === '736971909362614362' ||
			role.id === '754820807896596520'
		)
			hasMember = true;
	});

	newMem.roles.cache.forEach((role) => {
		if (role.id === '736971909362614362' && !hasMember) {
			client.channels.fetch('736979363362373642').then((channel) => {
				(channel as TextChannel).send('<a:wel:742119488366837780><a:come:742119500068946084>');
				(channel as TextChannel).send(
					`Welcome <@${newMem.id}> to the most elite group of european furs!\n\nI hope you enjoy your stay here, and here's a free cookie to welcome you! :cookie:`,
				);
			});
		} else if (role.id === '754820807896596520' && !hasMember) {
			client.channels.fetch('754816860133916825').then((channel) => {
				(channel as TextChannel).send('<a:wel:742119488366837780><a:come:742119500068946084>');
				(channel as TextChannel).send(
					`Welcome <@${newMem.id}>  to Paradise! We hope you will enjoy your stay. \n\nNon-alcoholic cocktails are on the house and provided on the table is a free cookie, just for you! \n\nHave fun! \n\nPS: I'd reccomend getting some roles in <#756597666011676742> if you haven't already! \n<@&755152376700076032>`,
				);
			});
		} else if (role.id === '462042250612965386' && !hasMember) {
			client.channels.fetch('629056060803645453').then((channel) => {
				(channel as TextChannel).send('<a:wel:742119488366837780><a:come:742119500068946084>');
				(channel as TextChannel).send(
					`<@${
						newMem.id
					}>, Welcome, welcome! We hope you enjoy your stay at The Floof Hotel!  *hands room card* \n\nYour room number is ${Math.floor(
						Math.random() * 5670,
					)} \n\nOn the desk is a free :cookie:, should you need us at any point, feel free to ping a member of staff! Should you have any feedback about anything, feel free to visit <#681616342733815825>! \n\nFeel free to tell us about you and your fursona in <#552957610899275776> \n\n<@&463088144292511764> Please welcome the above user!`,
				);
			});
		} else if (role.id === '667472170926080011' && !hasMember) {
			client.channels.fetch('667466143585402903').then((channel) => {
				(channel as TextChannel).send('<a:wel:742119488366837780><a:come:742119500068946084>');
				(channel as TextChannel).send(
					`Welcome <@${newMem.id}> to cuddle club! \n\nPlease accept a free cookie, on me! :cookie:`,
				);
			});
		}
	});
});

client.on('messageUpdate', async (msg, newMsg) => {
	if (
		msg.channel.id === '717430439396245577' ||
		msg.channel.id === '721808001098448896' ||
		msg.channel.id === '717858360430428160'
	) {
		// On receive message, (Given string `msg`) from channel #awoo
		if (!/^(\*|_)*awo+f?(!|\*|_)*( ?(:3|<3|owo|uwu))?( ?❤️)?(\*|_)*$/iu.test(newMsg.content!)) {
			await newMsg.delete();
			await newMsg.author!.send(`I see you.. No ${msg.content} only awoo!`);
		}
	}
	let staff = false;
	if (msg.guild!.id === '725201209358549012') {
		msg.member!.roles.cache.forEach((val) => {
			if (val.id === '739727880799518741') staff = true;
		});
		// eslint-disable-next-line @typescript-eslint/ban-ts-comment
		//@ts-ignore
		if (newMsg.content.includes('http') && !staff && !newMsg.content?.includes('tenor.com')) {
			await newMsg.delete();
			await newMsg.channel.send(
				'please do not post links here! \n\nIf you\'re looking to partner, please check <#763159239605747712>',
			);
		}
	}

	if (newMsg.author!.bot) return;

	if (newMsg.attachments) {
		const a = newMsg.attachments;
		a.forEach(function(b) {
			newMsg.content = newMsg.content + ' -- ' + b.url;
		});
	}
	try {
		const channel = newMsg.guild!.channels.cache.find((channel) => channel.name === 'message_logs');
		await (channel as TextChannel).send({
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
	// Premium users (Dark, Relms, smash, spacemonkey)
	const cooldownBypass = [
		'512608629992456192',
		'370535760757260289',
		'458812875927060480',
		'720125224695103548',
	];

	let staff = false;

	if (msg.content === '-rebuild') {
		if (msg.author.id === '512608629992456192' || msg.author.id === '370535760757260289') {
			const guilds = client.guilds.cache;
			let guildsin = 0;
			guilds.forEach(async (guild) => {
				guildsin++;

				const guildDB = new Guilds();

				guildDB.id = guild.id;
				guildDB.name = guild.name;
				guildDB.prefix = '!';
				guildDB.deleteInvLinks = false;
				guildDB.enableFAndXs = false;

				await addGuild(guildDB);
			});

			msg.channel.send(`${msg.author}, I have added ${guildsin} guilds to the database.`);
		} else {
			msg.channel.send(`${msg.author}, you have no permission to rebuild guilds`);
		}
	}

	if (msg.content.startsWith('-report')) {
		client.channels.fetch('767155058344460298').then((channel) => {
			(channel as TextChannel).send(
				'@here',
				new MessageEmbed()
					.setColor(0x00ff00)
					.setTitle(`Bug report from ${msg.author.username} | ${msg.author.id}`)
					.setDescription(msg.content)
					.setFooter(
						`Server ID: ${msg.guild?.id} | ${msg.guild?.name} | Sent from channel: ${msg.channel.id}`,
					),
			);
		});
		msg.channel.send('report sent!');
	}

	// Swear filter
	const guild = await getGuild(msg.guild!.id);

	if (guild!.blacklistedWords && guild!.blacklistedWords.length !== 0) {
		guild!.blacklistedWords.forEach((word) => {
			if (
				!guild!.bypassChannels ||
				!guild!.bypassChannels.find((chan) => chan.channelid === msg.channel.id)
			)
				if (msg.content.toLowerCase().includes(word.word)) msg.delete();
		});
	}

	if (guild?.enableFAndXs) {
		if (msg.content.toLowerCase() === 'f') {
			msg.channel.send(`${msg.author} has paid respects`);
			return;
		}

		if (msg.content.toLowerCase() === 'x') {
			msg.channel.send(`${msg.author} very much has doubts about this`);
			return;
		}
	}

	if (msg.author!.bot) {
		if (msg.channel.id === '763159605479079956' || msg.channel.id === '763081512752513084') {
			if (msg.author.id === '339254240012664832' || msg.author.id === '772205583536881694' || msg.author.id === '155149108183695360') return;
			if (msg.content.includes('SMH. Bot commands') || msg.content.includes('Welcome') ||msg.content.includes("imgflip.com") || msg.content.includes('do not post links here!') || msg.content.includes('vote') || msg.content.includes('very much has doubts') || msg.content.includes('has paid respects')) return;
			await msg.delete();
			msg.channel.send(
				'SMH. Bot commands go in <#763159637527756820> or <#763159688942190623>, Not general chats! \n\nIf this message appeared in error, please ignore it',
			);
		}
	}

	if (msg.content.toLowerCase() === 'make me a sandwich')
		msg.channel.send(`${msg.author} I can't, I have no condiments`);

	if (msg.content.toLowerCase() === 'what is the meaning of life?')
		msg.channel.send(`${msg.author} 42`);

	if (msg.channel.id === '462044347794456605' && msg.author.id === '155149108183695360')
		msg.channel.send('<@&462043912169586699> Please check the latest dyno case log.');

	if (msg.author.bot) return;

	if (msg.channel.id === '629075452723462154') {
		// Repost advertisement!
		await msg.delete();

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
			await msg.delete();
			await msg.author.send(`No ${msg.content}, only awoo!`);
		}
	}

	if (msg.guild!.id === '725201209358549012') {
		msg.member!.roles.cache.forEach((val) => {
			if (val.id === '739727880799518741') staff = true;
		});

		if (msg.content.includes('http') && !staff && !msg.content!.includes('tenor.com') && !msg.content!.includes('youtube.com') && !msg.content!.includes('twitter.com') && !msg.content!.includes('instagram.com')) {
			if(msg.channel.id !== '771415447538237450' || msg.content.includes('discord.gg')) {
				await msg.delete();
				await msg.reply(
					'please do not post links here! \n\nIf you\'re looking to partner, please check <#763159239605747712>',
				);
			}
		}
	}

	if (!msg.content.toLowerCase().startsWith(guild!.prefix.toLowerCase() ?? '!') || msg.author.bot)
		return;

	const args = msg.content
		.slice(guild!.prefix.length ?? '!')
		.trim()
		.split(/ +/);

	const commandName = args.shift()!.toLowerCase();

	const command =
		client.commands.get(commandName) ??
		client.commands.find((cmd) => cmd.aliases && cmd.aliases.includes(commandName));

	if (!command) return;

	if (!cooldownBypass.includes(msg.author.id)) {
		if (!client.commandCooldowns.has(command!.name))
			client.commandCooldowns!.set(command!.name, new Collection());

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
			command!.client = client;
			await command!.run(msg, args);
		}
	} catch (error) {
		console.error(error);
		await msg.reply('there was an error trying to execute that command!');
	}

	return;
});

client.on('messageDelete', async (messageDelete) => {
	if (messageDelete.author!.bot) return;

	if (messageDelete.attachments) {
		const a = messageDelete.attachments;
		a.forEach(function(b) {
			messageDelete.content = messageDelete.content + ' -- ' + b.url;
		});
	}

	try {
		// Send to local message channel
		const channel = messageDelete.guild!.channels.cache.find(
			(channel) => channel.name === 'message_logs',
		);

		await (channel as TextChannel).send({
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

client.on('channelCreate', async (channel) => {
	try {
		const c = (channel as TextChannel).guild.channels.cache.find(
			(c) => c.name === 'channel_logging',
		);
		await (c as TextChannel).send({
			embed: {
				color: 3447003,
				description: `A new channel (${(channel as TextChannel).name}) was created!`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.on('channelDelete', async (channel) => {
	try {
		const c = (channel as TextChannel).guild.channels.cache.find(
			(c) => c.name === 'channel_logging',
		);
		await (c as TextChannel).send({
			embed: {
				color: 16726088,
				description: `Channel (${(channel as TextChannel).name}) was deleted!`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.on('guildMemberAdd', async (member) => {
	try {
		const channel = member.guild.channels.cache.find((channel) => channel.name === 'user_logs');
		await (channel as TextChannel).send({
			embed: {
				color: 3447003,
				description: `A new member (${member.user!.username}) has joined!`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.on('guildMemberRemove', async (member) => {
	try {
		const channel = member.guild.channels.cache.find((channel) => channel.name === 'user_logs');
		await (channel as TextChannel).send({
			embed: {
				color: 16726088,
				description: `Member <@${member.id}> (${member.user!.username}) has left!`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.on('guildBanAdd', async (guild, member) => {
	try {
		const channel = guild.channels.cache.find((channel) => channel.name === 'case_logs');
		await (channel as TextChannel).send({
			embed: {
				color: 16726088,
				description: `Member <@${member.id}> (${member!.username}) has been banned!`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.on('guildBanRemove', async (guild, member) => {
	try {
		let channel = guild.channels.cache.find((channel) => channel.name === 'user_logs');

		await (channel as TextChannel).send({
			embed: {
				color: 16726088,
				description: `Member <@${member.id}> ban revoked`,
			},
		});

		channel = guild.channels.cache.find((channel) => channel.name === 'case_logs');

		await (channel as TextChannel).send({
			embed: {
				color: 16726088,
				description: `Member <@${member.id}> ban revoked`,
			},
		});
	} catch (e) {
		console.log(e);
	}
});

client.login(token);
