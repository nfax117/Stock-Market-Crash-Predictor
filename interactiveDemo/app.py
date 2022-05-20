from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, validators, StringField
import os
import sys
import flask_backend

app = Flask(__name__)
app.debug=True
app.secret_key = "super secret key"

#P/E Ratio, Open, Low, High, Volume, and Closing Price

class InputForm(Form):
    day1 = StringField('Day 1', validators=[validators.InputRequired()])
    day2 = StringField('Day 2', validators=[validators.InputRequired()])
    day3 = StringField('Day 3', validators=[validators.InputRequired()])
    day4 = StringField('Day 4', validators=[validators.InputRequired()])
    day5 = StringField('Day 5', validators=[validators.InputRequired()])
    day6 = StringField('Day 6', validators=[validators.InputRequired()])
    day7 = StringField('Day 7', validators=[validators.InputRequired()])
    day8 = StringField('Day 8', validators=[validators.InputRequired()])
    day9 = StringField('Day 9', validators=[validators.InputRequired()])
    day10 = StringField('Day 10', validators=[validators.InputRequired()])
    day11 = StringField('Day 11', validators=[validators.InputRequired()])
    day12 = StringField('Day 12', validators=[validators.InputRequired()])
    day13 = StringField('Day 13', validators=[validators.InputRequired()])
    day14 = StringField('Day 14', validators=[validators.InputRequired()])


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = InputForm()
    # if request.method == 'POST' and form.validate():
        #parse form info and call backend
        # out = flask_backend.run(name)
        # output=str(out)
        # return render_template("outputs/"+output+'.html')
    return render_template('home.html', form = form)

if __name__=='__main__':
    app.run()