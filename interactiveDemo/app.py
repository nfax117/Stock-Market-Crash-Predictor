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

def makeFloatList(day):
    #remove any white space
    day.strip()

    #split into a list by commas
    day = day.split(",")
    app.logger.info(day)
    
    #convert to a list of floats
    float_days = [float(i) for i in day]
    return float_days
@app.route('/', methods = ['GET', 'POST'])
def index():
    form = InputForm(request.form)
    app.logger.info('index')
    if request.method == 'POST' and form.validate():
        app.logger.info("in post")
        all_days = []
        day1 = makeFloatList(form.day1.data)
        all_days.append(day1)
        day2 = makeFloatList(form.day2.data)
        all_days.append(day2)
        day3 = makeFloatList(form.day3.data)
        all_days.append(day3)
        day4 = makeFloatList(form.day4.data)
        all_days.append(day4)
        day5 = makeFloatList(form.day5.data)
        all_days.append(day5)
        day6 = makeFloatList(form.day6.data)
        all_days.append(day6)
        day7 = makeFloatList(form.day7.data)
        all_days.append(day7)
        day8 = makeFloatList(form.day8.data)
        all_days.append(day8)
        day9 = makeFloatList(form.day9.data)
        all_days.append(day9)
        day10 = makeFloatList(form.day10.data)
        all_days.append(day10)
        day11 = makeFloatList(form.day11.data)
        all_days.append(day11)
        day12 = makeFloatList(form.day12.data)
        all_days.append(day12)
        day13 = makeFloatList(form.day13.data)
        all_days.append(day13)
        day14 = makeFloatList(form.day14.data)
        all_days.append(day14)

        out = flask_backend.run(all_days)
        result=str(out)
    else:
        app.logger.info('in else')
        result = None
    return render_template('home.html', form = form, result = result)

if __name__=='__main__':
    app.run()