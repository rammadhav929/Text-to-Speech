# Text-to-Audio Generator

This is a simple Flask web application that generates audio from text input. Users can enter text into a form, and the application will convert the text to speech and provide an audio file for download.

# Features

Text-to-Speech Conversion: Convert user-provided text into an audio file.
Downloadable Audio: After conversion, the audio file is available for download.
Prerequisites
Python 3.x
Flask: Web framework for Python.
say Module: Custom module or library for text-to-speech conversion. Ensure this module has a function generate_audio(text, filename) that converts the text to an audio file.

# Generate Audio:

Enter your text into the form on the homepage and submit.
After processing, you will receive a message indicating the audio file is ready for download.

# Download the Audio File:

Click the provided download link to save the audio file (audio.mp3) to your local machine.
File Structure
php

.
├── app.py # Main Flask application
├── templates
│ └── enter.html # HTML template for user input form
├── static
│ └── audio.mp3 # Directory for static files (e.g., generated audio)
└── README.md # This README file

# Acknowledgments

This project uses Flask, a micro web framework for Python.
The text-to-speech functionality is handled by the say module.
