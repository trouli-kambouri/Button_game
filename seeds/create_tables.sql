DROP TABLE IF EXISTS listings;
DROP TABLE IF EXISTS users;

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
    price_per_night INT NOT NULL
);