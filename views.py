from flask import Blueprint, render_template, request, url_for

from count_words import count_words

views = Blueprint(__name__, "views")

@views.route("/", methods=["POST", "GET"])
def index():
  if request.method == "POST":
    text_data = request.form["text_data"]
    return render_template("count_result.html", word_count=count_words(text_data))

  return render_template("index.html")