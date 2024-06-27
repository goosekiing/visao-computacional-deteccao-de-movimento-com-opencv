import numpy as np
import cv2

VIDEO = "Rua"
VIDEO_PATH = f"videos\\{VIDEO}.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)
has_frame, frame = cap.read()

frames_ids = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=72)

frames = []
for fid in frames_ids:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    has_frame, frame = cap.read()
    frames.append(frame)

median_frame = np.median(frames, axis=0).astype(dtype=np.uint8)
print(median_frame)
cv2.imshow("Median Frame", median_frame)
cv2.waitKey(0)
cv2.imwrite(f"images\\01-median-frame-{VIDEO.lower()}.jpg", median_frame)
