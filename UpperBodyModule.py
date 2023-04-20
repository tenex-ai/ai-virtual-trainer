import cv2 as cv
import time
import numpy as np
import pose_estimation_module as pem

def upperBody():
    ang=None
    print("upper body ai trainer is created")
    capture = cv.VideoCapture(0)
    capture.set(3, 1280)
    pose_det = pem.pose_detector()
    dir = 0
    count = 0
    ptime = 0
    hand = "r"
    id = []

    while True:
        if hand == "l":
            id = ["l", 11, 13, 15]
        if hand == "r":
            id = ["l", 12, 14, 16]
        success, frame = capture.read()
        frame = cv.resize(frame, (1280, 720), interpolation=cv.INTER_CUBIC)
        frame = pose_det.find_pos(frame, draw=False)
        lm_list = pose_det.find_position(frame)
        ang = pose_det.find_angle(frame, id[1], id[2], id[3], id[0])
        if ang!=None:
            per = np.interp(ang, (210, 290), (0, 100))
            height = np.interp(per, (0, 100), (370, 100))
            cv.rectangle(frame, (600, 100), (650, 370), (0, 255, 0), thickness=2)
            cv.rectangle(frame, (600, int(height)), (650, 370), (0, 255, 0), thickness=cv.FILLED)
            cv.putText(frame, f"{str(int(per))}%", (570, 70), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), thickness=3)

            if per == 100:
                cv.rectangle(frame, (600, 100), (650, 370), (0, 0, 255), thickness=2)
                cv.rectangle(frame, (600, int(height)), (650, 370), (0, 0, 255), thickness=cv.FILLED)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                cv.rectangle(frame, (600, 100), (650, 370), (0, 0, 255), thickness=2)
                cv.rectangle(frame, (600, int(height)), (650, 370), (0, 0, 255), thickness=cv.FILLED)
                if dir == 1:
                    count += 0.5
                    dir = 0
            cv.rectangle(frame, (10, 250), (160, 400), (255, 0, 0), thickness=cv.FILLED)
            if int(count) < 10:
                cv.putText(frame, str(int(count)), (45, 370), cv.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255), thickness=7)
            else:
                cv.putText(frame, str(int(count)), (5, 370), cv.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255), thickness=7)
            ctime = time.time()
            fps = 1 / (ctime - ptime)
            ptime = ctime

            cv.putText(frame, f"FPS : {str(int(fps))}", (20, 50), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), thickness=2)

        cv.imshow("frame", frame)

        if cv.waitKey(2) & 0xFF == ord('d'):
            break
        elif cv.waitKey(2) & 0xFF == ord('l'):
            hand = "l"
        elif cv.waitKey(2) & 0xFF == ord('r'):
            hand = "r"
        elif cv.waitKey(2) & 0xFF == ord('s'):
            count = 0
    capture.release()
    cv.destroyAllWindows()

# upperBody()