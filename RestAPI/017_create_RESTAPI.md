To create a REST API using Flask in Python, follow these steps:

-->First we have to Install Flask:
Ensure that you have Flask installed. If not, you can install it using pip:
pip install Flask

Next we have to create a Python file, for example, app.py, and set up a basic Flask application:

from flask import Flask, jsonify, request
app = Flask(__name__)

# Sample data
tasks = [
    {
        'id': 1,
        'title': 'Learn Python',
        'description': 'Learn Python programming language',
        'done': False
    },
    {
        'id': 2,
        'title': 'Build an API',
        'description': 'Build a RESTful API with Flask',
        'done': False
    }
]

# Define routes and corresponding actions
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'The task must have a title'}), 400
    task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)

And finally run the Flask Application by using this code in terminal python app.py
