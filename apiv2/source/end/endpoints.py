from flask import Blueprint, jsonify
from flask_jwt import jwt_required

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
