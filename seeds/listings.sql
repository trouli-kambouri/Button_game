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
