import { getRepository } from 'typeorm';

import { Twitter } from '../../Models/Twitter';

export default async (schema: Twitter): Promise<Twitter> => {
	const twitterRepo = getRepository(Twitter);

	const newTwitter = new Twitter();

	newTwitter.id = schema.id;
	newTwitter.secret = schema.secret;
	newTwitter.token = schema.token;
	newTwitter.username = schema.username;

	return twitterRepo.save(newTwitter);
};
