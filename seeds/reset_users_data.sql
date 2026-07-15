-- Have to do both because of FK on listings
TRUNCATE TABLE listings, users RESTART IDENTITY;
-- Also works:
-- TRUNCATE TABLE users RESTART IDENTITY;



INSERT INTO users (name, email, phone_number, password)
    VALUES
        ('kayleighkarpal', 'kayleighk@kickabout.com', '07635183911', 'badpassword'),
        ('mingma', 'maming@matsforcats.co.uk', '07876543909', '-*76sjfyemv'),
        ('gurpeetgill', 'gurpgill@grillsforu.net', '07652987709', 'youcantguess'),
        ('salsalamander', 'salsal@salsalsalads.net', '076526479839', 'icanguess'),
        ('taliatipple', 'ttipple@taliastipples.co.uk', '07856981178', 'guessmeifyoudare');
