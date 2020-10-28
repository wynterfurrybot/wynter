import { getRepository } from 'typeorm';

import { Twitter } from '../../Models/Twitter';

export default async (id: string): Promise<Twitter | undefined> => {
	return getRepository(Twitter).findOne({
		where: { id },
	});
};
