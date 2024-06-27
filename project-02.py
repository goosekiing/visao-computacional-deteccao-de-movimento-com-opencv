import numpy as np
import cv2
from time import sleep

# for VIDEO in ["Rua", "Arco", "Estradas", "Peixes", "Ponte"]:
VIDEO = "Rua"
VIDEO_PATH = f"videos\\{VIDEO}.mp4"
delay = 10

cap = cv2.VideoCapture(VIDEO_PATH)
has_frame, frame = cap.read()

frames_ids = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=72)

frames = []
for fid in frames_ids:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    has_frame, frame = cap.read()
    frames.append(frame)

median_frame = np.median(frames, axis=0).astype(dtype=np.uint8)
# # cv2.imshow("Median Frame", median_frame)
# # cv2.waitKey(0)
# cv2.imwrite(f"images\\01-median-frame-{VIDEO.lower()}.jpg", median_frame)

# # -- Aula 02 --

# cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
gray_median_frame = cv2.cvtColor(median_frame, cv2.COLOR_BGR2GRAY)
# # cv2.imshow("Gray Median Frame", gray_median_frame)
# # cv2.waitKey(0)
# cv2.imwrite(f"images\\02-gray-median-frame-{VIDEO.lower()}.jpg", gray_median_frame)

while (True):
    tempo = float(1/delay)
    sleep(tempo)

    has_frame, frame = cap.read()

    if not has_frame:
        print("Acabaram os frames")
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    dframe = cv2.absdiff(frame_gray, gray_median_frame)
    th, dframe = cv2.threshold(dframe, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cv2.imshow("Gray Frame", dframe)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cap.release()
