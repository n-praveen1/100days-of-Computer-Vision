\# Day 01 – Camera Image Capture



\## Objective

Capture an image from the system camera and save it to the local directory.



\## Tools Used

\- Python

\- OpenCV (cv2)



\## Steps

1\. Open the default webcam using OpenCV

2\. Display live camera feed

3\. Press \*\*'s'\*\* to save the captured image

4\. Press \*\*'q'\*\* to exit the application



\## Output

\- Captured image is saved in the `output\_images/` folder.



\## Observations

\- OpenCV uses device index `0` for the default webcam.

\- Proper resource release is important to avoid camera lock issues.



