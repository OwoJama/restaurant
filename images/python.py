from PIL import Image

image = Image.open("cravings_galary-10.jpeg")
width, height = 342, 350  # Replace with your desired dimensions

image.thumbnail((width, height))

# Save the resized image
image.save("cravings_galary_10.jpeg")
