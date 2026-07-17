CREATE TABLE listing_images (
    id SERIAL PRIMARY KEY,
    listing_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    position INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_listing 
        FOREIGN KEY(listing_id) 
        REFERENCES listings(id) 
        ON DELETE CASCADE
);