import mediapipe as mp
import cv2 as cv
import time
import math
import numpy as np


class pose_detector:
    def __init__(self, static_img=False, model_com=1, smooth_lm=True, enable_seg=False, smooth_seg=True,
                 min_det_con=0.5, min_track_con=0.5):
        self.static_img = static_img
        self.model_com = model_com
        self.smooth_lm = smooth_lm
        self.enable_seg = enable_seg
        self.smooth_seg = smooth_seg
        self.min_det_con = min_det_con
        self.min_track_con = min_track_con

        self.mpdraw = mp.solutions.drawing_utils
        self.mppose = mp.solutions.pose
        self.pose = self.mppose.Pose()

    def find_pos(self, frame, draw=True):
        frame = cv.resize(frame, (700, 400))
        imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpdraw.draw_landmarks(frame, self.results.pose_landmarks, self.mppose.POSE_CONNECTIONS)
        return frame

    def find_position(self, frame):
        self.lm_list=[]
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c=frame.shape
                self.lm_list.append([id, int(w*lm.x), int(h*lm.y)])
        return self.lm_list

    def find_angle(self, frame, p1, p2, p3, hand,draw=True):
        angle=None
        if len(self.lm_list) != 0:
            x1, y1 = self.lm_list[p1][1:]
            x2, y2 = self.lm_list[p2][1:]
            x3, y3 = self.lm_list[p3][1:]

            # drawing lines between the points
            if draw:
                
                cv.circle(frame, (x1, y1), 10, (0, 0, 255), thickness=2)
                cv.circle(frame, (x1, y1), 7, (0, 0, 255), thickness=cv.FILLED)
                cv.circle(frame, (x2, y2), 10, (0, 0, 255), thickness=2)
                cv.circle(frame, (x2, y2), 7, (0, 0, 255), thickness=cv.FILLED)
                cv.circle(frame, (x3, y3), 10, (0, 0, 255), thickness=2)
                cv.circle(frame, (x3, y3), 7, (0, 0, 255), thickness=cv.FILLED)

                cv.line(frame, (x1, y1), (x2, y2), (255, 255, 255), thickness=3)
                cv.line(frame, (x2, y2), (x3, y3), (255, 255, 255), thickness=3)

                angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
                if angle < 0:
                    angle += 360
                if hand == "l":
                    angle = 360 - angle
                cv.putText(frame, str(int(angle)), (x2-20, y2-20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)


        return angle


def main():
    ctime = 0
    ptime = 0
    cap = cv.VideoCapture("1.mp4")
    pos_es = pose_detector()
    while True:
        success, frame = cap.read()
        frame = pos_es.find_pos(frame)
        lm_list = pos_es.find_position(frame)
        # print(lm_list[4])
        if len(lm_list) > 0:
            cv.circle(frame, (int(lm_list[4][1]), int(lm_list[4][2])), 5, (0, 255, 0), thickness=cv.FILLED)
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv.putText(frame, str(int(fps)), (30, 70), cv.FONT_ITALIC, 1, (0, 255, 0), thickness=3)
        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xFF == ord("d"):
            break


if __name__ == "__main__":
    main()
