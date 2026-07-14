DROP TABLE IF EXISTS listings;

CREATE TABLE listings(
    id SERIAL PRIMARY KEY, 
    owner_id INT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    price_per_night INT NOT NULL,
    CONSTRAINT fk_owner FOREIGN KEY(owner_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO listings (
    owner_id, title, description, price_per_night)
    VALUES 
        (1, 'Rain-soaked shed on a mountain', 'Greenfield', 71),
        (1, 'Uncomfortable camper van in a lay-by', 'Newtown', 21),
        (2, 'Glamorous pad in fancy town', 'Hopington', 311);
        (2, 'Castle with only three ghosts included', 'Spookingham', 199),
        (3, 'Luxury treehouse with unreliable ladder', 'Treeford', 89),
        (1, 'Converted bus stop with panoramic traffic views', 'Roundabout-on-Sea', 34),
        (4, 'Medieval prison cell', 'Stonechester', 66),
        (2, 'Studio flat above a loud pub', 'Pintbury', 88),
        (5, 'Floating house that is not sinking', 'Above Mariana''s Trench', 112),
        (3, 'Countryside cottage with sheep included', 'Baaxton', 93),
        (4, 'Tiny house that is not a shed', 'Little Houseton', 68),
        (5, 'Beach hut only 5 days walk from beach', 'Landlockedshire', 58);
