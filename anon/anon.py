import cv2

cascade_classifier = cv2.CascadeClassifier('haar.xml')
cap = cv2.VideoCapture(0)
x, y, w, h = 0, 0, 0, 0

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    try:
        x, y, w, h = cascade_classifier.detectMultiScale(gray)[0]
    except IndexError:
        pass
    face = frame[y:y + h, x:x + w]
    face = cv2.resize(face, (w // 16, h // 16), interpolation=cv2.INTER_NEAREST)
    face = cv2.resize(face, (w, h), interpolation=cv2.INTER_NEAREST)
    frame[y:y + h, x:x + w] = face
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
