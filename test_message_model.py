"""User model tests."""

import os
from unittest import TestCase
from models import db, User, Message, Follows, Likes
from app import app

os.environ['DATABASE_URL'] = "postgresql:///warbler_test"

db.create_all()

class Test_Messages_Model(TestCase):
    def setUp(self):
        ...
        
    def tearDown(self):
        db.session.rollback()
        
    # def test_