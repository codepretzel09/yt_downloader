from flask import jsonify
from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)
default_dir = "/downloads"
mp3_dir = "/mnt/media2/Music"
mp4_dir = "/mnt/media2/Youtube"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/download', methods=['POST'])
def download():
    url = request.form["url"]
    file_type = request.form["file_type"]
    output_path = default_dir  # Replace this with the default downlaod path
    download_youtube(url, file_type, output_path)
    return jsonify({"message": "Download complete. Check Plex!"})

def download_youtube(url, file_type, output_path):
    yt = YouTube(url)

    if file_type.lower() == "mp4":
        video = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        video.download(output_path=mp4_dir) # can update this to use a nfs share
        print(f"Video downloaded: {video.default_filename}")

    elif file_type.lower() == "mp3":
        video = yt.streams.filter(only_audio=True).first()
        file_path = video.download(output_path=mp3_dir) # can update this to use a nfs share
        base, ext = os.path.splitext(file_path)
        new_file = base + ".mp3"
        os.rename(file_path, new_file)
        print(f"Audio downloaded: {os.path.basename(new_file)}")

    else:
        print("Invalid file type. Please enter either 'mp4' or 'mp3'.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7999)