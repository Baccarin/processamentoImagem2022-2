from PIL import Image, ImageFilter    

image = Image.open('img.png')
image = image.filter(ImageFilter.GaussianBlur) 
image.save("gaussiano.jpg")