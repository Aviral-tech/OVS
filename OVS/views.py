from flask import Blueprint,Flask, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import candidate

views = Blueprint("views", __name__)

@views.route("/")
def landing():
    return render_template("landing.html")

@views.route("/uploadface")
@login_required
def uploadface():
    status = current_user.status
    admin = current_user.admin
    return render_template("uploadFace.html", status=status, admin=admin)

@views.route("/profile")
@login_required
def profile():
    info = current_user
    status = current_user.status
    admin = current_user.admin
    return render_template("profile.html", status=status, admin=admin, info=info)

@views.route("/voting")
@login_required
def voting():
    status = current_user.status
    admin = current_user.admin
    candidates = candidate.query.filter_by().all()
    if status == "Not Verified":
         flash("User not Verified")
         return redirect(url_for("auth.home"))
    return render_template("voting.html", candidates=candidates, status=status, admin=admin)

@views.route("/result")
@login_required
def result():
    status = current_user.status
    admin = current_user.admin
    return render_template("result.html",status=status, admin=admin)
    