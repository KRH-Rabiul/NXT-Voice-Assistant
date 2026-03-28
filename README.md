# NXT Voice Assistant 🎙️🤖

An AI-powered desktop voice assistant built with **Python**, featuring **speech recognition**, **text-to-speech**, **browser automation**, **music playback**, **news headlines**, and **LLM-powered smart responses**.

This project is designed as a **portfolio-grade Python AI assistant** that demonstrates practical skills in:

* Python automation
* Voice interface design
* API integration
* AI-powered conversation
* Desktop productivity tools

---

## ✨ Features

* 🎤 **Wake Word Detection** (`NXT`)
* 🗣️ **Speech Recognition** using `speech_recognition`
* 🔊 **Text-to-Speech Response** using `pyttsx3`
* 🌐 **Open Websites by Voice**

  * Google
  * YouTube
  * Facebook
  * LinkedIn
* 🎵 **Music Playback Support**
* 📰 **Live News Headlines** via News API
* 🤖 **AI Chat Responses** using OpenRouter API
* ⏰ **Current Time Announcement**
* 🛑 **Voice Command Exit / Shutdown**

---

## 🛠️ Tech Stack

* **Python 3**
* `speech_recognition`
* `pyttsx3`
* `requests`
* `webbrowser`
* `datetime`
* `OpenRouter API`
* `News API`

---

## 📂 Project Structure

```text
NXT-Voice-Assistant/
│
├── main_.py
├── musicLibrary.py
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1) Clone the repository

```bash
git clone https://github.com/KRH-Rabiul/NXT-Voice-Assistant.git
cd NXT-Voice-Assistant
```

### 2) Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
NEWS_API_KEY=your_news_api_key
```

---

## ▶️ Run the Project

```bash
python main_.py
```

Then say the wake word:

```text
NXT
```

Example commands:

* `Open Google`
* `Open YouTube`
* `Play shape of you`
* `Tell me news`
* `What time is it`
* `Stop`

---

## 🧠 Example Voice Commands

| Command        | Action                   |
| -------------- | ------------------------ |
| Open Google    | Opens Google in browser  |
| Open LinkedIn  | Opens LinkedIn           |
| Play song_name | Plays music from library |
| News           | Reads top headlines      |
| Time           | Speaks current time      |
| Stop           | Exits the assistant      |

---

## 🚀 Future Improvements

* 🎯 Better wake-word detection
* 🧠 Local memory support
* 📁 File opening commands
* 💻 System control (shutdown, apps)
* 📧 Email sending by voice
* 🌍 Weather integration
* 🔐 Secure encrypted API key management

---

## 💼 Portfolio Value

This project demonstrates:

* Real-world Python project architecture
* API integration skills
* Voice AI workflow design
* Problem-solving with automation
* Beginner-friendly AI assistant engineering

A strong portfolio project for:

* **Software Engineering internships**
* **Python Developer roles**
* **AI/ML beginner portfolios**
* **Automation projects showcase**

---

## 👨‍💻 Author

**Khandakar Rabiul Hasan**

* GitHub: [https://github.com/KRH-Rabiul](https://github.com/KRH-Rabiul)
* LinkedIn: [www.linkedin.com/in/khandakar-rabiul-hasan](http://www.linkedin.com/in/khandakar-rabiul-hasan)

---

## ⭐ Support

If you like this project, consider giving it a **star ⭐ on GitHub**.

It helps the project grow and improves portfolio visibility.
