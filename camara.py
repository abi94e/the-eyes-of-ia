import cv2

camara= cv2.VideoCapture(0)

while (True):
    ret, frame = camara.read()

    
    cv2.imshow('video1',frame)

    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break

camara.release()
cv2.destroyAllWindows()
