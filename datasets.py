from sklearn.datasets import load_digits
digit = load_digits()


imgrs = digit['images']
import matplotlib.pyplot as plt
image = imgrs[23,:,:]
plt.imshow(image,cmap='gray')
#extract target
targets = digit["target"]
targets[23]