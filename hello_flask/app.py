from flask import Flask
import MySQLdb
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    for attempt in range(10):
        try:
            db = MySQLdb.connect(
                host="db",  # Docker service name
                user="root",
                passwd="my-secret-pw",
                db="mysql"
            )
            break
        except Exception as e:
            print(f"Attempt {attempt + 1}: MySQL not ready yet... retrying")
            time.sleep(2)
    else:
        return "Could not connect to MySQL after multiple attempts."

    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    return f"Hello, World! MySQL version: {version[0]}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
