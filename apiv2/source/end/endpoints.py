from flask import Blueprint, abort, request, jsonify
from flask_jwt import jwt_required, current_identity

from source import CONNECT

PRINTS = Blueprint('source', __name__, url_prefix='/source/end')


@PRINTS.route('/apiv2/questions', methods=['GET'])
@jwt_required()
def get_all_questions():
    cursor = CONNECT.cursor()
    cursor.execute('SELECT * FROM questions;')
    question = cursor.fetchall()
    cursor.close()
    output = []
    for qn in question:
        appear = {
            "question_id": qn[0],
            "User_id": qn[1],
            "body": qn[2]
        }
        output.append(appear)
        return jsonify({"All Questions": output})


@PRINTS.route('/apiv2/questions/<int:question_id>', methods=['GET'])
@jwt_required()
def get_one_question(question_id):
    output = []
    cursor = CONNECT.cursor()
    sqlcode = 'SELECT * FROM questions WHERE questionId=%s;'
    cursor.execute(sqlcode, ([question_id]))
    question = cursor.fetchall()
    cursor.close()

    if question:
        cursor = CONNECT.cursor()
        sqlcode = 'SELECT * FROM answers WHERE questionId=%s;'
        cursor.execute(sqlcode([question_id]))
        answrs = cursor.fetchall()
        output_answrs = []
        for answr in answrs:
            answr = list(answr)
            answrs_format = {
                "Answer Id": answr[0],
                "QuestionId": answr[1],
                "Answer": answr[2],
                "User": answr[3],
                "Upvotes": answr[4],
                "Downvotes": answr[5],
                "Status": answr[6],
                "Comments": answr[7]
            }
            output_answrs.append(answrs_format)
        output = [{
            "Question Id": question[0],
            "Body": question[1],
            "User": question[2],
            "Answers": output_answrs
        }]
        cursor.close()
        return jsonify(output)
    else:
        return abort(404)


@PRINTS.route('/apiv2/questions', methods=['POST'])
@jwt_required()
def post_question():
    if request.json and request.json['body']:
        cursor = CONNECT.cursor()
        sqlcode = 'INSERT INTO questions(userId, body) VALUES (%s, %s);'
        cursor.execute(sqlcode, (int(current_identity), request.json['body']))
        CONNECT.commit()
        cursor.close()
        return jsonify({"Success!": "Your question has been recorded"})
    else:
        return abort(400)


@PRINTS.route('/apiv2/questions/<int:question_id>', methods=['POST'])
@jwt_required()
def answer_question(question_id):
    cursor = CONNECT.cursor()
    sqlcode = 'SELECT * FROM questions WHERE questionId=%s;'
    cursor.execute(sqlcode, ([question_id]))
    qn = cursor.fetchall()
    if qn:
        if request.json and request.json['answer']:
            sqlcode = 'INSERT INTO ANSWERS(userId, answer, questionId) VALUES (%s, %s, %s);'
            cursor.execute(sqlcode, (int(current_identity), request.json['answer'], question_id))
            CONNECT.commit()
            cursor.close
            return jsonify({"Congratulations": "Answer received"})
        else:
            return abort(400)
    else:
        return abort(404)


@PRINTS.route('/apiv1/questions/<int: question_id>', methods=['DELETE'])
@jwt_required()
def delete_question(question_id):
    cursor = CONNECT.cursor()
    sqlcode = 'SELECT * FROM questions WHERE questionId=%s;'
    cursor.execute(sqlcode, ([question_id]))
    qn = cursor.fetchall()
    if qn:
        if int(current_identity)is qn[0][1]:
            sqlcode = 'DELETE FROM answers WHERE questionId=%s;'
            cursor.execute(sqlcode, ([question_id]))
            sqlcode = 'DELETE FROM questions WHERE questionId=%s;'
            cursor.execute(sqlcode, ([question_id]))
            cursor.close()
            CONNECT.commit()
            return jsonify({"200": "The question has been deleted!"})
        else:
            return jsonify({"403":"That action is not allowed"})
    else:
        return abort(404)


@PRINTS.route('apiv2/upvote/<int: answer_id>', methods=['POST'])
@jwt_required()
def upvote_answer(answer_id):
    cursor = CONNECT.cursor()
    sqlcode = 'SELECT * FROM answers WHERE answerId=%s;'
    cursor.execute(sqlcode, ([int(answer_id)]))
    answr = cursor.fetchall()
    print(answr)
    if answr:
        print('Here')
        sqlcode = 'SELECT * FROM votes WHERE voteId=%s AND voter=%s;'
        cursor.execute(sqlcode, (int(answr[0][0]), int(current_identity)))
        voting = cursor.fetchall()
        print(voting)
        if not voting:
            sqlcode = 'UPDATE answers SET upvotes = upvotes + 1 WHERE answerId=%s;'
            cursor.execute(sqlcode, ([answer_id]))
            CONNECT.commit()
            cursor.close()
            return jsonify({"OK": "Your vote has been recorded"})
        else:
            return jsonify({"403": "You are only allowed to vote once"})
    else:
        return abort(404)


@PRINTS.route('/api/downvote/<int:answer_id>', methods=['POST'])
@jwt_required()
def downvote_answer(answer_id):
    cursor = CONNECT.cursor()
    sqlcode = 'SELECT * FROM answers WHERE answerId=%s;'
    cursor.execute(sqlcode, ([int(answer_id)]))
    answr = cursor.fetchall()
    print(answr)
    if answr:
        print('here')
        sqlcode = 'SELECT * FROM votes WHERE voteId=%s AND voter=%s;'
        cursor.execute(sqlcode, (answer_id, int(current_identity)))
        voting = cursor.fetchall()
        print(voting)
        if not voting:
            sqlcode = 'UPDATE answers SET downvotes = downvotes + 1 WHERE answerId=%s;'
            cursor.execute(sqlcode, ([answer_id]))
            CONNECT.commit()
            cursor.close()
            return jsonify({"200": "Your vote has been recorded"})
        else:
            return jsonify({"403": "You are only allowed to vote once"})
    else:
        return abort(404)


@PRINTS.route('apiv1/state/<int:answer_id>', methods=['POST'])
@jwt_required()
def answer_state(answer_id):
    '''
    Changing the state of answer
    '''
    cursor = CONNECT.cursor()
    sqlcode = 'SELECT * FROM answers WHERE answerId=%s;'
    cursor.execute(sqlcode, ([int(answer_id)]))
    answr = cursor.fetchall()
    if answr:
        sqlcode = 'SELECT * FROM questions WHERE questionid=%s AND userId=%s;'
        cursor.execute(sqlcode, (int(answr[0][1]), int(current_identity)))
        qn = cursor.fetchall()
        if qn:
            sqlcode = 'SELECT * FROM answers WHERE questionId=%s AND state=TRUE'
            cursor.execute(sqlcode, ([int(answr[0][6])]))
            status = cursor.fetchall()
            if not status:
                sqlcode = 'UPDATE answers SET state = TRUE WHERE answerId=%s;'
                cursor.execute(sqlcode, ([answr[0][0]]))
                CONNECT.commit()
                return jsonify({"200": "Status changed to True"})
            else:
                return jsonify({"403": "Only one answer can be accepted per question"})
        else:
            return jsonify({"403": "Only the owner of the question has that access"})
    else:
        return abort(404)


@PRINTS.route('apiv2/update/<int:question_id>/<int:answer_id>', methods=['POST'])
@jwt_required()
def improve_answer(question_id, answer_id):
    '''
    Define the specific question
    '''
    if request.json and request.json['body']:
        improve = request.json['body']
        cursor = CONNECT.cursor()
        sqlcode = 'SELECT * FROM answers WHERE answerId=%s AND questionId=%s;'
        cursor.execute(sqlcode, (answer_id, question_id))
        answr = cursor.fetchall()
        if answr:
            if answr[0][2] == int(current_identity):
                sqlcode = 'UPDATE answers SET answer = %s WHERE answerId=%s AND questionId=%s;'
                cursor.execute(sqlcode, (improve, answer_id, question_id))
                CONNECT.commit()
                cursor.close()
                return jsonify({"200": "You updated the answer"})
            else:
                return jsonify({"403": "Only the owner of the answer can update the answer"})
        else:
            return abort(404)
    else:
        return abort(400)
