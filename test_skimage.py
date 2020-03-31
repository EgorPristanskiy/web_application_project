from skimage import io


image = io.imread("./static/image.png")
print(image.shape)
image[:, : , 0] += 100
io.imsave("tmp.png", image)