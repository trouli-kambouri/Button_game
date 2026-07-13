DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS spaces;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT,
    password TEXT NOT NULL
);

CREATE TABLE spaces(
    id SERIAL PRIMARY KEY, 
    owner_id INT NOT NULL REFERENCES users(id),
    title TEXT NOT NULL,
    description TEXT,
    price_per_night INT NOT NULL
);