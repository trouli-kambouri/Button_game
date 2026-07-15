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


INSERT INTO bookings (start_date, end_date, listing_id, guest_id, status)
    VALUES
        ('2026-11-21', '2026-11-22', 1, 3, 1),
        ('2026-10-21', '2026-10-22', 1, 3, 1),
        ('2026-08-21', '2026-08-22', 2, 3, 2);