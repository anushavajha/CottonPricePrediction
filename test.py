from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)
@app.route('/home')
@app.route('/')
def index():
    return render_template('signup.html')
if __name__ == "__main__":
    app.run(debug=True)
