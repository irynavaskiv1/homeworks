from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route(
    '/home/iryna/Documents/Projects/homeworks/Classwork/class_work_9.py')
@app.route(
    '/home/iryna/Documents/Projects/homeworks/Classwork/class_work_9.py')
def class_work_9(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath(subpath)
