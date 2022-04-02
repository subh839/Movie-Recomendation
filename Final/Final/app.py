from flask import Flask,render_template
app=Flask(__name__)

@app.route("/recomend")

def recomend():
    return render_template('recomend.py')
