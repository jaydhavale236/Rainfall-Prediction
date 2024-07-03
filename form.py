from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set a secret key for CSRF protection


class MyForm(FlaskForm):
    day = IntegerField('day', validators=[DataRequired(), Length(min=1, max=20)])
    pressure = FloatField('pressure', validators=[DataRequired(), Length(min=1, max=20)])
    maxtemp = FloatField('maxtemp', validators=[DataRequired(), Length(min=1, max=20)])
    temparature = FloatField('temparature', validators=[DataRequired(), Length(min=1, max=20)])
    mintemp = FloatField('mintemp', validators=[DataRequired(), Length(min=1, max=20)])
    dewpoint = FloatField('dewpoint', validators=[DataRequired(), Length(min=1, max=20)])
    humidity = IntegerField('humidity', validators=[DataRequired(), Length(min=1, max=20)])
    cloud = IntegerField('cloud', validators=[DataRequired(), Length(min=1, max=20)])
    sunshine = FloatField('sunshine', validators=[DataRequired(), Length(min=1, max=20)])
    winddirection = IntegerField('winddirection', validators=[DataRequired(), Length(min=1, max=20)])
    windspeed = FloatField('windspeed', validators=[DataRequired(), Length(min=1, max=20)])


    submit = SubmitField('submit')

@app.route('/', methods=['POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        flash(f'Hello, {form.name.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('new.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)