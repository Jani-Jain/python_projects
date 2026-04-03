# Gesture Media Controller 🖐️🎵

A Python-based application that allows you to control your computer's media playback using hand gestures. It leverages **OpenCV** for video processing and **MediaPipe** for high-fidelity hand landmark tracking.



## 🚀 Features
* **Volume Control:** Adjust system volume by changing the distance between your thumb and index finger.
* **Play/Pause:** Toggle media playback with a specific hand sign (e.g., a fist or palm).
* **Track Navigation:** Skip tracks by waving left or right.
* **Real-time Feedback:** Visual overlays showing the detected hand landmarks and current volume levels.

---

## 🛠️ Tech Stack
* **Python 3.x**
* **OpenCV:** For capturing and processing webcam frames.
* **MediaPipe:** For 21-point hand skeleton tracking.
* **PyAutoGUI / Keyboard:** To simulate media key presses.
* **NumPy:** For mathematical calculations (like calculating distances between points).

---

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/gesture-media-controller.git
    cd gesture-media-controller
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install opencv-python mediapipe pyautogui numpy
    ```

---

## 🎮 How It Works

The system calculates the Euclidean distance between hand landmarks. The formula used for distance between two points $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$ is:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

### Key Mappings:
| Gesture | Action |
| :--- | :--- |
| **Thumb & Index Distance** | Volume Up / Down |
| **Four Fingers Up** | Play / Pause |
| **Swipe Right** | Next Track |
| **Swipe Left** | Previous Track |

---

## 🖥️ Usage
1.  Run the main script:
    ```bash
    python main.py
    ```
2.  Ensure your webcam is uncovered and you are in a well-lit environment.
3.  Press **'q'** on your keyboard to exit the application.

---

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for new gestures or performance optimizations.

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
