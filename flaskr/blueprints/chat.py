import os
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import flaskr.openaiapi as op

bp = Blueprint('chat', __name__, url_prefix='')

@bp.route('/', methods=('POST', 'GET'))
def index():
    if request.method == 'POST':
        input = request.get_json()['question']
        answ = op.completion(input)
        return jsonify({'answer': answ['choices'][0]['message']['content']})
    return render_template('chat/index.html', system=op.messages[0]["content"])

@bp.route('/clear', methods=['GET'])
def clear():
    op.clear()
    return redirect(url_for('chat.index'))

@bp.route('/change_system', methods=['POST'])
def change_system():
    new_system = request.get_json()['system']
    op.define_system(new_system)
    return jsonify({})

