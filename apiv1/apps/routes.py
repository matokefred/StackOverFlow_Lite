'''Define and initialize the routes'''
import os
from flask import Flask, jsonify, make_response
from flask import abort, request
from pytz import unicode
from apps.models import QUESTIONS
from instance.config import APP_CONFIG


def create_app(config_name):
    '''Instantiation and routes'''
    app = Flask(__name__, instance_relative_config=True,
                instance_path=os.environ.get('INSTANCE_PATH'))
    app.config.from_object(APP_CONFIG[config_name])


#  Customize any errors to come back in json and not in HTML

    @app.errorhandler(400)
    def _bad_request(error):
        # pylint: disable=W0612,W0613
        return make_response(jsonify({'error-Definition':
                                          'Bad Request, '
                                          'check if entered parameters are correct'}), 400)

    # Get all the questions present

    @app.route('/apiv1/questions', methods=['GET'])
    def _get_questions():
        return jsonify({'All questions': QUESTIONS})

    # Get a particular question based on their URI

    @app.route('/apiv1/questions/<int:question_id>', methods=['GET'])
    def _get_question(question_id):
        new_qn = [new_qn for new_qn in QUESTIONS if new_qn['question_id'] == question_id]
        # pylint: disable=C1801
        if len(new_qn) == 0:
            abort(400)
        return jsonify({'Requested Question': new_qn[0]})

    # Create a new question

    @app.route('/apiv1/questions', methods=['POST'])
    def _add_question():
        if not request.json or not 'content' in request.json:
            abort(400)
        new_qn = {
            'question_id': QUESTIONS[-1]['question_id'] + 1,
            'category': request.json.get('category', ""),
            'content': request.json['content'],  # Ensuring that the entered question has content
            'answer': request.json.get('answer', "")
        }
        QUESTIONS.append(new_qn)  # Adding the added question to the 'database'
        return jsonify({'You added this question': new_qn}), 201

    # Answer a question

    @app.route('/apiv1/questions/<int:question_id>/answers', methods=['POST'])
    def _add_answer(question_id):
        new_qn = [new_qn for new_qn in QUESTIONS if new_qn['question_id'] == question_id]
        # pylint: disable=C1801
        if len(new_qn) == 0:
            abort(400)
        if not request.json:
            abort(400)
        # pylint: disable=C0123
        if 'category' in request.json and type(request.json['category']) is not unicode:
            abort(400)
        if 'content' in request.json and type(request.json['content']) is not unicode:
            abort(400)
        if 'answer' in request.json and type(request.json['answer']) is not unicode:
            abort(400)
        new_qn[0]['category'] = request.json .get('category', new_qn[0]['category'])
        new_qn[0]['content'] = request.json.get('content', new_qn[0]['content'])
        new_qn[0]['answer'] = request.json.get('answer', new_qn[0]['answer'])
        return jsonify({'You answered this question': new_qn[0]})

    @app.route('/apiv1/questions/<int:question_id>', methods=['DELETE'])
    def _delete_question(question_id):
        new_qn = [new_qn for new_qn in QUESTIONS if new_qn['question_id'] == question_id]
        # pylint: disable=C1801
        if len(new_qn) == 0:
            abort(400)
        QUESTIONS.remove(new_qn[0])
        return jsonify({'success!': 'The question has been deleted successfully'})
    return app
