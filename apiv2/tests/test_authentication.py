'''
Module imports from the base test and tests for user authentication
'''
import json
from .base_test import BaseTest


class TestAuthentication(BaseTest):
    '''
    Actual authentication test suite
    '''
    def test_registration(self):
        '''
        Test for the storage of user info in the database
        '''
        user_register = self.test_client().post('/apiv2/authenticate/registration',
                                       data=json.dumps(self.reg_user), headers={'Content-Type': 'application/json'})
        self.assertEqual(user_register.status_code, 201)
        self.assertIn("Successfully created an account", user_register.data)

    def test_login_user(self):
        '''
        Testing the login authentication
        '''
        self.token = self.get_token()
        user_login = self.test_client().post('/api/v1/auth/login',
                                       data=json.dumps(self.login_user),
                                       headers={'Content-Type': 'application/json'})
        self.jwt = self.split_jwt(user_login.json)
        self.assertEqual(user_login.status_code, 200)