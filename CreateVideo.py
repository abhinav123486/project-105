import os
import cv2

path = "Images/"
Images = []

for files in os.listdir(path):
    file, ext = os.path.splitext(files)
    if ext in ['.gif', '.png', '.jpg', '.jepg', '.jfif']:
        file_name = path + files
        print(file_name)
        Images.append(files)
        
count = len(Images)
frame = cv2.imread(Images[0])
width, height, channels = frame.shape()
size = (width, height)

print(size)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
    cv2.imread(Images[i])
    out.write()