-- NOTE - will delete FK on referencing bookings table
DROP TABLE IF EXISTS listings CASCADE;

CREATE TABLE listings(
    id SERIAL PRIMARY KEY, 
    owner_id INT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    price_per_night INT NOT NULL,
    available_from DATE NOT NULL,
    available_until DATE NOT NULL,
    thumbnail VARCHAR(255),

    CONSTRAINT valid_date_range CHECK (available_from <= available_until),
    CONSTRAINT fk_owner FOREIGN KEY(owner_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO listings (
    owner_id, title, description, price_per_night, available_from, available_until, thumbnail)
    VALUES 
        (1, 'Rain-soaked shed on a mountain', 'Greenfield', 71, '2026-01-01', '2026-01-31', 'Greenfield.png'),
        (1, 'Uncomfortable camper van in a lay-by', 'Newtown', 21, '2026-01-01', '2026-01-31', 'Newton.png'),
        (2, 'Glamorous pad in fancy town', 'Hopington', 311, '2026-01-01', '2026-01-31', 'Hopington.png'),
        (2, 'Medieval castle with ghost included', 'Spooksville', 199, '2026-01-01', '2026-01-31', 'Spooksville.png'),
        (3, 'Luxury treehouse with unreliable ladder', 'Treeford', 89, '2026-01-01', '2026-01-31', 'Treeford.png'),
        (1, 'Converted bus stop with panoramic traffic views', 'Roundabout-on-Sea', 34, '2026-01-01', '2026-01-31', 'Roundabout-on-sea.png'),
        (4, 'Medieval prison cell', 'Stonechester', 66, '2026-01-01', '2026-01-31', 'Stonechester.png'),
        (2, 'Studio flat above a loud pub', 'Pintbury', 88, '2026-01-01', '2026-01-31', 'Pintbury.png'),
        (5, 'Floating house that is not sinking', 'Above Mariana''s Trench', 112, '2026-01-01', '2026-01-31', 'Above_marianas_trench.png'),
        (3, 'Countryside cottage with sheep included', 'Baaxton', 93, '2026-01-01', '2026-01-31', 'Baaxton.png'),
        (4, 'Tiny house that is not a shed', 'Little Houseton', 68, '2026-01-01', '2026-01-31', 'Little_Houseton.png'),
        (5, 'Beach hut only 5 days walk from beach', 'Landlockedshire', 58, '2026-01-01', '2026-01-31', 'Landlockedshire.png');
        
