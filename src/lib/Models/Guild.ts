import { Entity, PrimaryColumn, Column } from 'typeorm';

@Entity({
	synchronize: true,
	name: 'guilds',
})
export class Guilds {
	@PrimaryColumn('varchar', {
		length: 255,
		unique: true,
		name: 'id',
		comment: 'Guild ID',
		nullable: false,
	})
	id!: string;

	@Column('varchar', {
		name: 'name',
		comment: 'The Guild Name',
		nullable: false,
	})
	name!: string;

	@Column('varchar', {
		name: 'prefix',
		comment: 'The Prefix',
		default: '!',
		nullable: false,
	})
	prefix!: string;

	@Column('bool', {
		name: 'deleteinvlinks',
		comment: 'Delete inv links or not',
		nullable: false,
		default: false,
	})
	deleteInvLinks!: boolean;

	@Column('varchar', {
		array: true,
		name: 'blacklistedwords',
		default: '{}',
		nullable: false,
		comment: 'Blacklisted words',
	})
	blacklistedWords!: string[];
}
