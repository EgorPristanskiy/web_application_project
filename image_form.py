from flask import render_template, request
from flask.views import View
import threading


class ImageForm(View):
    methods = ["POST", "GET"]
    running = False

    def dispatch_request(self):
        if request.method == "POST":
            red_color_value = request.form["red_color_control"]
            blue_color_value = request.form["blue_color_control"]
            green_color_value = request.form["green_color_control"]
            print("Red color {}\nBlue color{}\n Green color{}\n".format(red_color_value, blue_color_value, green_color_value))
        if request.method == "GET":
            try:
                print(request.form["red_color_control"])
            except KeyError:
                pass
        return render_template("image_processing.html", image_file='image.png')

    @staticmethod
    def add_url(app):
        app.add_url_rule("/image_processing", view_func=ImageForm.as_view("image_processing"))
