from flask import Blueprint, abort, request, jsonify
from datetime import datetime as dt
from flask_jwt import jwt_required, current_identity

from source.app import CONNECT

PRINTS = Blueprint('source', __name__, url_prefix='/source/end')


@PRINTS.route('/apiv2/questions', methods= ['GET'])
@jwt_required
def get_all_questions():
    cursor = CONNECT.cursor()
    cursor.execute('SELECT * FROM questions;')
    question = cursor.fetchall()
    cursor.close()
    output = []
    for qn in question:
        appear = {
            "question_id": qn[0],
            "body": qn[1],
            "user_id": qn[2]
        }
        output.append(appear)
        return jsonify({"All Questions": output})


@PRINTS.route('/apiv2/questions/<int:question_id>', methods=['GET'])
@jwt_required
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
    return abort(404)
