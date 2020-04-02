from flask import render_template, request
from flask.views import View
from image_processing import ImageProcessing


class ImageForm(View):
    methods = ["POST", "GET"]
    running = False
    image_processing = ImageProcessing(image_path="static/image.png")

    def dispatch_request(self):
        return render_template("image_processing.html", image_file='image.png')

    @staticmethod
    def add_url(app):
        app.add_url_rule("/image_processing", view_func=ImageForm.as_view("image_processing"))
