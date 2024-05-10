from flask import Flask

app = Flask(__name__)

@app.route('/power/<int:x>/<int:y>')
def power(x, y):
    result = x ** y
    return result

if __name__ == "__main__":
    app.run()