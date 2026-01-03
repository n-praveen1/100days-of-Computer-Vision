import cv2
import os

output_dir = "output_images"
os.makedirs(output_dir, exist_ok=True)

# Open camera (0 = default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access camera")
    exit()

print("Press 's' to save image | Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Camera Feed", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        image_path = os.path.join(output_dir, "captured_image.jpg")
        cv2.imwrite(image_path, frame)
        print(f"Image saved at {image_path}")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
