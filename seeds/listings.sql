DROP TABLE IF EXISTS listings;

CREATE TABLE listings(
    id SERIAL PRIMARY KEY, 
    owner_id INT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    price_per_night INT NOT NULL,
    thumbnail VARCHAR(255),
    CONSTRAINT fk_owner FOREIGN KEY(owner_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO listings (
    owner_id, title, description, price_per_night, thumbnail)
    VALUES 
        (1, 'Rain-soaked shed on a mountain', 'Greenfield', 71, 'Greenfield.png'),
        (1, 'Uncomfortable camper van in a lay-by', 'Newtown', 21, 'Newton.png'),
        (2, 'Glamorous pad in fancy town', 'Hopington', 311, 'Hopington.png'),
        (2, 'Medieval castle with ghost included', 'Spooksville', 199, 'Spooksville.png'),
        (3, 'Luxury treehouse with unreliable ladder', 'Treeford', 89, 'Treeford.png'),
        (1, 'Converted bus stop with panoramic traffic views', 'Roundabout-on-Sea', 34, 'Roundabout-on-sea.png'),
        (3, 'Medieval prison cell', 'Stonechester', 66, 'Stonechester.png'),
        (2, 'Studio flat above a loud pub', 'Pintbury', 88, 'Pintbury.png'),
        (3, 'Floating house that is not sinking', 'Above Mariana''s Trench', 112, 'Above_marianas_trench.png'),
        (3, 'Countryside cottage with sheep included', 'Baaxton', 93, 'Baaxton.png'),
        (3, 'Tiny house that is not a shed', 'Little Houseton', 68, 'Little_Houseton.png'),
        (3, 'Beach hut only 5 days walk from beach', 'Landlockedshire', 58, 'Landlockedshire.png');