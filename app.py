from web_application_polytech import Login, UploadImage, RedirectToLogin, ImageForm
from flask import Flask
import os


class App(object):
    def __init__(self):
        app_path = os.path.dirname(os.path.abspath(__file__))
        self.__app = Flask(__name__)
        login_page = Login()
        image_form = ImageForm()
        redirect_to_login = RedirectToLogin()
        upload_image_page = UploadImage()
        image_form.add_url(self.__app)
        redirect_to_login.add_url(self.__app)
        login_page.add_url(self.__app)
        upload_image_page.add_url(self.__app)

    def get_app(self):
        return self.__app


app = App().get_app()
application = app

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8003")
