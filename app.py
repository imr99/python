# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Goor morning, Simplyfi Soft Tech pvt ltd .Thanks for the Opportunity!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
