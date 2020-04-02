from login import Login
from upload_image import UploadImage
from redirect_to_login import RedirectToLogin
from flask import Flask
from image_form import ImageForm
from threading import Thread


class App(object):
    def __init__(self):
        self.app = Flask(__name__)
        login_page = Login()
        image_form = ImageForm()
        redirect_to_login = RedirectToLogin()
        upload_image_page = UploadImage()
        image_form.add_url(self.app)
        redirect_to_login.add_url(self.app)
        login_page.add_url(self.app)
        upload_image_page.add_url(self.app)
        # self.app.secret_key = 'super secret key'
        # self.app.config['SESSION_TYPE'] = 'filesystem'

    def callback_form(self):
        while True:
            with self.app.test_client() as client:
                client.get('/image_processing')

    def run(self):
        # Thread(target=self.callback_form).start()
        self.app.run(debug=True)


if __name__ == '__main__':
    app = App()
    app.run()
