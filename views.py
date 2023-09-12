from flask import Blueprint, jsonify, render_template, request

from count_words import count_words


views = Blueprint(__name__, "views")

@views.route("/", methods=["POST", "GET"])
def index():
  if request.method == "POST":
    if request.form["text_data"]:
      text_data = request.form["text_data"]
      return render_template("count_result.html", word_count=count_words(text_data))
    else:
      return jsonify({"error": "Invalid input"}), 400

  return render_template("index.html")
