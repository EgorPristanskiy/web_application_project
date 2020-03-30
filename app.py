from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)
application = app


@app.route('/hello')
def hello_world():
    return os.path.join(app.root_path, 'static')


def check_email(email):
    arguments_by_dog = email.split("@")
    if len(arguments_by_dog) == 2:
        arguments_by_point = email.split('.')
        if len(arguments_by_point) == 2:
            return True
    return False


@app.route('/', methods=['POST'])
def form_manager():
    email_address = request.form["email"]
    password = request.form["password"]
    if check_email(email_address) and len(password) > 6:
        print(email_address, password)
        return render_template("login_page.html")
    return render_template("login.html")


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'image.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8003')
