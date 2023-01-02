import cv2

carCascade = cv2.CascadeClassifier('Haarcascade Files/cars.xml')

cap = cv2.VideoCapture('Video/Car.mp4')

while cap.isOpened():
    #time.sleep(.03)
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    car = carCascade.detectMultiScale(gray,1.4,2)

    for (x,y,w,h) in car:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow('Cars',img)

    k= cv2.waitKey(30) & 0xff    #enter key
    if k == 27:    #ESC
        break

cap.release()
cv2.destroyAllWindows()
