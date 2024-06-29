from flask import Blueprint, render_template

tasks_bp = Blueprint('tasks_bp', __name__)

@tasks_bp.route('/tasks')
def tasks():
    return render_template('tasks.html')
