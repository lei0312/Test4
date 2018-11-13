from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return 'hello Lei New VerSion 999'

if __name__ == '__main__':
    app.run()