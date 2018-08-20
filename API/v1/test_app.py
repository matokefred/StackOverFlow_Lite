import unittest
from apps.routes import create_app


class Tdd(unittest.TestCase):
    def setUp(self):
        self.app = create_app(
            config_name="testing")
        self.client = self.app.test_client

    def test_get_all_questions(self):
        response = self.client().get('/API/v1/questions', content_type='json')
        self.assertIn(b'All questions', response.data)

    def test_get_a_question(self):
        response = self.client().get('/API/v1/questions/4', content_type='json')
        self.assertEqual(response.status_code, 400)

    def test_add_question(self):
        response = self.client().post('/API/v1/questions', content_type='json')
        self.assertEqual(response.status_code, 400)

    def test_add_answer(self):
        response = self.client().post('/API/v1/questions/2/answers', content_type='json')
        self.assertEqual(response.status_code, 400)

    def test_delete_question(self):
        response = self.client().delete('/API/v1/questions/1', content_type='json')
        self.assertIn(b'The question has been deleted successfully', response.data)


if __name__ == '__main__':
    unittest.main()
