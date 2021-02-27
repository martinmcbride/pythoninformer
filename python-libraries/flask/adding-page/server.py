from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home page',
                           content='My first Flask site')

@app.route('/about')
def about():
    return render_template('index.html', title='About',
                           content='This is the About page')

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
