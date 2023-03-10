import cv2
import os

# Define the path of the directory containing the images
image_directory = '/mnt/chromeos/MyFiles/Downloads/PRO-C105/PRO-C105-Project-Images-main'

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('video.mp4', fourcc, 25.0, (640, 480))

# Loop through the images in the directory and add them to the video
for image_name in os.listdir(image_directory):
    if image_name.endswith('.jpg') or image_name.endswith('.jpeg') or image_name.endswith('.png'):
        image_path = os.path.join(image_directory, image_name)
        img = cv2.imread(image_path)
        resized_img = cv2.resize(img, (640, 480))
        out.write(resized_img)

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()
