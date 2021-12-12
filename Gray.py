import cv2

Img=cv2.imread('1.jpg');
cv2.imshow('original Image',Img);
Blue_plane=Img[:,:,0];
cv2.imshow('Blue_plane',Blue_plane);
Green_plane=Img[:,:,1];
cv2.imshow('Green_plane',Green_plane);
Red_plane=Img[:,:,1];
cv2.imshow('Red_plane',Red_plane);

cv2.waitKey(0)

