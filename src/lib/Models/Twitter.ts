import { Column, Entity, PrimaryColumn } from 'typeorm';

@Entity({
	synchronize: true,
	name: 'twitter',
})
export class Twitter {
	@PrimaryColumn('varchar', {
		length: 255,
		unique: true,
		name: 'id',
		nullable: false,
	})
	id!: string;

	@Column('varchar', {
		length: 255,
		unique: true,
		name: 'secret',
		nullable: false,
	})
	secret!: string;

	@Column('varchar', {
		length: 255,
		unique: true,
		name: 'token',
		nullable: false,
	})
	token!: string;

	@Column('varchar', {
		length: 255,
		unique: true,
		name: 'username',
		nullable: false,
	})
	username!: string;
}
