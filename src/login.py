from flask import Flask, render_template, request, send_from_directory, redirect, url_for, Response
from flask.views import View


class Login(View):
    methods = ["GET", "POST"]

    @staticmethod
    def check_email(email):
        arguments_by_dog = email.split("@")
        if len(arguments_by_dog) == 2:
            arguments_by_point = email.split('.')
            if len(arguments_by_point) == 2:
                return True
        return False

    def dispatch_request(self):
        print(request.method)
        if request.method == "POST":
            email_address = request.form["email"]
            password = request.form["password"]
            # if self.check_email(email_address) and len(password) > 6:
            print(email_address, password)
            return redirect("/image_processing")
        elif request.method == "GET":
            return render_template("login.html")

    @staticmethod
    def add_url(app):
        app.add_url_rule("/login", view_func=Login.as_view("login"))
