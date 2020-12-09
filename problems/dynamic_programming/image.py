from PIL import Image

image = Image.open('unsplash_01.jpg')
new_image = image.resize((150, 170))
new_image.save('vazha_pindi.png')
