# Holomat Calibration & Jarvis AI Assistant

Inspired by [ConceptBytes' Holomat](https://github.com/Concept-Bytes/Holomat)

This repository contains two main components:

1. **Calibration Scripts** – Python scripts to perform camera calibration for the Holomat project using a Charuco board and 4-point calibration via OpenCV contours.
2. **Jarvis AI Assistant** – A voice-activated assistant inspired by Iron Man’s Jarvis. It leverages OpenAI (and a local Ollama-based model) for conversational capabilities and controls smart devices via voice commands.

---

## Table of Contents

- [Installation](#installation)
  - [Calibration Scripts](#calibration-scripts)
  - [Jarvis AI Assistant](#jarvis-ai-assistant)
- [Usage](#usage)
  - [Calibration Scripts](#calibration-scripts-usage)
  - [Jarvis AI Assistant](#jarvis-ai-assistant-usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Installation

### Calibration Scripts

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository


2. **Install the required Python libraries:**
  ```
  pip install opencv-python mediapipe numpy
  pip install opencv-contrib-python
  pip install pyautogui
```
### Jarvis AI Assistant

1. **Install additional dependencies:**

```
pip install openai pygame ollama
```
2. **Configuration:**

- In /assist.py, add your OpenAI API key.
- In assist.py and assist_local.py, update any additional configuration (such as assistant_id and thread_id for the OpenAI assistant, if applicable).
- Ensure your system is set up for audio input/output (microphone, speakers).

## Usage
### Calibration Scripts Usage

  -Run the calibration script:
```
python calibration.py
```
Note:
  -It is strongly recommended to follow along with my video on Patreon as there may be additional debugging steps needed to get everything working correctly.

###Jarvis AI Assistant Usage
-Start the assistant:
```
python jarvis.py
```
  -How it works:
    -The assistant continuously listens for hot words such as "jarvis".
    -Upon detecting a hot word, it records your voice, processes the speech, and sends the query to the appropriate AI engine.
    -The response is then spoken back using text-to-speech, and if included, device control commands (e.g., #3d_printer-1 to turn on the 3D printer) are executed.
    -Two versions are provided:
    -assist.py uses the OpenAI API.
    -assist_local.py uses a local Ollama-based model with conversation history.

##Requirements
-Python: 3.6 or later
-OpenCV: 4.0 or later
-MediaPipe
-NumPy
-PyAutoGUI
-OpenAI API
-Pygame
-Ollama
-Other dependencies as required by the scripts

##Contributing
Contributions are welcome! If you'd like to improve or add new features, please fork the repository and submit a pull request.

##License
Distributed under the MIT License. See the LICENSE file for more information.

##Contact
For any feedback, support, or questions, please reach out via GitHub Issues or email me at santosmatthewjohn.com.
