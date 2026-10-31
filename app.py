from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Create database and student table
def create_table():
    con = sqlite3.connect("student.db")
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            rollno INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            year INTEGER
        )
    """)

    cur.execute("""
        INSERT OR IGNORE INTO students
        VALUES (41, 'Sushmitha', 'CSE', 3)
    """)

    con.commit()
    con.close()


# Retrieve student information
@app.route("/")
def student():
    con = sqlite3.connect("student.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM students WHERE rollno = ?", (41,))
    data = cur.fetchone()

    con.close()

    return render_template("student.html", student=data)


if __name__ == "__main__":
    create_table()
    app.run(debug=True)