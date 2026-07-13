# User stories


## Title: A user can sign up

User story:
As someone with a space to rent
I want to sign up as a user of MakersBnB
So I can then use the platform to list and rent my space

Acceptance criteria:
- A user can navigate to a sign up page
- When then complete the form using valid credentials, they are automatically logged in and redirected to the spaces index page
- All tests pass
- Out of scope: manually logging in
- Out of scope: listing spaces
- Out of scope: Logging out

Tests:
- The user is redirected to "/spaces" after signing up
- The user's name is included somewhere on the page as part of a greeting which confirms they are now signed in


## Title: A signed up user can log in

User story:
As a signed up user of MakersBnB
So that I can check my account
I want to log into the platform

Acceptance criteria:
- A user can navigate to the login page
- When they use their valid credentials to log inm they are redirected to the spaces index page
- All tests pass
- Out of scope: listing spaces
- Out of scope: Logging out

Tests:
- The user is redirected to "/spaces" after signing in
- The user's name is included somewhere on the page as part of a greeting which confirms they are now signed in

## Title: A signed in user can list a space

User story:
As a signed in user
So that I can make money from renting my space
I want to create a listing for that space
And it should include all the basic details

Acceptance criteria:
- A signed in user can navigate to a form for creating a listing
- The form only asks for a space name, location, description and price
- When they submit the form with valid data
  - They are redirected to a page that displays their new listing as confirmation
  - The new space is visible in a list of all spaces
- All tests pass
- Out of scope: deleting a listing
- Out of scope: logging out
- Out of scope: editing a listing
- Out of scope: bookings
- Out of scope: space images

Tests:
- The newly listed space includes all details entered into the form
- The newly listed space appears in a list of spaces

