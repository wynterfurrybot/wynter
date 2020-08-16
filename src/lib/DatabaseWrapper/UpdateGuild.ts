import { getRepository } from 'typeorm';

import { Guilds } from '../Models/guild';

export default async (id: string, schema: Partial<Guilds>): Promise<Guilds | undefined> => {
	const guild = await getRepository(Guilds).findOne({
		where: { id },
	});

	if (guild === undefined) {
		return undefined;
	}

	guild.id = schema.id ?? guild.id;
	guild.name = schema.name ?? guild.name;
	guild.prefix = schema.prefix ?? guild.prefix;
	guild.blacklistedWords = schema.blacklistedWords ?? guild.blacklistedWords;
	guild.deleteInvLinks = schema.deleteInvLinks ?? guild.deleteInvLinks;

	const updatedGuild = await getRepository(Guilds).save(guild);

	return updatedGuild;
};
