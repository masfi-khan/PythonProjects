from PIL import Image

# RGB values for recoloring.
# darkBlue = (0, 51, 76)
# red = (217, 26, 33)
# lightBlue = (112, 150, 158)
# yellow = (252, 227, 166)

darkViolet = (60, 47, 99)
lightViolet = (90, 72, 110)
palePink = (255, 210, 210)
pink = (232, 140, 140)
darkRed = (187, 70, 70)
greenBlue = (55, 86, 82)
brown = (139, 59, 5)

# Import image.
my_image = Image.open("portugal.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.
# print(image_list)

recolored = [] #list that will hold the pixel data for the new image.
#
# YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
def colorization():
     for item in image_list:
         color = (item[0] + item [1] + item[2])
         if color < 182:
             recolored.append(pink)
         elif color >= 182 and color < 364:
             recolored.append(lightViolet)
         elif color >= 364 and color < 546:
             recolored.append(palePink)
         elif color >= 546:
             recolored.append(darkRed)


colorization()
# # Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
