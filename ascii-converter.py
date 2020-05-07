
from PIL import Image 
import numpy
  
def main(): 
    try: 
        #Relative Path 
        name ='picture3'
        with Image.open(name + '.jpg').convert('L') as img:  
            width, height = img.size 
            imgWidth = 220
            width = int(imgWidth)
            height = int(width*3/height/2*imgWidth)
            img = img.resize((width, height))
            #Saved in the same relative location 
            img.save("resized_" + name + ".jpg")  
            greyscale_map = list(img.getdata())
            greyscale_map = numpy.array(greyscale_map)
            greyscale_map = greyscale_map.reshape((height, width))
            arr =[]
            for i in greyscale_map:
                arr2=[]
                for j in i:
                    if j in range(40): arr2.append('#')
                    elif j in range(40,70): arr2.append('W')
                    elif j in range(70,90): arr2.append('N')
                    elif j in range(90,110): arr2.append('O')
                    elif j in range(110,130): arr2.append('I')
                    elif j in range(130,170): arr2.append('+')
                    elif j in range(170,200): arr2.append('-')
                    elif j in range(200,210): arr2.append('.')
                    else: arr2.append(' ')
                arr.append(arr2)
            with open(name + '.txt', 'w') as f:
                for item in arr:
                    for i in item:
                        f.write("%s" % i)
                    f.write("\n")
    except IOError: 
        pass
  
if __name__ == "__main__": 
    main() 
