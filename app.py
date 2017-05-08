from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint, sample, choice
from labels import run_inference

app = Flask(__name__)

@app.route("/")
def index():
	data = run_inference()
	display = sample(list(data), 5)
	result = {}
	for key in display:
		result[key] = data[key]
	return render_template('index.html', data=result)

if __name__ == "__main__":
    app.run()
