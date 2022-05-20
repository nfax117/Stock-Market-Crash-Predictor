from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, BooleanField, StringField, validators
import os
import sys
import flask_backend

app = Flask(__name__)
app.debug=True
app.secret_key = "super secret key"

@app.route('/interactiveDemo')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')


class RegisterForm(Form):
    name = StringField('', [validators.Length(min=1, max=500)], render_kw={"placeholder": "Please Enter a statement here"})



# connect and run the python backend
@app.route('/code', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        

        # call the run function from the imported python file
        out = imdb_classifer.run(name)
        output=str(out)

        return render_template("outputs/"+output+'.html')
    return render_template('code.html', form=form)


if __name__=='__main__':
    app.run()