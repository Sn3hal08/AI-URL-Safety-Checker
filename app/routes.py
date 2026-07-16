from flask import Blueprint, render_template, request
from .model_loader import predict_url
main=Blueprint('main',__name__)
@main.route("/",methods=["GET","POST"])
def home():
    result=None
    if request.method=="POST":
        url=request.form.get("url")
        result=predict_url(url)
    return render_template("index.html",result=result)