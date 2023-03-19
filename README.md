# YouTube Downloader

YouTube Downloader is a simple and user-friendly web application that allows users to download YouTube videos as MP4 (video) or MP3 (audio) files. The application is built using Flask, a Python web framework, and Pytube, a lightweight library to download YouTube videos.

![YouTube Downloader Screenshot](screenshot.png)

## Features

- Download YouTube videos in MP4 (video) format
- Download YouTube videos in MP3 (audio) format
- Select video quality (highest or lowest)
- Dark/Light mode toggle
- URL preview of the video

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository to your local machine:

git clone https://github.com/codepretzel/youtube-downloader.git
cd youtube-downloader


### Step 2: Install Dependencies

Install the required Python packages using pip:

pip install -r requirements.txt


### Step 3: Run the Application

Run the Flask application:

python app.py


### Step 4: Access the Web Interface

Open your web browser and navigate to `http://127.0.0.1:7999` to access the YouTube Downloader web interface.

## Usage

1. Enter the YouTube video URL in the input field.
2. Select the desired file type (MP4 or MP3) from the dropdown menu.
3. Choose the video quality (highest or lowest) from the dropdown menu.
4. Click the "Download" button to start the download process.
5. A "Download complete" message will be displayed upon successful completion, and the file will be saved to the specified location.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to report bugs or suggest improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.