INSERT INTO tbl_stages (stage_name) VALUES
('Basic'),
('Stage 1'),
('Stage 2'),
('EX'),
('V'),
('VSTAR');

INSERT INTO tbl_types (type_name) VALUES
('Fire'),
('Water'),
('Grass'),
('Electric'),
('Psychic'),
('Fighting'),
('Dark'),
('Metal'),
('Fairy'),
('Dragon');

INSERT INTO tbl_collections (collection_name, release_date, total_cards) VALUES
('Base Set', '1999-01-09', 102),
('Jungle', '1999-06-16', 64),
('Fossil', '1999-10-10', 62),
('Team Rocket', '2000-04-24', 83),
('Neo Genesis', '2000-12-16', 111);

INSERT INTO tbl_cards (
    hp, name, info, attack, damage, weak, ressis, retreat,
    card_number, collection_id, stage_id, type_id
) VALUES
-- 1. Pikachu (Base Set)
(40, 'Pikachu', 'Mouse Pokémon', 'Thunder Jolt', '30', 'Fighting', 'Metal', '1',
 25, 1, 1, 4),

-- 2. Charizard (Base Set)
(120, 'Charizard', 'Flame Pokémon', 'Fire Spin', '100', 'Water', 'Fighting', '3',
 4, 1, 3, 1),

-- 3. Blastoise (Base Set)
(100, 'Blastoise', 'Shellfish Pokémon', 'Hydro Pump', '40+', 'Electric', 'None', '3',
 2, 1, 3, 2),

-- 4. Bulbasaur (Base Set)
(40, 'Bulbasaur', 'Seed Pokémon', 'Leech Seed', '20', 'Fire', 'Water', '1',
 44, 1, 1, 3),

-- 5. Eevee (Jungle)
(50, 'Eevee', 'Evolution Pokémon', 'Quick Attack', '10+', 'Fighting', 'Psychic', '1',
 51, 2, 1, 5),

-- 6. Snorlax (Jungle)
(90, 'Snorlax', 'Sleeping Pokémon', 'Body Slam', '30', 'Fighting', 'None', '4',
 11, 2, 1, 6),

-- 7. Dragonite (Fossil)
(100, 'Dragonite', 'Dragon Pokémon', 'Slam', '40x', 'Ice', 'Fighting', '2',
 4, 3, 3, 10),

-- 8. Gengar (Fossil)
(80, 'Gengar', 'Shadow Pokémon', 'Nightmare', '30', 'Dark', 'Fighting', '1',
 5, 3, 3, 5),

-- 9. Dark Charmeleon (Team Rocket)
(50, 'Dark Charmeleon', 'Flame Pokémon', 'Fireball', '50', 'Water', 'Grass', '1',
 32, 4, 2, 1),

-- 10. Togepi (Neo Genesis)
(40, 'Togepi', 'Spike Ball Pokémon', 'Charm', '—', 'Metal', 'Dark', '1',
 51, 5, 1, 9);
