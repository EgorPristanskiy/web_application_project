from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from skimage import io
import os

app = Flask(__name__)
application = app
IMAGE_FILENAME = None
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/hello')
def hello():
    return url_for("hello")


@app.route('/image_processing')
def image_processing():
    print(IMAGE_FILENAME)
    return render_template("image_processing.html", image_name=IMAGE_FILENAME)


@app.route('/image_processing', methods=['POST'])
def upload():
    global IMAGE_FILENAME
    '''
    # this is to verify that folder to upload to exists.
    if os.path.isdir(os.path.join(APP_ROOT, 'files/{}'.format(folder_name))):
        print("folder exist")
    '''
    target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        # This is to verify files are supported
        ext = os.path.splitext(filename)[1]
        if (ext == ".jpg") or (ext == ".png"):
            print("File supported moving on...")
        else:
            render_template("Error.html", message="Files uploaded are not supported...")
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
    IMAGE_FILENAME = filename
    # return send_from_directory("images", filename, as_attachment=True)
    return redirect("image_processing")


@app.route('/image_processing', methods=['POST'])
def color_control():
    red_value = request.form["red_color_control"]
    green_value = request.form["green_color_control"]
    blue_value = request.form["blue_color_control"]
    print("Red value {}\nGreen value {}\nBlue value {}".format(red_value, green_value, blue_value))
    return render_template("image_processing.html")


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
        return render_template("upload.html")
    return render_template("login.html")


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'image.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8003')
