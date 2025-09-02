# 🎬 YouTube to Blog Automation with CrewAI

This project automates the process of:

1. Searching for YouTube videos from a specific channel.
2. Generating a script/summary from the selected video.
3. Creating a blog post from the script.

It uses **CrewAI** to orchestrate multiple AI agents with tasks in a sequential workflow.

---

## 🚀 Features

- Search videos from a given **YouTube channel** only.
- Extract video details based on **topic and video title match**.
- Automatically write a **script** for the video.
- Convert the script into a **detailed blog post**.
- Modular structure with `agents`, `tasks`, and `tools`.

---

## 📂 Project Structure

````graphql
      youtube-blog/
        │── crew.py # Entry point, defines Crew workflow
        │── agents.py # Agents (YouTube Script Writer, Blog Writer)
        │── tasks.py # Tasks assigned to agents
        │── tools.py # Custom YouTube search tool
        │── requirements.txt # Python dependencies
        │── README.md # Project documentation



## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/youtube-blog.git
   cd youtube-blog
```

Create and activate a virtual environment:
```bash
     conda create -n crewai-blog python=3.10 -y
     conda activate crewai-blog
```

Install dependencies:

```bash
     python crew.py
Usage
   ```bash
      python crew.py

````
