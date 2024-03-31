import os
import cv2
import time
import uuid

IMAGE_PATH = "dataset"

labels = ["Hello", "Yes", "No", "Thanks", "IloveYou", "Please"]

num_images = 20

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)

    # Use the camera to capture images
    cap = cv2.VideoCapture(0)
    print(f"Collecting images for {label}")

    # 5 sec delay to get ready
    time.sleep(5)

    for num_img in range(num_images):
        ret, frame = cap.read()

        image_name = os.path.join(IMAGE_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))

        cv2.imwrite(image_name, frame)
        cv2.imshow("frame", frame)

        time.sleep(2)
        
        # press 'q' to quit
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break

    cap.release()
