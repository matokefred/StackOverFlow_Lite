import unittest
from app import app


class Tdd(unittest.TestCase):
    def test_get_all_questions(self):
        testing = app.test_client(self)
        response = testing.get('/questions', content_type='json')
        self.assertIn(b'All questions', response.data)

    def test_get_a_question(self):
        testing = app.test_client(self)
        response = testing.get('/questions/4', content_type='json')
        self.assertEqual(response.status_code, 400)

    def test_add_question(self):
        testing = app.test_client(self)
        response = testing.post('/questions', content_type='json')
        self.assertEqual(response.status_code, 400)

    def test_add_answer(self):
        testing = app.test_client(self)
        response = testing.post('/questions/2/answers', content_type='json')
        self.assertEqual(response.status_code, 400)

    def test_delete_question(self):
        testing = app.test_client(self)
        response = testing.delete('/questions/1', content_type='json')
        self.assertIn(b'The question has been deleted successfully', response.data)


if __name__ == '__main__':
    unittest.main()
