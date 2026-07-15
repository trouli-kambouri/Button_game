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
    owner_id INT NOT NULL
        REFERENCES users(id)
        ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    price_per_night INT NOT NULL,
    available_from DATE NOT NULL,
    available_until DATE NOT NULL,

    CONSTRAINT valid_date_range CHECK (available_from <= available_until)
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
    status INT NOT NULL,
    CONSTRAINT fk_listing FOREIGN KEY(listing_id) 
        REFERENCES listings(id) 
        ON DELETE CASCADE,
    CONSTRAINT fk_guest FOREIGN KEY(guest_id) 
        REFERENCES users(id) 
        ON DELETE CASCADE,
    CONSTRAINT fk_statuses FOREIGN KEY(status) 
        REFERENCES booking_statuses(id) 
        ON DELETE CASCADE
);

INSERT INTO booking_statuses (id, name)
    VALUES
        (1, 'requested'),
        (2, 'confirmed'),
        (3, 'denied'),
        (4, 'past');