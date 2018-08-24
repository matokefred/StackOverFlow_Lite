from unittest import TestCase
import json
from source import APP
from source.models.models import DatabaseTables


class BaseTest(TestCase):
    '''
    Instantiate the test suite
    '''
    def setUp(self):
        self.test = DatabaseTables()
        self.test.create_all()
        self.source = APP
        self.test_client = self.app.test_client
        self.question = {
            "body": "What is neural networks"
        }
        self.answer = {
            "answer_body": "Giving the computer power to think and make decisions like humans"
        }
        self.registration = {
            "username": "matoke24",
            "email": "matoke24@gmail.com",
            "password": "matoke.git"

        }
        self.login = {
            "username": "matoke24",
            "password": "matoke.git"
        }
        self.token = ''

    def gettoken(self):
        '''
        New authentication for the tests
        '''
        user_register = self.test_client().post('/apiv2/authenticate/registration',
                                       data=json.dumps(self.user_registration), headers={'Content-Type': 'application/json'})
        login_user = self.test_client().post('/apiv2/authenticate/login',
                                       data=json.dumps(self.user_login), headers={'Content-Type': 'application/json'})
        self.token = self.split_jwt(user_register.json, login_user.json)
        return self.token

    def split_jwt(self, jwt):
        '''
        split tokens from any entered string
        '''
        jwt = json.dumps(jwt)
        null, jwt = jwt.split(' "')
        jwt, null = jwt.split('"}')
        return jwt

    def tearDown(self):
        '''
        Delete the database after all the tests are complete
        '''
        self.test.drop_all()
