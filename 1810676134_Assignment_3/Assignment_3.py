import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
	img_path = '/home/shahadat/Desktop/DIP/white_bird.jpeg'
	rgb = plt.imread(img_path)
		
	grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
	
	kernel1 = np.ones((3, 3), dtype = np.float32) * 2 / 7
	kernel2 = np.array([[0, 1, 0], [-3, 0, 1], [-1, 2, 1]])
	kernel3 = np.ones((3, 3), dtype = np.float32) * 3 /20
	kernel4 = np.array([[0, 2, 1], [1, -1, -1], [1, -1, 0]])
	kernel5 = np.ones((3, 3), dtype = np.float32) /4
	kernel6 = np.array([[1, 0, -1], [0,1,0], [0,0,1]])
	
	processed_img1 = cv2.filter2D(grayscale, -1, kernel1)
	processed_img2 = cv2.filter2D(grayscale, -1, kernel2)
	processed_img3 = cv2.filter2D(grayscale, -1, kernel3)
	processed_img4 = cv2.filter2D(grayscale, -1, kernel4)
	processed_img5 = cv2.filter2D(grayscale, -1, kernel5)
	processed_img6 = cv2.filter2D(grayscale, -1, kernel6)
		
	img_set = [rgb, grayscale, processed_img1, processed_img2,processed_img3,processed_img4,processed_img5,processed_img6]
	title_set = ['RGB', 'Grayscale', 'Kernel1', 'Kernel2','Kernel3', 'Kernel4','Kernel5', 'Kernel6']
	plot_img(img_set, title_set)

def plot_img(img_set, title_set):
	n = len(img_set)
	plt.figure(figsize = (15, 15))
	for i in range(n):
		img = img_set[i]
		ch = len(img.shape)
	
		plt.subplot(4, 2, i + 1)
		if (ch == 3):
			plt.imshow(img_set[i])
		else:
			plt.imshow(img_set[i], cmap = 'gray')
		plt.title(title_set[i])
		plt.subplots_adjust(left=0.1,
		            bottom=0.01, 
		            right=1, 
		            top=0.95, 
		            wspace=0.0, 
		            hspace=0.5)
                    
	plt.show()		
	
if __name__ == '__main__':
	main()
