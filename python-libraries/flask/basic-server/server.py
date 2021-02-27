from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'My first Flask site'

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
