import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from werkzeug.security import generate_password_hash
from ..models.users import User

class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config=config_dict['test'])
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

        db.create_all()

    def tearDown(self):
        db.drop_all()

        self.appctx.pop()
        self.app = None
        self.client = None

    def test_user_registeration(self):
        data = {
            "username":"testUser",
            "email":"test@mail.com",
            "password":generate_password_hash('password')
        }
        response = self.client.post('/auth/signup', json=data)

        assert response.status_code == 201

        user = User.query.filter_by(email="test@mail.com").first()
        assert user.username == "testUser"

    def test_user_login(self):
        data = {
            "email":"test@mail.com",
            "password":generate_password_hash('password')
        }

        response = self.client.post('/auth/login', json=data)

        assert response.status_code == 200