DROP TABLE IF EXISTS feature;
CREATE TABLE IF NOT EXISTS `feature` (

	id INTEGER NOT NULL, 

	name VARCHAR(50), description VARCHAR(200) NULL, 

	PRIMARY KEY (id)

);

INSERT INTO feature VALUES(1,'Sci-Fi',NULL);

INSERT INTO feature VALUES(2,'Politics',NULL);

INSERT INTO feature VALUES(3,'Tech',NULL);

INSERT INTO feature VALUES(17,'agaj;',NULL);

INSERT INTO feature VALUES(18,'string',NULL);

DROP TABLE IF EXISTS scenario;
CREATE TABLE IF NOT EXISTS `scenario` (

	`id`	INTEGER NOT NULL,

	`title`	VARCHAR(80),

	`body`	TEXT,

	`pub_date`	DATETIME,

	`feature_id`	INTEGER, sequence INTEGER NULL,

	PRIMARY KEY(`id`),

	FOREIGN KEY(`feature_id`) REFERENCES `feature`(`id`)

);

INSERT INTO scenario VALUES(1,'The Road to Extinction','The drought had lasted now for ten million years, and the reign of the terrible lizards had long since ended. Here on the Equator, in the continent which would one day be known as Africa, the battle for existence had reached a new climax of ferocity, and the victor was not yet in sight. In this barren and desiccated land, only the small or the swift or the fierce could flourish, or even hope to survive.','2016-06-11 15:56:29.200201',1,NULL);

INSERT INTO scenario VALUES(2,'The New Rock','Late that night, Moon-Watcher suddenly awoke. Tired out by the day’s exertions and disasters, he had been sleeping more soundly than usual, yet he was instantly alert at the first faint scrabbling down in the valley.','2016-06-11 16:38:48.496609',1,NULL);

INSERT INTO scenario VALUES(3,'Academy','Moon-Watcher and his companions had no recollection of what they had seen, after the crystal had ceased to cast its hypnotic spell over their minds and to experiment with their bodies. The next day, as they went out to forage, they passed it with scarcely a second thought; it was now part of the disregarded background of their lives. They could not eat it, and it could not eat them; therefore it was not important.','2016-06-11 16:38:51.149464',1,NULL);

INSERT INTO scenario VALUES(4,'The Leopard','The tools they had been programmed to use were simple enough, yet they could change this world and make the man-apes its masters. The most primitive was the hand-held stone, that multiplied manyfold the power of a blow. Then there was the bone club, that lengthened the reach and could provide a buffer against the fangs or claws of angry animals. With these weapons, the limitless food that roamed the savannas was theirs to take.','2016-06-11 16:38:51.508791',1,NULL);

INSERT INTO scenario VALUES(5,'Encounter in the Dawn','As he led the tribe down to the river in the dim light of dawn, Moon-Watcher paused uncertainly at a familiar spot. Something, he knew, was missing; but what it was, he could not remember. He wasted no mental effort on the problem, for this morning he had more important matters on his mind.','2016-06-19 10:07:47.702359',1,NULL);

INSERT INTO scenario VALUES(6,'asf','one','2017-09-19 04:58:02.943138',18,NULL);

INSERT INTO scenario VALUES(7,'string','scenario1','2017-09-19 06:29:33.654085',2,12);

INSERT INTO scenario VALUES(8,'string','scenario2','2017-09-19 06:35:20.599975',2,13);

INSERT INTO scenario VALUES(9,'string','scenario4','2017-09-19 06:35:27.960240',2,NULL);

INSERT INTO scenario VALUES(10,'string','scenario5','2017-09-19 06:37:26.680970',2,NULL);

DROP TABLE IF EXISTS alembic_version;
CREATE TABLE IF NOT EXISTS `alembic_version` (

	version_num VARCHAR(32) NOT NULL, 

	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)

);

INSERT INTO alembic_version VALUES('5c969c45bb53');

INSERT INTO alembic_version VALUES('d9d5eb4d6211');

INSERT INTO alembic_version VALUES('75248a2c7fa8');

