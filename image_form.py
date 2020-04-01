from flask import render_template, request, session
from flask.views import View


class ImageForm(View):
    methods = ["POST", "GET"]

    def dispatch_request(self):
        if request.method == "GET":
            # image_filename = session.get("image_form")
            # print("Load file from {}".format(image_filename))
            return render_template("image_processing.html", image_file='image.png')

    @staticmethod
    def add_url(app):
        app.add_url_rule("/image_processing", view_func=ImageForm.as_view("image_feed"))
