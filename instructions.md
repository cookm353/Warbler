# Warbler

PorousLoris
353straw

## Part 1: Fix Current Features

### Step 1: Understand the Model

- [x] Read models.py
  - [x] Make a diagram of the tables
  - [x] Why does the follows table have two FKs?
    - [x] One for the user following, another for the user being followed
- [x] Set up a debugger in a route using pdb
  - [x] Activate it to pause execution
  - [x] Test the relationships between the model classes to understand how they work

### Step 2: Fix Logout

- [x] Implement logout route
- [x] Add a flash message and redirect to login page

### Step 3: Fix User Profile

- User profile works, but needs to have the following added
  - [x] Location
  - [x] Bio
  - [x] Header image (should be a background at the top)
  
### Step 4: Fix User Cards
  
- [x] User cards need to show bio for users...
  - [x] Followers page
  - [x] Following page
  - [x] List-users page

### Step 5: Profile Edit

- [x] Implement buttons for editing profile
  - [x] Ensure user is logged on first!
  - [x] Show a form with the following:
    - [x] Username
    - [x] Email
    - [x] image_url
    - [x] header_image_url
    - [x] bio
    - [x] password
- [x] Check if the password is valid
  - [x] If not, flash an error and return to homepage
- [x] Form should edit the user for all fields *except* their password
  - [x] The password field is only to check if it's the right current password
- [x] On success, it should redirect to user detail page

### Step 6: Fix Homepage

- [x] Home page for logged-in users should show that last 100 warbles from only users that the logged-in user is following and the user, **not** all users

### Step 7: Research and Understand Login Strategy

- [ ] Check out code in app.py related to authentication
  - [ ] How's the logged in user being kept track of?
  - [ ] What's the **g** object?
    - **g** is a namespace that can hold data in the application context
    - Data persists as lok as the page is open
    - 
  - [ ] What's the purpose of `add_user_to_g`?
    - Store the current user so they can be accessed more easily
  - [ ] What does `@app.before_request` mean?
    - Decorator that causes the function to run before any request is handled
  
## Part 2: Add Likes

- Don't use any JS for this step!
- [x] Add a feature allowing a user to like and unlike warbles
  - [x] Users should only be able to like warbles written by other users
  - [x] Liking a warble should add a star or some other symbol next to the liked warble
  - [x] Liking and unliking a warble should be done by clicking on the star (or other symbol)
- [x] Profile page should show how many warbles the user has liked
  - [x] There should be a link to a page showing the user's liked warbles

## Part 3: Add Tests

- There are 4 test files: test_user_model.py, test_user_views.py, test_message_model.py, and test_message_views.py
  - Two tests for testing models, and two for testing routes/view functions
- Tests for user model to include:
  - [x] Does repr work properly?
  - [x] Does is_following detect when user1 is following user2?
  - [x] Does is_following detect when user1 isn't following user2?
  - [x] Does is_followed_by successfully detect when user1 is followed by user2?
  - [x] Does is_followed_by successfully detect when user1 is not followed by user2?
  - [x] Does User.create successfully create a new user given valid credentials?
  - [x] Does User.create fail to create a new user if any of the validations (e.g. uniqueness, non-nullable fields) fail?
  - [x] Does User.authenticate successfully return a user when given a valid username and password?
  - [x] Does User.authenticate fail to return a user when the username is invalid?
  - [x] Does User.authenticate fail to return a user when the password is invalid?
- Include similar tests for the message model
- Tests routes as per usual

## Further Study

- [ ] Add a custom 404 page
- [ ] Add AJAX
  - [ ] When liking/unliking warbles so users don't have to refresh the page
  - [ ] Composing warbles via a popup modal that's available on every page via the navbar button
- [ ] DRY Up Templates
  - [ ] Reduce the amount of repetition in templates
  - [ ] Look up {% include %} and use this so forms aren't so repetitive
  - [ ] Learn about {% macro %} and {% import %} statements to reduce repetition in user detail, followers, followed_user pages, and more
- [ ] DRY Up Auth
  - Multiple routes have several lines checking if a user is logged in
  - [ ] Write a decorator which checks if the `g.user` object isn't null, and if not flashes and redirects
- [ ] DRY Up URLs
  - [ ] Learn about `url_for()` and implement to reduce repetition in URLs
  - This can let you not use URLLs directly in other routes/templates
  - This will also make it easier if you need to move URLs around
- [ ] Optimize Queries
  - [ ] Use the Flask-DebugToolbar to audit query usage and reduce the total number of queries being performed
- [ ] Add Admins
  - [ ] Add an is_admin field to user model
  - Admins should be able to...
    - [ ] Delete any user's messages
    - [ ] Delete any user
    - [ ] Edit a user profile
    - [ ] Make another user an admin when editing a profile
- [ ] Add 'Private' Accounts
  - [ ] Let users make their accounts private
  - [ ] Private accounts should normally only show the profile page w/o messages
  - [ ] Private accounts can be followed, but the user will need to approve the follow request
  - [ ] After confirming, you should be able to see a private user's messages
- [ ] Block Users
  - [ ] Let users block others
  - [ ] Add a block/unblock button on a user detail page
  - [ ] Blocked users can't view the blocker in any way
- [ ] DMs
  - [ ] Let users send private messages to other users
  - [ ] DMs should only be visible to the sender and recipient
