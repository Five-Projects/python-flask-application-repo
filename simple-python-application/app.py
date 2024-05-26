from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! This is an AWS CICD Pipeline to deploy a Python Flask application.'

if __name__ == '__main__':
    app.run()

