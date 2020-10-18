import { DeleteResult, getRepository } from 'typeorm';

import { Guilds } from '../Models/Guilds';

export default async (id: string): Promise<DeleteResult | undefined> => {
	const guildRepo = getRepository(Guilds);

	const guild = await guildRepo.findOne({
		where: { id },
	});

	if (guild === undefined) return undefined;

	return guildRepo.delete(guild);
};
