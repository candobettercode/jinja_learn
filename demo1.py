from flask import Flask, jsonify, render_template

# Crete a Flask application instance
app = Flask(__name__)

# crete a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello, World!</h1>"
def index():
    f_name = "John"
    l_name = "Doe"
    stuff = "This is bold text"
    fruits = ["Apple", "Banana", "Cherry"]
    return render_template('index.html', first_name=f_name, last_name=l_name, stuff=stuff, fruits=fruits)

# localhost:5000/user/<name>
@app.route('/user/<name>')
def user(name):
    # return f"<h1>Hello, {name}!</h1>"
    return render_template('user.html', user_name=name)

# create custome error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)