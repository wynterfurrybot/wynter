import { getRepository } from 'typeorm';

import { Guilds } from '../Models/guild';

export default async (id: string): Promise<Guilds | undefined> => {
	return getRepository(Guilds).findOne({
		where: { id },
	});
};
