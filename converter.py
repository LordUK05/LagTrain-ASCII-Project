import PIL.Image
import os
import time
 
img_flag = True
path = ""
count = 0
def ConvertFrame(path):
    try:
      img = PIL.Image.open(path)
      img_flag = True
    except:
      print(path, "Unable to find image ");
     
    width, height = img.size
    aspect_ratio = height/width
    new_width = 200
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
     
    img = img.convert('L')
     
    chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", ".", "!", "W", "H"]
     
    pixels = img.getdata()
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    return ascii_image

def cls():
    print ("\n" * 1000)
# os.system('Music.mp3')
#for i in range(1259):
#    count = count+1
#    path = str("FRAMEDUMP/frame ("+str(count)+").png" )
#    image_ascii = ConvertFrame(path)
#    print(image_ascii)
#    time.sleep(0.2)
#    cls()
    #os.system("cls")

for i in range(2518):
    count = count+1
    path = str("FRAMEDUMP/frame"+str(count)+".png" )
    image_ascii = ConvertFrame(path)
    toappend = image_ascii+"¬"
    with open("DAT_200.asciidata", "a") as f:
        f.write(toappend)

f.close()
