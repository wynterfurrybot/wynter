import { getRepository } from 'typeorm';

import { Guilds } from '../Models/Guilds';

export default async (id: string): Promise<Guilds | undefined> => {
	return getRepository(Guilds).findOne({
		where: { id },
	});
};
