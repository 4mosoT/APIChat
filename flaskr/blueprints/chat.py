import os
from flask import Blueprint, render_template, send_from_directory, current_app, request, jsonify
import flaskr.openaiapi as op

bp = Blueprint('chat', __name__, url_prefix='')

@bp.route('/', methods=('POST', 'GET'))
def index():
    if request.method == 'POST':
        input = request.get_json()['question']
        answ = op.completion(input)
        return jsonify({'answer': answ['choices'][0]['message']['content']})
    return render_template('chat/index.html')
