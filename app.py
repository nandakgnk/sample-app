from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
