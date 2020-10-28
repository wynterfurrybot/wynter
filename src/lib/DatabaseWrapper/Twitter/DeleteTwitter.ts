import { DeleteResult, getRepository } from 'typeorm';

import { Twitter } from '../../Models/Twitter';

export default async (id: string): Promise<DeleteResult | undefined> => {
	const twitterRepo = getRepository(Twitter);

	const twitter = await twitterRepo.findOne({
		where: { id },
	});

	if (twitter === undefined) return undefined;

	return twitterRepo.delete(twitter);
};
