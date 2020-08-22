import { getRepository } from 'typeorm';

import { Guilds } from '../Models/guild';

export default async (schema: Guilds): Promise<Guilds> => {
	const guildRepo = getRepository(Guilds);

	const newGuild = new Guilds();

	newGuild.blacklistedWords = schema.blacklistedWords;
	newGuild.deleteInvLinks = schema.deleteInvLinks;
	newGuild.id = schema.id;
	newGuild.name = schema.name;
	newGuild.prefix = schema.prefix;

	return guildRepo.save(newGuild);
};
