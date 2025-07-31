from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/auth', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        un = request.form['username']
        pw = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for i in rows:
            print(i[0])
            if un == i[0]: 
                print(i)
                if pw == i[1]:
                    return redirect(url_for('test'))
                else:
                    error = 'Invalid Credentials. Please try again.'
            else: 
                error = 'Invalid Credentials. Please try again.'
        conn.close()
        return render_template("auth.html", error=error)
    return render_template("auth.html", error=error)

@app.route('/home')
def test():
    return render_template("index.html")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return redirect("/")



if __name__ == '__main__':
     app.run(port=8080, debug=True)

