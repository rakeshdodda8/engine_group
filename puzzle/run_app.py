import os
from flask import send_file
from flask import Blueprint
from puzzle.settings import RESUME_FILE_NAME

ra = Blueprint("run_app", __name__)

@ra.route('/engine_group', methods = ['GET'])
def eng_grp():
    qs = request.args.get('q')
    data = {
        'Ping': 'OK',
        'Years': '8+ years',
        'Email Address': 'mail8rakesh@gmail.com',
        'Referrer': 'linkedin',
        'Name': 'Rakesh Dodda',
        'Degree': 'Masters of Science in Computer Science',
        'Phone': '732-742-9108',
        'Position': 'Software Engineer',
        'Puzzle': 'ABCD\nA=><>\nB<=<>\nC>>=>\nD<<<=',
        'Resume': 'OK',
        'Source': 'git@github.com:rakeshdodda8/engine_group.git',
        'Status': 'Yes'
    }

    if qs in data:
        return data[qs], 200

@ra.route("/engine_group/download/resume", methods = ['GET'])
def download_resume():
    path = '{}/{}'.format(os.path.dirname(os.path.abspath(__file__)), RESUME_FILE_NAME)
    try:
        return send_file(path, as_attachment=True)
    except Exception as e:
        return "error downloading resume", 200