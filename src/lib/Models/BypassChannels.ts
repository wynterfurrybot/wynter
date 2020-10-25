import { Column, Entity, ManyToOne, PrimaryColumn } from 'typeorm';

import { Guilds } from './Guilds';

@Entity({
	synchronize: true,
	name: 'bypasschannels',
})
export class BypassChannels {
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
		name: 'channelid',
		comment: 'The Channel ID',
		nullable: false,
	})
	channelid!: string;
}
