import cv2
import re
import numpy as np
from pyzbar.pyzbar import decode
import webbrowser

cap = cv2.VideoCapture(0)
data_received = False

while cap.isOpened():
    _, img = cap.read()
    for qrcode in decode(img):
        codeData = qrcode.data.decode('utf-8')
        print(codeData)

        url_pattern = r'(https?://\S+)'
        match = re.search(url_pattern, codeData)
        if match:
            n=True
        else:
            n=False
        if(n):
            webbrowser.open(codeData)
        else :
            print(codeData)

        points = np.array([qrcode.polygon], np.int32)
        points = points.reshape((-1, 1, 2))
        points2 = qrcode.rect

        cv2.polylines(img, [points], True, (0, 255, 0), 5)
        cv2.putText(img, codeData, (points2[0], points2[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

        data_received = True
    cv2.imshow('image', img)

    if (cv2.waitKey(1) & 0xFF) and data_received:
        break

cap.release()
cv2.destroyAllWindows()
