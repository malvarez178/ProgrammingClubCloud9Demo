from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'This_is_my_secret_key'

app.config['MYSQL_HOST'] = 'database-1.csf1wtezlwz9.us-west-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'crud2'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

@app.route('/')
def Index():
    cursor = mysql.connection.cursor()
    cursor.execute('select * from students')
    data = cursor.fetchall()
    return render_template("index.html", students = data)
   #return 'Hello world!'

#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        flash("Added Student Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cursor = mysql.connection.cursor()
        cursor.execute('insert into students (name, email, phone) values (%s, %s, %s)' , (name,email,phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))

#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        student_id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cursor = mysql.connection.cursor()
        cursor.execute(""" 
            update students
            set name=%s, email=%s, phone=%s 
            where id=%s """, (name,email,phone,student_id))
        flash("Student Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:student_id>', methods = ['GET'])
def delete(student_id):
    flash("Record Has Been Deleted Successfully")
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8080, debug=True)
