from flask import Flask, jsonify, make_response

app = Flask(__name__)

questions = [
    {
        'uri': 1,
        'category': 'Programming',
        'content': 'What is polymorphism?',
        'answer': 'The ability of a single method or feature to take up different upon being called'
    },
    {
        'uri': 2,
        'category': 'Networks',
        'content': 'What is the difference bewteen a router and switch?',
        'answer': 'A router is a layer3 (packets) device and a switch is a layer2 (frames)'
    },
    {
        'uri': 3,
        'category': 'Machine learning',
        'content': 'What is a neural net?',
        'answer': ''
    }
]

#  Customize any errors to come back in json and not in HTML


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error-Definition': 'Bad Request, check if entered parameters are correct'}), 400)

# Get all the questions present


@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify({'All questions': questions})


if __name__ == '__main__':
    app.run(debug=True)