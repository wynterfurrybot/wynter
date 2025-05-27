# Wynter v2
Wynter Rewrite, made from Python

Made on a CC-BY license.

Uses the following libaries: 

discord.py - 1.6.0a

Fully open sourced.

Docs: https://docs.furrybot.dev/

Support: [https://discord.gg/5eNDkdd](https://discord.gg/EG5pUEmnXb)

How to self host Wynter: 
```
$ git clone https://github.com/Rapptz/discord.py
$ cd discord.py
$ python3 -m pip install -U .
$ cd ..
$ git clone https://github.com/wynterfurrybot/wynter.git
$ cd wynter2
$ cd Wynter
$ python3 -m pip install -r requirements.txt 

IF SUCCESSFUL:
$ mv example.env .env
$ nano .ev
IN NANO, edit the values to match your config.
CTRL X to save.
$ python3 index.py

IF NOT: 
you may need to update PIP by doing the command below:
$ python3 -m pip install --upgrade pip
then repeat the command to install requirements.
```

Database structures:

(I totally forgot to include this before today, lol, whoops)

```
CREATE TABLE `eco` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `server_id` varchar(255) NOT NULL,
  `money` int NOT NULL DEFAULT '100',
  `in_jail` tinyint(1) DEFAULT '0',
  `bank` int DEFAULT '0',
  `wages_docked` tinyint(1) DEFAULT '0',
  `server_currency` varchar(255) DEFAULT 'pounds',
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_server_unique` (`user_id`,`server_id`)
);

 CREATE TABLE `guilds` (
  `id` varchar(20) COLLATE utf8mb4_general_ci NOT NULL COMMENT 'Guild ID',
  `name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'The Guild Name',
  `prefix` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '!' COMMENT 'The Prefix',
  `deleteinvlinks` tinyint DEFAULT '0' COMMENT 'Delete inv links or not',
  `enablefandx` tinyint DEFAULT '0' COMMENT 'Enable F and X commands or not',
  `dadjokes` tinyint(1) NOT NULL DEFAULT '0',
  `enfandximages` tinyint DEFAULT '0' COMMENT 'Enable / disable f and x command images.',
  `muterole` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'The guilds mute role',
  PRIMARY KEY (`id`)
);

-- Note: Punishments table is currently not in use, we need to fix this! --

CREATE TABLE `punishments` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Incremented ID',
  `servername` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'The Guild Name',
  `serverid` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT 'The server ID',
  `offender` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT 'The offender name',
  `offenderid` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `moderator` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT 'The moderator name',
  `type` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT 'Type of punishment',
  `reason` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT 'Reason of punishment',
  PRIMARY KEY (`id`)
);
```

# Branches:

Beta - for development use only, these updates may not be finished, or ever come to the master branch.

Master - for stable releases.

# Notice:

Relms (a former dev) no longer works on Wynter as of v2. Previous commits by her may be archived here.

