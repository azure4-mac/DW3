from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Entrar")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        return redirect(url_for("home")) 
    return render_template("login.html", form=form)


@app.route("/empresa")
def empresa():
    return "Seja bem-vindo ao sistema de empresa!"

@app.route("/trabalhe-conosco")
def trabalhe_conosco():
    return "Seja bem-vindo ao sistema de trabalhe conosco!"

@app.route("/contatos")
def contatos():
    return "Seja bem-vindo ao sistema de contatos!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
