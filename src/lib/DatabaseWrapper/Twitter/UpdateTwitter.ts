import { getRepository } from 'typeorm';

import { Twitter } from '../../Models/Twitter';

export default async (id: string, schema: Partial<Twitter>): Promise<Twitter | undefined> => {
	const twitter = await getRepository(Twitter).findOne({
		where: { id },
	});

	if (twitter === undefined) return undefined;

	twitter.id = schema.id ?? twitter.id;
	twitter.secret = schema.secret ?? twitter.secret;
	twitter.username = schema.username ?? twitter.username;
	twitter.token = schema.token ?? twitter.token;

	const updatedTwitter = await getRepository(Twitter).save(twitter);

	return updatedTwitter;
};
