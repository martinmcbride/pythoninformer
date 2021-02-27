from flask import Flask, render_template
import platform
import sys
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home page',
                           content='My first Flask site')

@app.route('/about')
def about():
    return render_template('index.html', title='About',
                           content='This is the About page')

@app.route('/status')
def status():
    dt = str(datetime.datetime.now())
    os = platform.system()
    pyver = sys.version
    return render_template('status.html',
                           title='Status',
                           date=dt,
                           operating_system=os,
                           python_version=pyver)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
