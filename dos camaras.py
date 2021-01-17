import cv2

camara = cv2.VideoCapture(0)
camara1 = cv2.VideoCapture(1)

while (True):
    ret, frame = camara.read()
    ret1, frame1 = camara1.read()

    cv2.imshow('camara 1', frame)
    cv2.imshow('camara 2', frame1)
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break

camara.release()
camara1.release()
cv2.destroyAllWindows()
