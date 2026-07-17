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
