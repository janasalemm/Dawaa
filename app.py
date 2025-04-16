from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("dawaa.db")
    db = conn.cursor()
    db.execute("""
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            times_per_day INTEGER NOT NULL,
            times TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    conn = sqlite3.connect("dawaa.db")
    db = conn.cursor()
    db.execute("SELECT * FROM medicines")
    medicines = db.fetchall()
    conn.close()
    return render_template("index.html", medicines=medicines)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        times_per_day = request.form.get("times_per_day")
        times = request.form.get("times")
        conn = sqlite3.connect("dawaa.db")
        db = conn.cursor()
        db.execute("INSERT INTO medicines (name, times_per_day, times) VALUES (?, ?, ?)",
                   (name, times_per_day, times))
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
