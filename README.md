# AI Voice & Vision Medical Assistant

AI Voice & Vision Medical Assistant is an AI-powered healthcare tool that integrates image analysis and voice interaction to assist in diagnosing medical conditions. The system allows users to upload images of skin diseases, receive AI-generated medical insights, and listen to the diagnosis through text-to-speech (TTS) conversion. The goal is to provide a user-friendly, AI-driven medical consultation experience.

## Features

- ✅ **AI-Powered Image Analysis** – Uses LLaMA-3.2 Vision to analyze images of skin conditions and generate medical insights.
- ✅ **Voice Interaction** – Converts AI-generated text responses into speech using Google TTS (gTTS).
- ✅ **Interactive UI** – Built with Gradio, allowing users to upload images and interact with the AI easily.
- ✅ **Real-Time Medical Responses** – Provides concise and understandable health advice.
- ✅ **Multimodal Input Support** – Accepts both images and voice-based input for a seamless healthcare experience.

## Technology Stack

- **Programming Language**: Python
- **AI Model**: LLaMA-3.2 Vision Preview
- **Frontend**: Gradio
- **Speech Processing**: Google TTS (gTTS)

### Libraries Used:
- `gradio` – For UI development
- `gtts` – Text-to-Speech conversion
- `Pillow`/`OpenCV` – Image preprocessing
- `os` – File handling

## Project Structure

AI-VOICE-BOT/ │── brain_of_the_doctor.py # AI model integration for image analysis
│── voice_of_the_doctor.py # Text-to-Speech conversion
│── voice_of_the_patient.py # Handles speech input
│── gradio_app.py # Main application interface
│── acne.jpg / ulcers.jpg # Sample images for testing
│── final.mp3 # Generated speech response
│── .venv, .gradio # Virtual environment & dependencies
│── Pipfile, Pipfile.lock # Dependency management files


## How It Works

1. **Upload an Image** – The user uploads a skin-related image.  
   <img src="https://github.com/ShreeshaGM/ai-voice-and-vision-for-disease-detection-/blob/main/AI-Voice-BOT/acne.jpg" width="300" height="200" />

2. **AI Analysis** – The system uses LLaMA-3.2 Vision to detect abnormalities and provide a medical assessment.

3. **Voice Output** – The AI-generated response is converted to speech using gTTS.

4. **User Interaction** – Users receive an interactive text and voice-based diagnosis.  
   <img src="https://github.com/ShreeshaGM/ai-voice-and-vision-for-disease-detection-/blob/main/AI-Voice-BOT/clear%20skin.jpg" width="300" height="200" />

## Setup & Installation

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <your-repo-link>
cd AI-VOICE-BOT

2. Install Dependencies
Install the required Python dependencies:

bash
Copy code
pip install -r requirements.txt
Or, if using Pipenv:

bash
Copy code
pipenv install
pipenv shell
3. Run the Application
To start the application, run:

bash
Copy code
python gradio_app.py
The application will launch on http://127.0.0.1:7860 in your browser.

Future Improvements
✅ Speech-to-Text for voice-based diagnosis.

✅ Support for more medical conditions.

✅ Improved accuracy with fine-tuned AI models.

✅ Integration with patient history tracking.

Contributing
We welcome contributions! Feel free to fork the repository, make improvements, and submit a pull request.

License
Include your licensing information here (e.g., MIT License, etc.).

vbnet
Copy code

### Important Notes:
1. Replace `<your-repo-link>` with your actual repository link on GitHub or wherever you're hosting your project.
2. Ensure that the images (`acne.jpg` and `ulcers.jpg`) are placed in the repository where they are referenced, or update the image paths if they are located elsewhere.
3. Add your license details under the "License" section at the bottom if you have a specific license (e.g., MIT License, Apache 2.0, etc.).

This is the complete `README.md` that explains how the system works, how to set it up, and includes sections for contributions, future improvements, and more. Let me know if you need further adjustments!
