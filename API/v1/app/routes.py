import os
from flask import Flask, jsonify, make_response
from flask import abort, request
from app.models import questions
from instance.config import APP_CONFIG


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True,
                instance_path=os.environ.get('INSTANCE_PATH'))
    app.config.from_object(APP_CONFIG[config_name])


#  Customize any errors to come back in json and not in HTML

    @app.errorhandler(400)
    def bad_request(error):
        return make_response(jsonify({'error-Definition': 'Bad Request, check if entered parameters are correct'}), 400)

    # Get all the questions present

    @app.route('/questions', methods=['GET'])
    def get_questions():
        return jsonify({'All questions': questions})

    # Get a particular question based on their URI

    @app.route('/questions/<int:uri>', methods=['GET'])
    def get_question(uri):
        qn = [qn for qn in questions if qn['uri'] == uri]
        if len(qn) == 0:
            abort(400)
        return jsonify({'Requested Question': qn[0]})

    # Create a new question

    @app.route('/questions', methods=['POST'])
    def add_question():
        if not request.json or not 'category' in request.json:
            abort(400)
        if not request.json or not 'content' in request.json:
            abort(400)
        qn = {
            'uri': questions[-1]['uri'] + 1,
            'category': request.json['category'],  # Ensuring that the entered question has a category
            'content': request.json['content'],  # Ensuring that the entered question has content
            'answer': request.json.get('answer', "")
        }
        questions.append(qn)  # Adding the added question to the 'database'
        return jsonify({'You added this question': qn})

    # Answer a question

    @app.route('/questions/<int:uri>/answers', methods=['POST'])
    def add_answer(uri):
        qn = [qn for qn in questions if qn['uri'] == uri]
        if len(qn) == 0:
            abort(400)
        if not request.json:
            abort(400)
        if 'category' in request.json and type(request.json['category']) is not unicode:
            abort(400)
        if 'content' in request.json and type(request.json['content']) is not unicode:
            abort(400)
        if 'answer' in request.json and type(request.json['answer']) is not unicode:
            abort(400)
        qn[0]['category'] = request.json .get('category', qn[0]['category'])
        qn[0]['content'] = request.json.get('content', qn[0]['content'])
        qn[0]['answer'] = request.json.get('answer', qn[0]['answer'])
        return jsonify({'You answered this question': qn[0]})

    @app.route('/questions/<int:uri>', methods=['DELETE'])
    def delete_question(uri):
        qn = [qn for qn in questions if qn['uri'] == uri]
        if len(qn) == 0:
            abort(400)
        questions.remove(qn[0])
        return jsonify({'success!': 'The question has been deleted successfully'})
    return app
