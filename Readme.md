# Reviva — Real-Time Yawn Detection & Driver Fatigue Monitoring using YOLOv8 and IoT

Reviva is an AI-powered real-time driver monitoring system designed to detect yawning, a major indicator of fatigue, and trigger safety alerts to prevent road accidents. The system uses a lightweight YOLOv8 deep-learning model for fast inference and deploys efficiently on Raspberry Pi with buzzer and Telegram IoT notifications.

---

## Table of Contents
1. Features  
2. System Overview  
3. Architecture  
4. Dataset and Model Training  
5. Tech Stack  
6. Installation and Usage  
7. Raspberry Pi Deployment  
8. IoT Alert System (Buzzer and Telegram)  
9. Project Structure  
10. Results (Screenshots Placeholder)  
11. Contributors  
12. Future Enhancements  
13. License  

---

## Features
- Real-time yawning detection using YOLOv8  
- Continuous monitoring through live video stream  
- High-speed inference optimized for Raspberry Pi  
- Buzzer alert for drowsy drivers  
- Telegram notifications for remote monitoring  
- Robust performance under low light, motion, and occlusion  

---

## System Overview
Reviva continuously monitors the driver's facial region using an in-vehicle camera. Each frame is processed by the YOLOv8 model to classify yawn vs. non-yawn states. When multiple yawns are detected within a short duration, multi-channel alerts are activated to ensure driver safety.

---

## Architecture
Camera → Raspberry Pi → YOLOv8 Inference → Driver Yawn Detected?  
→ No → Continue monitoring  
→ Yes → Trigger buzzer alert + Telegram notification

![Architecture](https://raw.githubusercontent.com/SudharsaaX/Reviva-Yawn-Detection/main/results/reviva_architecture.png)


---

## Dataset and Model Training
- Dataset: Yawn Detection Dataset (Roboflow)
- Classes: Yawn, No Yawn
- Image size: 640 × 640
- Model: Ultralytics YOLOv8n

| Metric | Score |
|--------|-------|
| mAP@50 | 0.91 |
| Precision | 0.88 |
| Recall | 0.87 |

![Confusion Matrix](https://raw.githubusercontent.com/SudharsaaX/Reviva-Yawn-Detection/main/results/reviva_confusion_matrix.jpg)
---

## Tech Stack
| Component | Technology |
|----------|------------|
| Model | YOLOv8n |
| Language | Python |
| Framework | PyTorch |
| Computer Vision | OpenCV |
| Hardware | Raspberry Pi 4 + Camera Module |
| IoT Alerts | Buzzer + Telegram Bot API |

---

## Installation and Usage

### Clone the repository
```bash
git clone https://github.com/SudharsaaX/Reviva-Yawn-Detection.git
cd Reviva-Yawn-Detection

pip install -r requirements.txt

python main.py
---

## Raspberry Pi Deployment

sudo apt update
sudo apt install python3-opencv
pip install -r requirements.txt
python yawn_eye_alert_iot_first_test.py

## IoT Alert System (Telegram)
Steps to enable Telegram notifications:

Open Telegram → Search BotFather

Create a bot → Get BOT_TOKEN

Create a Telegram group → Add bot → Get CHAT_ID

Insert both values in the script:
BOT_TOKEN = "your_token_here"
CHAT_ID = "your_chat_id_here"


---

### ⭐ Preview of how it will display

✔ Clean separate code blocks  
✔ Bullet steps for readability  
✔ No Markdown break issues  
✔ Professional formatting for final-year project & recruiters

---

### ⚠ Final tip
To make README even more polished, add this just below the **Results** section:

```md
<p align="center">
  <img src="https://raw.githubusercontent.com/SudharsaaX/Reviva-Yawn-Detection/main/results/reviva_output.png" width="700">
</p>
