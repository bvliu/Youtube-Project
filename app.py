from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)

# import youtube-8m
import sys
sys.path.insert(0, 'youtube-8m')

from inference import inference

 
@app.route("/")
def index():
	# video_ids = [] # matrix of 20 random video ids
	# tags = [[]] # matrix of tags

	return "hi"

 #    return render_template('index.html')

@app.route("/hello/<string:name>/")
def hello(name):
	quotes = ["'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
	"'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
	"'To understand recursion you must first understand recursion..' -- Unknown",
	"'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
	"'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
	"'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
	randomNumber = randint(0,len(quotes)-1) 
	quote = quotes[randomNumber]

	# print (name)

	return render_template('test.html', **locals())

@app.route("/train")
def train(name):
	return render_template('test.html', **locals())
 
if __name__ == "__main__":
    app.run()
