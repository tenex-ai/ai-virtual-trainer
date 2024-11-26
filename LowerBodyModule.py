import cv2 
import time
import numpy as np
import pose_estimation_module as pem
def lowerBody():
    print("lower body ai trainer is created")
    ctime=0
    ptime=0
    fps=0
    dir=0
    count=0
    pd=pem.pose_detector()
    cap=cv2.VideoCapture("5g.mp4")
    while True:
        ret, img=cap.read()
        # img=cv2.resize(img, (3000,800), interpolation=cv2.INTER_CUBIC)
    img=pd.find_pos(img, draw=False)
    pd.find_position(img)
        pd.find_angle(img, 23, 25, 27, "l",45,21)
        angle=pd.find_angle(img, 24, 26, 28, "r")
        per = np.interp(angle, (164, 180), (0, 100))
        height = np.interp(per, (0, 100), (370, 100))
        cv2.rectangle(img, (600, 100), (650, 370), (0, 255, 0), thickness=2)
        cv2.rectangle(img, (600, int(height)), (650, 370), (0, 255, 0), thickness=cv2.FILLED)
        cv2.putText(img, f"{str(int(per))}%", (570, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), thickness=3)
        # print(int(per))
        if per == 100:
            cv2.rectangle(img, (600, 100), (650, 370), (0, 0, 255), thickness=2)
            cv2.rectangle(img, (600, int(height)), (650, 370), (0, 0, 255), thickness=cv2.FILLED)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            cv2.rectangle(img, (600, 100), (650, 370), (0, 0, 255), thickness=2)
            cv2.rectangle(img, (600, int(height)), (650, 370), (0, 0, 255), thickness=cv2.FILLED)
            if dir == 1:
                count += 0.5
                dir = 0
        cv2.rectangle(img, (10, 250), (160, 400), (255, 0, 0), thickness=cv2.FILLED)
        if int(count) < 10:
            cv2.putText(img, str(int(count)), (45, 370), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255), thickness=7)
        else:
            cv2.putText(img, str(int(count)), (5, 370), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255), thickness=7)
        ctime = time.time()
        fps = 1 / (ctime - ptime + ctime - ptime - ftime)
        ptime = ctime
        cv2.imshow('win', img)
        if cv2.waitKey(2) & 0xFF == ord('d'):
            break
        if cv2.waitKey(2) & 0xFF == ord('s'):
            count = 0
        
console.log('ok bye')
# lowerBody()
