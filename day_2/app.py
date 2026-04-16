

from flask import Flask
# initialize the Flask application
app = Flask(__name__)

@app.route('/home')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)