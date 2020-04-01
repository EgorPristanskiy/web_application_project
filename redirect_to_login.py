from flask import redirect
from flask.views import View


class RedirectToLogin(View):
    methods = ["GET", "POST"]

    def dispatch_request(self):
        return redirect("/login")

    @staticmethod
    def add_url(app):
        app.add_url_rule("/", view_func=RedirectToLogin.as_view("redirect_to_login"))
