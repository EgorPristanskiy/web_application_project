from flask import redirect, request, Response, url_for
from flask.views import View
from image_processing import ImageProcessing


class ImageProcessingAdapter(View):
    methods = ["POST", "GET"]
    image_processing = ImageProcessing(image_path="static/image.png")
    colors_values = [50, 50, 50]

    def dispatch_request(self):
        if request.method == "POST":
            red_color_value = int(request.form["red_color_control"])
            blue_color_value = int(request.form["blue_color_control"])
            green_color_value = int(request.form["green_color_control"])
            colors_value = [red_color_value, green_color_value, blue_color_value]
            self.image_processing.set_color_values(colors_value)
            return redirect("/image_processing")
        elif request.method == "GET":
            return Response(self.image_processing.image_stream_thread(),
                            mimetype='multipart/x-mixed-replace; boundary=frame')

    @staticmethod
    def add_url(app):
        app.add_url_rule("/video_feed",
                         view_func=ImageProcessingAdapter.as_view("video_feed"))
