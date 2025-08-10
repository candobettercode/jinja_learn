from flask import Flask, jsonify, render_template

# Crete a Flask application instance
app = Flask(__name__)

# crete a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello, World!</h1>"
def index():
    return render_template('index.html')

# localhost:5000/user/<name>
@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)