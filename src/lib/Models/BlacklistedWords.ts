import { Column, Entity, ManyToOne, PrimaryColumn } from 'typeorm';

import { Guilds } from './Guilds';

@Entity({
	synchronize: true,
	name: 'blacklistedwords',
})
export class BlacklistedWords {
	@PrimaryColumn('int', {
		unique: true,
		name: 'id',
		comment: 'Auto Incrementing ID to make mssql stfu xD',
		nullable: false,
		generated: 'increment',
	})
	id!: string;

	@ManyToOne(() => Guilds, (guild) => guild.id, {
		nullable: true,
	})
	guild!: Guilds;

	@Column('varchar', {
		length: 255,
		unique: false,
		name: 'word',
		comment: 'The blacklisted word',
		nullable: false,
	})
	word!: string;
}
