from PIL import Image

img = Image.open("binary.png")
img.save("binary.ico", format="ICO")