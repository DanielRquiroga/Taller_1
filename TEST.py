import matplotlib.pyplot as plt
import skimage.io as io
import skimage.measure as measure

# Load the Ferrari logo image
ferrari = io.imread('ferrari.png')

# Convert the Ferrari logo image to grayscale
ferrari_gray = skimage.color.rgb2gray(ferrari)

# Extract the contours of the Ferrari logo image
ferrari_contours = measure.find_contours(ferrari_gray, 0.5)

# Load the BMW logo image
bmw = io.imread('bmw.png')

# Convert the BMW logo image to grayscale
bmw_gray = skimage.color.rgb2gray(bmw)

# Extract the contours of the BMW logo image
bmw_contours = measure.find_contours(bmw_gray, 0.5)

# Plot the Ferrari logo contours
fig, ax = plt.subplots()
ax.imshow(ferrari)
for contour in ferrari_contours:
    ax.plot(contour[:, 1], contour[:, 0], linewidth=1.5, color='red')
plt.show()

# Plot the BMW logo contours
fig, ax = plt.subplots()
ax.imshow(bmw)
for contour in bmw_contours:
    ax.plot(contour[:, 1], contour[:, 0], linewidth=1.5, color='red')
plt.show()