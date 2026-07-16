DROP TABLE IF EXISTS bookings;


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



INSERT INTO bookings (start_date, end_date, listing_id, guest_id, status)
    VALUES
        ('2026-11-21', '2026-11-22', 1, 3, 'requested'),
        ('2026-10-21', '2026-10-22', 1, 3, 'requested'),
        ('2026-08-21', '2026-08-22', 2, 3, 'confirmed');