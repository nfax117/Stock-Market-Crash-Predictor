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
    day1 = StringField('Enter Data for 09/20/2021:', validators=[validators.InputRequired()])

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
    return render_template('home.html')

@app.route('/mulBigInput', methods = ['GET', 'POST'])
def mulBigInput():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        app.logger.info("in post")
        day1 = makeFloatList(form.day1.data)
        out = flask_backend.runMul(day1)
        result=str(out)
    else:
        app.logger.info('in else')
        result = None
    return render_template('mulBIGInput.html', form = form, result = result)
@app.route('/mulBigNoInput', methods = ['GET', 'POST'])
def mulBigNoInput():
    if request.method == 'POST':
        out = flask_backend.runMul(None)
        result=str(out)
    else:
        result = None
    return render_template('mulBIGNoInput.html', result = result)

@app.route('/uniBigInput', methods = ['GET', 'POST'])
def uniBigInput():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        app.logger.info("in post")
        day1 = [float(form.day1.data)]
        out = flask_backend.runUni(day1)
        result=str(out)
    else:
        app.logger.info('in else')
        result = None
    return render_template('uniBIGInput.html', form = form, result = result)
@app.route('/uniBigNoInput', methods = ['GET', 'POST'])
def uniBigNoInput():
    if request.method == 'POST':
        out = flask_backend.runUni(None)
        result=str(out)
    else:
        result = None
    return render_template('uniBIGNoInput.html', result = result)
if __name__=='__main__':
    app.run()