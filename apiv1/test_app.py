#! The test class for the routes to make sure they return what is required
'''Good practise in test driven development'''

import unittest
from apps.routes import create_app
# import json


class Tdd(unittest.TestCase):
    '''This class helps in setting up the test suite that will contain the test cases'''
    def setUp(self):
        self.app = create_app(
            config_name="testing")
        self.client = self.app.test_client
        self.question = {'id': 1, 'content': ''}

    def test_get_all_questions(self):
        '''A test on the get_questions method'''
        response = self.client().get('/apiv1/questions', content_type='json')
        self.assertIn(b'All questions', response.data)

    def test_get_a_question(self):
        '''A test on get_question Method'''
        response = self.client().get('/apiv1/questions/4', content_type='json')
        self.assertEqual(response.status_code, 400)

    def test_add_question(self):
        '''Testing the add_question method'''
        response = self.client().post('/apiv1/questions', content_type='json')
        self.assertEqual(response.status_code, 400)

    def test_add_answer(self):
        '''Test add_answer method'''
        response = self.client().post('/apiv1/questions/2/answers', content_type='json')
        self.assertEqual(response.status_code, 400)

    def test_delete_question(self):
        '''Test the delete functionality'''
        response = self.client().delete('/apiv1/questions/1', content_type='json')
        self.assertIn(b'The question has been deleted successfully', response.data)


if __name__ == '__main__':
    unittest.main()
