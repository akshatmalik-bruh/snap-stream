# 🚀 Snap Stream: Revolutionizing College Video Lectures

### Table of Contents
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Tech Stack](#tech-stack)
4. [Project Structure](#project-structure)
5. [Getting Started](#getting-started)
6. [Contributing](#contributing)

## Overview
Snap Stream is an innovative video summarizer built to help students quickly grasp key concepts from youtube viceo lectures. By condensing lengthy lectures into concise 30-second reading blocks, this project aims to enhance learning efficiency and make studying more manageable. Whether you're a student looking to save time or an educator seeking to improve knowledge retention, Snap Stream is the perfect tool for you.

## Key Features
Summarize youtube video into 30-second reading blocks
Support for hindi and english
User-friendly interface for easy navigation

## Tech Stack
| Library/Framework | Version |
| --- | --- |
| FastAPI | 0.115.13 |
| FastAPI-CLI | 0.0.7 |
| Jinja2 | 3.1.6 |
| Pydantic | 2.11.7 |
| SQLAlchemy | 2.0.41 |
| Uvicorn | 0.34.3 |
| Youtube-Transcript-API | 1.1.0 |
| yt-dlp | 2025.6.25 |

## Project Structure
```markdown
.
├── .gitignore
├── database.py
├── main.py
├── modelresponse.py
├── models.py
├── requirements.txt
├── script.py
├── script2.py
├── static
│   └── styles.css
├── subtitles
│   ├── College Rules Are DESTROYING Your Future ｜ Must Watch for Students!.en.vtt
│   └── College Rules Are DESTROYING Your Future ｜ Must Watch for Students!.hi.vtt
├── templates
│   ├── item.html
│   └── subtitle.html
```

## Getting Started
To get started with Snap Stream, follow these steps:
1. Clone the repository: `git clone https://github.com/your-username/snap-stream.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `uvicorn main:app --host 0.0.0.0 --port 8000`


