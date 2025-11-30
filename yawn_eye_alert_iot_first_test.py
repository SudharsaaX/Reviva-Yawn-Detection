import cv2
import time
import math
import mediapipe as mp
from ultralytics import YOLO
import simpleaudio as sa
import requests  

#  Telegram Bot Setup
TELEGRAM_BOT_TOKEN = '7331584156:AAHY_VzAyYk29idfkYhiafJUdpbrP6TQWZ4'
TELEGRAM_CHAT_ID = '-4812700284'

def send_telegram_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
        requests.post(url, data=data)
    except Exception as e:
        print(f"Telegram error: {e}")

#  Load YOLOv8 model for yawning detection
model = YOLO("best.pt")


#  Mediapipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

#  Eye landmarks for EAR
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def eye_aspect_ratio(landmarks, eye_points, w, h):
    def to_pixel(pt): return int(pt.x * w), int(pt.y * h)
    p1, p2, p3, p4, p5, p6 = [to_pixel(landmarks[i]) for i in eye_points]
    A = math.dist(p2, p6)
    B = math.dist(p3, p5)
    C = math.dist(p1, p4)
    ear = (A + B) / (2.0 * C)
    return ear

# EAR threshold and time limits
EAR_THRESHOLD = 0.25
EYE_CLOSED_SECONDS_THRESHOLD = 3

# Sound alert
#def play_alert():
#    wave_obj = sa.WaveObject.from_wave_file("alert.wav")
#    play_obj = wave_obj.play()

# Start webcam
cap = cv2.VideoCapture("http://192.168.29.150:8080/video")
time.sleep(2)

eye_closed_start = None
alert_triggered = False

print("Running... Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # YOLOv8 yawn detection
    yolo_results = model.predict(source=frame, conf=0.5, save=False, verbose=False)
    frame = yolo_results[0].plot()
    yawn_detected = any(d.cls == 0 or d.cls == 1 for d in yolo_results[0].boxes)

    # Mediapipe eye detection
    face_results = face_mesh.process(rgb_frame)
    if face_results.multi_face_landmarks:
        landmarks = face_results.multi_face_landmarks[0].landmark
        left_ear = eye_aspect_ratio(landmarks, LEFT_EYE, w, h)
        right_ear = eye_aspect_ratio(landmarks, RIGHT_EYE, w, h)
        avg_ear = (left_ear + right_ear) / 2.0

        # Eye closed detection
        if avg_ear < EAR_THRESHOLD:
            if eye_closed_start is None:
                eye_closed_start = time.time()
        else:
            eye_closed_start = None
            alert_triggered = False

        # Display EAR
        cv2.putText(frame, f'EAR: {avg_ear:.2f}', (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        # Check if both conditions met
        if yawn_detected and eye_closed_start:
            duration = time.time() - eye_closed_start
            if duration >= EYE_CLOSED_SECONDS_THRESHOLD and not alert_triggered:
                play_alert()
                send_telegram_alert("ALERT: Driver is yawning and eyes are closed!")
                alert_triggered = True
                cv2.putText(frame, "YAWN + CLOSED EYES!", (30, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    # Display
    #cv2.imshow("Yawn + Eye Alert", frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
#break

cap.release()
#cv2.destroyAllWindows()
