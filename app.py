from flask import Flask, render_template_string
import redis
import os

app = Flask(__name__)

r = redis.Redis(
    host=os.environ.get('REDIS_HOST', 'redis'),
    port=int(os.environ.get('REDIS_PORT', 6379))
)

WELCOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding-top: 100px; background-color: #f4f4f4; }
        h1 { font-size: 48px; color: #333; }
    </style>
</head>
<body>
    <h1>Welcome to the Coderco Containers Challenge 🎉</h1>
</body>
</html>
"""

COUNT_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Visitor Counter</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding-top: 100px; background-color: #f4f4f4; }
        h1 { font-size: 48px; color: #333; }
        p { font-size: 24px; color: #666; }
    </style>
</head>
<body>
    <h1>🚀 Page Visit Counter</h1>
    <p>This page has been visited <strong>{{ count }}</strong> times.</p>
</body>
</html>
"""

@app.route('/')
def welcome():
    return render_template_string(WELCOME_HTML)

@app.route('/count')
def count():
    visit_count = r.incr('visits')
    return render_template_string(COUNT_HTML, count=visit_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
