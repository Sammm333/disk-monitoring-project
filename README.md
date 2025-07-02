Disk Monitor
A simple Python-based tool for monitoring disk space, packaged in a Docker container and automated with GitHub Actions. The script checks free disk space, logs results to disk_usage.log, and issues warnings if free space falls below 20%. Built to demonstrate Python scripting and DevOps automation skills.
Features

Monitors disk space using the psutil library.
Logs disk usage with timestamps to disk_usage.log.
Alerts when free space is below 20%.
Runs in a Docker container for portability.
Automated execution via GitHub Actions on a schedule.

Tech Stack

Python: psutil for disk monitoring, logging for log management.
Docker: Containerizes the application for consistent deployment.
GitHub Actions: Automates periodic execution and log collection.

Setup

Clone the Repository:git clone <repository-url>
cd disk-monitor


Install Dependencies:Ensure Docker is installed. The requirements.txt includes:psutil==5.9.5


Build Docker Image:docker build -t disk-monitor .


Run the Container:docker run --rm disk-monitor



Usage

The script checks the root disk (/) and logs results to disk_usage.log.
Check logs in the project directory or GitHub Actions artifacts (if using CI/CD).
Modify disk_monitor.py to adjust the threshold (default: 20%) or add notifications.

CI/CD

GitHub Actions workflow (.github/workflows/disk-monitor.yml) runs the script hourly.
Logs are uploaded as artifacts in GitHub Actions.

Future Enhancements

Add Telegram/email notifications for alerts.
Support monitoring multiple disks.
Deploy to a specific server for real-world use.

License
MIT License
