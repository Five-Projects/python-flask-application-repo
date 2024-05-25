from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! This is a simple Python Flask application.'

if __name__ == '__main__':
    app.run()

