from flask import render_template, request, redirect, session
from flask.views import View
import os
from os.path import expanduser


class UploadImage(View):
    methods = ["GET", "POST"]
    home = expanduser("~")
    print(home + os.path.dirname((__file__)))
    app_root = home

    def dispatch_request(self):
        if request.method == "POST":
            target = os.path.join(self.app_root, 'static/')
            print("target_path{}".format(target))
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
            # session["image_feed"] = destination
            return redirect("/image_processing")
        elif request.method == "GET":
            return render_template("upload.html")

    @staticmethod
    def add_url(app):
        app.add_url_rule("/upload", view_func=UploadImage.as_view("upload"))
