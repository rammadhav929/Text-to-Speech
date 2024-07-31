from flask import Flask, render_template, request, send_from_directory
from say import generate_audio

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("enter.html")


@app.route("/", methods=["POST"])
def process_text():
    user_text = request.form["user_input"]
    try:
        # Ensure you pass the desired filename
        generate_audio(user_text, "download/audio.mp3")
        message = "Audio generated and available for download!"
    except Exception as e:
        message = f"Error generating audio: {e}"
    return render_template("enter.html", message=message)


app.config["STATIC_FOLDER"] = "static"


@app.route("/download/audio.mp3")
def download_audio():
    return send_from_directory("static", "audio.mp3", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
