# Keylogging Project

This is a simple yet powerful keylogger application built with Python and Tkinter. It provides a user-friendly graphical interface to start and stop the logging of keystrokes. All captured data is saved locally for educational and monitoring purposes.

---

## Description

[cite_start]The application captures all keyboard events when active and saves them into two separate log files: a plain text file (`key_log.txt`) for easy reading and a structured JSON file (`key_log.json`) for detailed analysis of key presses, holds, and releases[cite: 5]. [cite_start]The GUI provides clear status indicators, real-time statistics, and easy controls for managing the keylogging process[cite: 5].

---

## Features

* [cite_start]**Graphical User Interface**: An intuitive GUI built with Tkinter for easy operation[cite: 5].
* [cite_start]**Start/Stop Functionality**: Simple buttons to start and stop the keylogger at any time[cite: 5].
* [cite_start]**Dual Log Format**: Saves logs in both human-readable `.txt` and machine-readable `.json` formats[cite: 5].
* [cite_start]**Real-time Status**: A visual indicator shows whether the keylogger is currently `ACTIVE` or `INACTIVE`[cite: 5].
* [cite_start]**Keystroke Counter**: Displays the total number of key events recorded during a session[cite: 5].
* [cite_start]**Easy Log Access**: A "View Logs" button that opens the output directory (`/out`) directly in the system's file explorer[cite: 5].
* [cite_start]**Cross-Platform**: Designed to run on Windows, macOS, and Linux[cite: 5].

---

## Requirements

* Python 3.x
* [cite_start]`pynput` [cite: 5]

---

## Installation and Usage

1.  **Clone or Download**: Obtain the project files and place them in a directory on your computer.

2.  **Navigate to Directory**: Open a terminal or command prompt and navigate to the project's root folder (`Keylogging-main`).

3.  **Install Dependencies**: Install the required `pynput` library using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**: Execute the main script to launch the GUI.
    ```bash
    python keylogger.py
    ```

5.  **Using the Controller**:
    * [cite_start]Click **▶ START KEYLOGGER** to begin capturing keystrokes[cite: 5].
    * [cite_start]Click **■ STOP KEYLOGGER** to terminate the capture session[cite: 5].
    * [cite_start]Click **📁 VIEW LOGS** to open the `out` folder containing the log files[cite: 5].

---

## Disclaimer

⚠️ **FOR EDUCATIONAL USE ONLY** ⚠️

[cite_start]This software is intended for educational purposes and for use on systems you own or have explicit permission to monitor[cite: 5]. Using a keylogger on a computer without the owner's consent is a violation of privacy and is illegal in many jurisdictions. The developers of this project are not responsible for any misuse of this software. [cite_start]THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND[cite: 3].

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

[cite_start]Copyright (c) 2025 ntvs28[cite: 2].
