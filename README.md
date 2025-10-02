# JarvisPy (Voice Command Windows Assistant)

**JarvisPy** is a personal **learning project** created by **Manish Singh** to explore and improve Python skills.  
It is a Windows-based voice assistant application with a GUI interface that allows you to interact with your system using voice commands.

---

## Features

- Voice recognition using **Google Voice-to-Text API**  
- Executes predefined commands stored in a **local database**  
- GUI interface for ease of use  
- Custom trigger word: **"Jarvis"**  
- Reads sample commands and executes actions based on similarity  

---

## How It Works

1. The app listens for the trigger word **"Jarvis"**.  
2. Converts your spoken command into text using Google's voice-to-text parser.  
3. Matches the command with predefined commands in the database.  
4. Executes the corresponding action on the Windows system.  

---

## Requirements

- Python 3.9+  
- `tkinter` (for GUI)  
- `speechrecognition` (for voice input)  
- `pyttsx3` (for text-to-speech responses)  
- `google-api-python-client` (or any Google voice-to-text wrapper)  
- Other dependencies listed in `requirements.txt`  

---
```
python main.py
```
## Learning Outcomes

1. This project was primarily for learning purposes and helped in:
   - Practicing Python GUI development with Tkinter
   - Working with voice recognition and speech synthesis
   - Understanding command parsing and execution
   - Learning how to integrate Python with external APIs
2. Future Improvements
   - Add customizable commands by the user
   - Integrate more advanced natural language processing
   - Cross-platform support (Linux/Mac)
   - Better GUI with real-time command feedback

## License
MIT License © 2025 Manish Singh


Created with ❤️ by Manish Singh
