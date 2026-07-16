DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS booking_statuses CASCADE;
DROP TABLE IF EXISTS listings CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT,
    password TEXT NOT NULL
);

CREATE TABLE listings (
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

-- TODO: Add column for url image to listings

CREATE TABLE booking_statuses (
    id INT PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    listing_id INT NOT NULL,
    guest_id INT NOT NULL,
    status VARCHAR(20) NOT NULL,
    CONSTRAINT fk_listing FOREIGN KEY(listing_id) 
        REFERENCES listings(id) 
        ON DELETE CASCADE,
    CONSTRAINT fk_guest FOREIGN KEY(guest_id) 
        REFERENCES users(id) 
        ON DELETE CASCADE
);


INSERT INTO booking_statuses (id, name)
    VALUES
        (1, 'requested'),
        (2, 'confirmed'),
        (3, 'denied'),
        (4, 'completed');

INSERT INTO users (name, email, phone_number, password)
    VALUES
        ('kayleighkarpal', 'kayleighk@kickabout.com', '07635183911', 'badpassword'),
        ('mingma', 'maming@matsforcats.co.uk', '07876543909', '-*76sjfyemv'),
        ('gurpeetgill', 'gurpgill@grillsforu.net', '07652987709', 'youcantguess'),
        ('salsalamander', 'salsal@salsalsalads.net', '076526479839', 'icanguess'),
        ('taliatipple', 'ttipple@taliastipples.co.uk', '07856981178', 'guessmeifyoudare');

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

INSERT INTO bookings (start_date, end_date, listing_id, guest_id, status)
    VALUES
        ('2026-11-21', '2026-11-22', 1, 3, 'requested'),
        ('2026-10-21', '2026-10-22', 1, 3, 'requested'),
        ('2026-08-21', '2026-08-22', 2, 3, 'requested');