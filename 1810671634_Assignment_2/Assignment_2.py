import matplotlib.pyplot as plt
import cv2
import math


def main():
   
    img_path = '/home/shahadat/Desktop/DIP/bird.jpeg'
    rgb=plt.imread(img_path)
    print(rgb)
    print(rgb.shape)

    plt.figure(figsize=(50,100))
    plt.subplot(3,2,1)
    plt.title('Grayscale')
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    plt.imshow(grayscale,cmap='gray')
    
    
    width,height=grayscale.shape
    print("Width=",width)
    print("Height=",height)
    
   #1st Condition
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    c1_img=grayscale
    
    for i in range(0, width):
    	for j in  range(0,height):
    		if grayscale[i][j] >120  and grayscale[i][j] <200:
    			c1_img[i][j]=100
    		else:
    			c1_img[i][j]=10
 
    
    plt.subplot(3,2,2)
    plt.title('1st Condition')
    plt.imshow(c1_img,cmap='gray')
    

    
    #2nd Condition
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    c2_img=grayscale
    
    for i in range(0, width):
    	for j in  range(0,height):
    		if grayscale[i][j] >120  and grayscale[i][j] <200:
    			c2_img[i][j]=100
 
    
    plt.subplot(3,2,3)
    plt.title('2nd Condition')
    plt.imshow(c2_img,cmap='gray')
    
    
    
    #3rd Condition
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    c3_img=grayscale
    
    for i in range(0, width):
    	for j in  range(0,height):
    		c3_img[i][j]=10*math.log(1+grayscale[i][j])
 
    
    plt.subplot(3,2,4)
    plt.title('3rd Condition')
    plt.imshow(c3_img,cmap='gray')
    
    
    #4th Condition
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    c4_img=grayscale
    
    for i in range(0, width):
    	for j in  range(0,height):
    		c4_img[i][j]= 10*(grayscale[i][j] + 0.0000001 )**2
 
    
    plt.subplot(3,2,5)
    plt.title('4th Condition')
    plt.imshow(c4_img,cmap='gray')
   
    
    
    plt.subplots_adjust(left=0.1,
                    bottom=0.2, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.5, 
                    hspace=1.5)
    
    plt.show()
    
 
    

if __name__ == '__main__':
	main()


	
