import {Column, Entity, PrimaryGeneratedColumn} from 'typeorm';

@Entity({
	synchronize: true,
	name: 'punishments',
})
export class Punishments {
	@PrimaryGeneratedColumn({
		name: 'id',
		comment: 'Incremented ID',
	})
	id!: string;

	@Column('varchar', {
		name: 'servername',
		comment: 'The Guild Name',
		nullable: true,
	})
	serverName!: string;

	@Column('varchar', {
		name: 'serverid',
		comment: 'The server ID',
		nullable: false,
		unique: true,
	})
	serverId!: string;

	@Column('varchar', {
		name: 'offender',
		comment: 'The offender ID',
		nullable: false,
		unique: false,
	})
	offender!: string;

	@Column('varchar', {
		name: 'moderator',
		comment: 'The moderator ID',
		nullable: false,
		unique: false,
	})
	moderator!: string;

	@Column('varchar', {
		name: 'type',
		comment: 'Type of punishment',
		nullable: false,
		unique: false,
	})
	type!: string;

	@Column('varchar', {
		name: 'reason',
		comment: 'Reason of punishment',
		nullable: false,
		unique: false,
	})
	reason!: string;
}
