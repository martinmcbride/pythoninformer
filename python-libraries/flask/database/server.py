from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home page',
                           content='My first Flask site')

@app.route('/fruits')
def fruits():
    con = sqlite3.connect('data.db')
    cur = con.cursor()    
    cur.execute("SELECT * FROM fruits")
    rows = cur.fetchall()

    return render_template('fruits.html', title='Fruits list',
                           rows=rows)


@app.route('/fruit/<name>')
def fruit(name):
    con = sqlite3.connect('data.db')
    cur = con.cursor()    
    cur.execute("SELECT * FROM fruits where name = ?", (name,))
    rows = cur.fetchall()
    name = rows[0][0]
    color = rows[0][1]
    image = rows[0][2]

    return render_template('fruit.html', name=name,
                           color=color, image=image)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
