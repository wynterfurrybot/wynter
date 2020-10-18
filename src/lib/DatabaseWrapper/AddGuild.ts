import { getRepository } from 'typeorm';

import { Guilds } from '../Models/Guilds';

export default async (schema: Guilds): Promise<Guilds> => {
	const guildRepo = getRepository(Guilds);

	const newGuild = new Guilds();

	newGuild.blacklistedWords = schema.blacklistedWords;
	newGuild.deleteInvLinks = schema.deleteInvLinks;
	newGuild.id = schema.id;
	newGuild.name = schema.name;
	newGuild.prefix = schema.prefix;
	newGuild.bypassChannels = schema.bypassChannels;
	newGuild.enableFAndXs = schema.enableFAndXs;

	return guildRepo.save(newGuild);
};
