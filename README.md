# 💽 Disk Monitor

A simple Python-based tool for monitoring disk space, packaged in a Docker container and scheduled with cron.  
The script checks free disk space every minute, logs results to `disk_usage.log`, and issues warnings if free space falls below 20%.  
This project demonstrates Python scripting, containerization with Docker, and automation via cron inside containers.

---

## 🚀 Features

- ✅ Monitors disk space using the `psutil` library
- 📝 Logs disk usage with timestamps to `disk_usage.log`
- ⚠️ Alerts when free space is below 20%
- 📦 Runs in a Docker container for portability
- ⏱ Scheduled to run every minute via cron

---

## 🧰 Tech Stack

- **Python**: Uses `psutil` for disk monitoring and `logging` for log handling  
- **Docker**: Containerizes the application for isolated and consistent deployment  
- **Cron**: Runs the monitoring script on a fixed schedule within the container

---

## ⚙️ Setup Instructions

### 1. 🔁 Clone the Repository

```bash
git clone https://github.com/Sammm333/disk-monitoring-project.git
cd disk-monitoring-project

📄 Project Files
Ensure the following files exist in the directory:

.
├── Dockerfile
├── disk_monitor.py
├── requirements.txt
├── crontab
└── README.md


🐳 Build the Docker Image
docker build -t disk-app-cron:0.0.1 .

▶️ Run the Container
Option A: Foreground (see output immediately)

docker run --rm -it disk-app-cron:0.0.1

Option B: Background Mode (detached)

docker run -d --name disk-monitor disk-app-cron:0.0.1

Thanks :)
