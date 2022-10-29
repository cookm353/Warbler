from unittest import TestCase
from app import CURR_USER_KEY, app
import bcrypt
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

        alice = User(username='Alice89', password='qwerty',
                     email='alice@gmail.com', bio = 'Foo')
        bob = User(username='BobB', password='1234',
                   email='bboy@gmail.com', bio='Bar')

        db.session.add_all([alice, bob])
        db.session.commit()


    def tearDown(self):
        db.session.rollback()

    def test_landing_page(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('New to Warbler?', html)
            
    def test_registration_form(self):
        with app.test_client() as client:
            resp = client.get('/signup')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Join Warbler today.', html)
            
    def test_registering(self):
        with app.test_client() as client:
            data = {'username': 'Carlos', 'password': 'qwerty',
                    'email': 'cslim@gmail.com'}
            resp = client.post('/signup', data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('New Message', html)
            
    def test_registering_with_used_name(self):
        with app.test_client() as client:
            data = {'username': 'Alice89', 'password': 'qwerty',
                    'email': 'alice@gmail.com'}
            resp = client.post('/signup', data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Username already taken', html)
            
    def test_login_form_display(self):
        with app.test_client() as client:
            resp = client.get('/login')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Welcome back', html)
            
    def test_valid_login(self):
        with self.client as client:
            with client.session_transaction() as session:
                # sessin[CURR_USER_KEY] = 
                ...
        
        with app.test_client() as client:
            data = {'username': 'Alice89', 
                    'password': 'qwerty'}
            resp = client.post('/login', data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('@Alice', html)
            
    def test_invalid_login(self):
        with app.test_client() as client:
            data = {'username': 'Foobar', 'password': 'qwerty'}
            resp = client.post('/login', data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Invalid credentials', html)
            
    def test_users_page_logged_out(self):
        with app.test_client() as client:
            resp = client.get('/users')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn("@Alice89", html)
            self.assertNotIn('Follow', html)
        
    def test_users_page_logged_in(self):
        with app.test_client() as client:
            # Log in and then test
            
            resp = client.get('/users')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Follow', html)
            
    def test_deleting_user(self):
        with app.test_client() as client:
            # Log user in
            
            resp = client.post('/users/delete')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)