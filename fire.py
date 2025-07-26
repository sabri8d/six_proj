import cv2
from playsound import playsound

firecascade = cv2.CascadeClassifier('fire_detection.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = firecascade.detectMultiScale(frame, 1.2, 5)

    for (x, y, w, h) in fire:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        print("fire is detect")
        playsound('sound1.mp3')  
    cv2.imshow('sabri', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
