from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)
 
@app.route("/")
def index():
    return "FlaskApp!"

@app.route("/hello/<string:name>/")
def hello(name):
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
               "'To understand recursion you must first understand recursion..' -- Unknown",
               "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
               "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = randint(0, len(quotes)-1)
    quote = quotes[randomNumber]

    return render_template('test.html', **locals())
 
#make sure to set host='0.0.0.0'. This tells the app to accept requests from any host
if __name__ == "__main__":
    use_c9_debugger = False
    app.run(use_debugger=not use_c9_debugger, debug=True,
                    use_reloader=not use_c9_debugger, host='0.0.0.0', port=8080)

