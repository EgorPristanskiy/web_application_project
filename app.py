from src.login import Login
from web_application_polytech import Login, UploadImage, RedirectToLogin, ImageForm, ImageProcessingAdapter
from src.upload_image import UploadImage
from src.redirect_to_login import RedirectToLogin
from flask import Flask
from src.image_form import ImageForm
from src.image_processing_adapter import ImageProcessingAdapter


class App(object):
    def __init__(self):
        self.__app = Flask(__name__)
        login_page = Login()
        image_form = ImageForm()
        redirect_to_login = RedirectToLogin()
        upload_image_page = UploadImage()
        image_processing_adapter = ImageProcessingAdapter()
        image_form.add_url(self.__app)
        redirect_to_login.add_url(self.__app)
        login_page.add_url(self.__app)
        upload_image_page.add_url(self.__app)
        image_processing_adapter.add_url(self.__app)

    def get_app(self):
        return self.__app


app = App().get_app()
application = app

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8003")
