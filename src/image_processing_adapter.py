from flask import redirect, request, Response
from flask.views import View
from web_application_polytech import ImageProcessing


class ImageProcessingAdapter(View):
    methods = ["POST", "GET"]
    image_processing = ImageProcessing(image_path="/home/egorpristanskiy/web_application_design/web_application_project/static/image.png")
    colors_values = [50, 50, 50]

    def dispatch_request(self):
        if request.method == "POST":
            rotate_angle = int(request.form["rotate_control"])
            self.image_processing.set_color_values(colors_value)
            return redirect("/image_processing")
        elif request.method == "GET":
            return Response(self.image_processing.image_stream_thread(),
                            mimetype='multipart/x-mixed-replace; boundary=frame')

    @staticmethod
    def add_url(app):
        app.add_url_rule("/video_feed",
                         view_func=ImageProcessingAdapter.as_view("video_feed"))
