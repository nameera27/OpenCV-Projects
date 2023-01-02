import cv2

faceCascade = cv2.CascadeClassifier('Haarcascade Files/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face = faceCascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow('Face',img)

    k = cv2.waitKey(30) & 0xff  # enter key
    if k == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
