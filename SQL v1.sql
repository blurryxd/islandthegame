CREATE USER 'dbuser06' @'localhost' IDENTIFIED BY 'islandpass;
GRANT SELECT, INSERT, UPDATE, DELETE ON island.* TO dbuser06@localhost;

DROP DATABASE if EXISTS `island`;
CREATE DATABASE IF NOT EXISTS `island`;
USE `island`;

CREATE TABLE Location
(
  ID INT(25) NOT NULL,
  Nimi varchar(50)  NOT NULL,
  Tekstit varchar(400)  NOT NULL,
  Extratekstit varchar(200),
  PRIMARY KEY (ID)
);

INSERT INTO `Location` (`ID`, `Nimi`, `Tekstit`, `extratekstit`) VALUES
	(1, 'Boat', 'You wake up in a motorboat. There is water surrounding you everywhere but north. There is also a note right next to you.', ''),
	(2, 'Docks', 'You walk on the dock, and look around. You see a boat south from you and road towards north.', ''),
	(3, 'Abandoned House', 'You just stepped inside something ravaged and miserable. I guess you can still call it a house. Seems like no one has bothered coming here in a long time. There\'s a silver key laying on the floor.', ''),
	(4, 'Road4', 'You walk the footpath. Theres an abandoned house to your west, path to your north and path to your east.', ''),
	(5, 'Road5', 'You walk the footpath. Theres a path to your west, Town Hall in your north, footpath to your east and a dock to your south.', ''),
	(6, 'Road6', 'You walk the footpath. Theres a path to your west, path to your north and a bar to your east.', ''),
	(7, 'Bar', 'You enter the bar. It’s dark and smoky, but still feels rather cozy. Another day you could sit down for couple of drinks. The place looks as abandoned as every other place in the Island, even all the gold has been left behind.', ''),
	(8, 'Road8', 'You walk the footpath. Theres a path to your south and a graveyard to your north.', ''),
	(9, 'Town Hall', 'You step inside the old office building. There’s paper and other useless looking office equipment laying everywhere… You also spot a shovel in the corner. Why would anyone have a shovel in place like this?', ''),
	(10, 'Road10', 'You walk the footpath. Theres a path to your north and south.', ''),
	(11, 'Haunted house', 'You enter the haunted house. It’s an old and creepy place with not much decoration. There\'s candles giving you vision. There’s something in the corner. As you step closer, something creepy that seem to be floating in the air shows itself. You can see right through it!', 'You try to enter the haunted house, but a spooky ghost appears. The ghost demands your gold and shoo\'s you away. You run for your life.'),
	(12, 'Graveyard', 'You are at a graveyard. There are tombstones all around you and a rotten smell in the air. Looks like someone has buried something here... Someting else than just bodies. You can see an old, dimly lit church standing ahead of you in the north. On your west you also spot something, but it’s too dark to see. Theres also a pathway to your east.', ''),
	(13, 'Road13', 'You walk the pathway. Theres graveyard to your west and footpath to your east.', ''),
	(14, 'Road14', 'You walk the pathway. Theres path to your west and south. Theres also an old barn to your east.', ''),
	(15, 'Old Barn', 'You step inside the old barn, the building is barely standing at this point. There’s hay laying everywhere, you see metal crowbar under a haystack.', ''),
	(16, 'Church', 'You are inside a church that seems to be a thousand years old. The walls have been painted from floor to ceiling and covered with huge religious mosaic art. There\’s gasoline on the floor at the altar. I wonder what was going on in here...', ''),
	(17, 'Victory', 'You win!', '');
	
CREATE TABLE Player
(
  Player_ID INT(11) NOT NULL,
  location_ID INT(11) NOT NULL,
  PRIMARY KEY (Player_ID),
  FOREIGN KEY (location_ID) REFERENCES Location(ID)
);

INSERT INTO Player (Player_ID, location_ID) VALUES
	(1, 1);	
	
CREATE TABLE Items
(
  Item_ID INT(11) NOT NULL,
  Item_Name varchar(50) NOT NULL,
  Pickup_able INT(11) NOT NULL,
  Player_ID INT(11),
  location_ID INT(11) NOT NULL,
  examine varchar(400),
  PRIMARY KEY (Item_ID),
  FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID),
  FOREIGN KEY (location_ID) REFERENCES Location(ID)
);

INSERT INTO Items (Item_ID, Item_Name, Pickup_able, Player_ID, location_ID, examine) VALUES
	(1, 'Note', 1, NULL, 1, 'The note is moist and sallow from the dampness. You try to read the note but most of the ink has become un-readable. You can make up few words though: Theres still some ... head for the barn! Watch out, theres a ... ... out of the island.'),
	(2, 'Crowbar', 1, NULL, 15, 'A heavy all access key!'),
	(3, 'Gold', 1, NULL, 7, 'Shiny!'),
	(4, 'Town Hall key', 1, NULL, 11, 'A town hall key. For being Ghost\'s key, it looks rather boring.'),
	(5, 'Shovel', 1, NULL, 9, 'A tool for digging.'),
	(6, 'House key', 1, NULL, 12, 'A standard looking house key.'),
	(7, 'Silver key', 1, NULL, 3, 'A big silver key with a cross engraved in it.'),
	(8, 'Gasoline', 1, NULL, 16, 'A boat could use this.');
	
CREATE TABLE Siirtymä
(
  Direction varchar(50),
  From_ID INT(11),
  To_ID INT(11),
  Available bool,
  PRIMARY KEY (From_ID, To_ID),
  FOREIGN KEY (From_ID) REFERENCES Location(ID),
  FOREIGN KEY (To_ID) REFERENCES Location(ID)
);

INSERT INTO `Siirtymä` (`From_ID`, `Direction`, `To_ID`, `Available`) VALUES
	(1, 'north', 2, TRUE),
	(2, 'north', 5, TRUE),
	(2, 'south', 1, TRUE),
	(5, 'south', 2, TRUE),
	(5, 'west', 4, TRUE),
	(5, 'north', 9, FALSE),
	(5, 'east', 6, TRUE),
	(9, 'south', 5, TRUE),
	(4, 'west', 3, FALSE),
	(4, 'north', 8, TRUE),
	(4, 'east', 5, TRUE),
	(3, 'east', 4, TRUE),
	(8, 'south', 4, TRUE),
	(8, 'north', 12, TRUE),
	(12, 'south', 8, TRUE),
	(12, 'west', 11, FALSE),
	(12, 'north', 16, FALSE),
	(12, 'east', 13, TRUE),
	(11, 'east', 12, TRUE),
	(16, 'south', 12, TRUE),
	(13, 'west', 12, TRUE),
	(13, 'east', 14, TRUE),
	(14, 'west', 13, TRUE),
	(14, 'east', 15, TRUE),
	(14, 'south', 10, TRUE),
	(15, 'west', 14, TRUE),
	(10, 'north', 14, TRUE),
	(10, 'south', 6, TRUE),
	(6, 'north', 10, TRUE),
	(6, 'east', 7, FALSE),
	(6, 'west', 5, TRUE),
	(7, 'west', 6, TRUE),
	(1, 'south', 17, FALSE);
	