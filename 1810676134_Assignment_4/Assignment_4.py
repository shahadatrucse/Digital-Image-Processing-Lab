import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import math


def main():
    
    img_path='/home/shahadat/Desktop/DIP/bird.jpeg'
    rgb=plt.imread(img_path)
 
    plt.figure(figsize=(50,100))
    plt.subplot(3,2,1)
    plt.title('RGB')
    plt.imshow(rgb)

    grayscale = cv.cvtColor(rgb, cv.COLOR_RGB2GRAY)
    plt.subplot(3,2,2)
    plt.title('Grayscale')
    plt.imshow(grayscale,cmap='gray')
    kernel = np.array([
        [1,0,-1],
        [3,-1,5],
        [1,2,0]
    ])
    grayscale = cv.cvtColor(rgb, cv.COLOR_RGB2GRAY)
    kernel_output = cv.filter2D(grayscale,-1,kernel)
    plt.subplot(3,2,3)
    plt.title('Built in Filter')
    plt.imshow(kernel_output,cmap='gray')
    
    plt.subplot(3,2,4)
    plt.title('Built In Histogram')
    plt.hist(img.ravel(),256,[0,256]);
    
    img = np.array(grayscale)
    img = img.reshape(-1);
    yaxis = np.zeros((256,),dtype=int)
    for i in range(0,len(img)):
        yaxis[img[i]] += 1
    xaxis = np.array([i for i in range(0,256)])
    plt.subplot(3,2,6)
    plt.title('Customize Histogram')
    plt.bar(xaxis,yaxis,width=1)
    
    img=grayscale
    w, h = img.shape
    new_img = np.zeros(shape=(w+2,h+2))
    w, h = new_img.shape
    new_img[1:w-1,1:h-1] = img
    new_img.astype(int)
    
    img=new_img
    _, k = kernel.shape
    w, h = img.shape
    new_w, new_h = w-k+1, h-k+1
    conv_img = np.zeros(shape=(new_w,new_h))
    for i in range(new_w):
        for j in range(new_h):
            mat = img[i:i+k,j:j+k]
            conv_img[i,j] = np.sum(np.multiply(kernel,mat))
            if conv_img[i,j]<0:
                conv_img[i,j]=0
            elif(conv_img[i,j]>255):
                conv_img[i,j]=255
    
    my_kernel_output = conv_img
    plt.subplot(3,2,5)
    plt.title('Customize Filter')
    plt.imshow(my_kernel_output,cmap='gray')
    
    
    plt.show()
    
if __name__ == '__main__':
    main()
