"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase

from models import db, User, Message, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler_test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()
        
        alice = User(email='alice@test.com', username='alice',
                     password='abc123')
        bob = User(email='bob@test.com', username='bob',
                   password='abc123')
        charlie = User(email='charlie@test.com', username='charlie',
                       password='abc123')
        
        db.session.add_all([alice, bob, charlie])
        db.session.commit()
        
        follow1 = Follows(user_being_followed_id=1, user_following_id=2)
        follow2 = Follows(user_being_followed_id=2, user_following_id=1)
        follow3 = Follows(user_being_followed_id=1, user_following_id=3)
        follow4 = Follows(user_being_followed_id=2, user_following_id=3)
        
        db.session.add_all([follow1, follow2, follow3, follow4])
        db.session.commit()
        

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)
        
    def test_getting_user(self):
        alice = User.get(1)
        
        self.assertIsInstance(alice, User)
        self.assertEqual(alice.username, 'alice')
        
    def test_getting_all_users(self):
        users = User.get_all()
        
        self.assertIsInstance(users, list)
        
        for user in users:
            self.assertIsInstance(user, User)
        
    def test_repr(self):
        alice = User.get(1)
        self.assertEqual(repr(alice), '<User #1: alice, alice@test.com>')
        
    def test_is_following(self):
        alice = User.get(1)
        charlie = User.get(3)
        
        self.assertTrue(charlie.is_following(alice))
        self.assertFalse(alice.is_following(charlie))
        
    def test_is_being_followed_by(self):
        alice = User.get(1)
        charlie = User.get(3)
        
        self.assertTrue(alice.is_followed_by(charlie))
        self.assertFalse(charlie.is_followed_by(alice))
        
    def test_successfully_creating_user(self):
        User.signup('deb', 'deb@test.com', 'abc123', User.image_url.default.arg)
        deb = User.get(4)
        
        self.assertIsInstance(deb, User)
        
    def test_unsuccessfully_creating_user(self):
        with self.assertRaises(Exception):
            User.signup('deb', 'deb@test.com', 'abc123')            
        
    def test_successful_authentication(self):
        User.signup('deb', 'deb@test.com', 'abc123', User.image_url.default.arg)
        
        self.assertTrue(User.authenticate('deb', 'abc123'))
        
    def test_unsuccessful_authentication(self):
        User.signup('deb', 'deb@test.com', 'abc123', User.image_url.default.arg)
        
        self.assertFalse(User.authenticate('deb', 'abc1234'))
        self.assertFalse(User.authenticate('debb', 'abc123'))