DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT,
    password TEXT NOT NULL
);

INSERT INTO users (name, email, phone_number, password)
    VALUES
        ('kayleighkarpal', 'kayleighk@kickabout.com', '07635183911', 'badpassword'),
        ('mingma', 'maming@matsforcats.co.uk', '07876543909', '-*76sjfyemv'),
        ('gurpeetgill', 'gurpgill@grillsforu.net', '07652987709', 'youcantguess'),
        ('salsalamander', 'salsal@salsalsalads.net', '076526479839', 'icanguess'),
        ('taliatipple', 'ttipple@taliastipples.co.uk', '07856981178', 'guessmeifyoudare');
