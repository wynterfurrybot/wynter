import { Column, Entity, OneToMany, PrimaryColumn } from 'typeorm';
import { BlacklistedWords } from './BlacklistedWords';
import { BypassChannels } from './BypassChannels';

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

	@Column('bit', {
		name: 'enablefandx',
		comment: 'Enable F and X commands or not',
		nullable: true,
		default: 0,
	})
	enableFAndXs!: boolean;

	@Column('varchar', {
		name: 'muterole',
		comment: 'The guilds mute role',
		nullable: true,
		default: null,
	})
	muteRole!: string | null;

	@OneToMany(() => BlacklistedWords, (BlacklistedWords) => BlacklistedWords.guild, {
		nullable: true,
		cascade: true,
		eager: true,
	})
	blacklistedWords!: BlacklistedWords[];

	@OneToMany(() => BypassChannels, (BypassChannels) => BypassChannels.guild, {
		nullable: true,
		cascade: true,
		eager: true,
	})
	bypassChannels!: BypassChannels[];
}
