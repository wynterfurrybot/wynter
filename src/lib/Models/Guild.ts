import { Entity, PrimaryColumn, Column } from 'typeorm';

@Entity({
	synchronize: true,
	name: 'guilds',
})
export class Guilds {
	@PrimaryColumn('varchar', {
		length: 20,
		unique: true,
		name: 'id',
		comment: 'Guild ID',
		nullable: false,
	})
	id!: string;

	@Column('varchar', {
		name: 'name',
		comment: 'The Guild Name',
		nullable: true,
	})
	name!: string;

	@Column('varchar', {
		name: 'prefix',
		comment: 'The Prefix',
		default: '!',
		nullable: true,
	})
	prefix!: string;

	@Column('bit', {
		name: 'deleteinvlinks',
		comment: 'Delete inv links or not',
		nullable: true,
		default: 0,
	})
	deleteInvLinks!: boolean;

	@Column('varchar', {
		name: 'blacklistedwords',
		default: '{}',
		nullable: true,
		comment: 'Blacklisted words',
	})
	blacklistedWords!: string[];

	@Column('varchar', {
		name: 'bypasschannels',
		default: '{}',
		nullable: true,
		comment: 'Channels that bypass swear filter',
	})
	bypassChannels!: string[];
}
