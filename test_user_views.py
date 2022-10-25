from unittest import TestCase
from app import app
from models import Follows, User, Likes, Message, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///warbler_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['WTF_CSRF_ENABLED'] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class TestUserViews(TestCase):
    def setUp(self):
        Follows.query.delete()
        Likes.query.delete()
        User.query.delete()
        Message.query.delete()
        
        alice = User()
        
    def tearDown(self):
        ...
        
    def test_login(self):
        ...