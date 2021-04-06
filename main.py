import random
from random import randint
import sys
from PIL import Image, ImageChops
import argparse

pin_lenth = 5
array =[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]

for  i in range(10):
 random.shuffle(array[i])

def combine(share1,share2):
    s1 = Image.open(share1)
    s2 = Image.open(share2)
    s1 = s1.convert("1")
    s2 = s2.convert("1")
    combine = ImageChops.logical_or(s1, s2)
    combine.save("combine.png")

def shares(filename):
    original = Image.open(filename) # open colour image
    
    original = original.convert("1") # convert image to black and white
    
    o_pixels = original.load()# load black and white image to o_pixels

    first = Image.new("1", (original.size[0], original.size[1] ))
    f_pixels = first.load()
    
    second = Image.new("1", (original.size[0], original.size[1] ))
    s_pixels = second.load()
    
    for i in range(original.size[0]):
        for j in range(original.size[1]-1):
            if o_pixels[i,j] == 0:
                if random.randint(0, 1): #random.randint produces random integer in the range specified, including the boundaries.
                    f_pixels[i,j     ] = 1
                    f_pixels[i,j  + 1] = 0
                    s_pixels[i,j    ] = 0
                    s_pixels[i,j + 1] = 1
                else:
                    f_pixels[i,j    ] = 0
                    f_pixels[i,j + 1] = 1
                    s_pixels[i,j     ] = 1
                    s_pixels[i,j + 1] = 0
            else:
                if random.randint(0, 1):
                    f_pixels[i,j     ] = 0
                    f_pixels[i,j  + 1] = 1
                    s_pixels[i,j     ] = 0
                    s_pixels[i,j  + 1] = 1
                else:
                    f_pixels[i,j     ] = 1
                    f_pixels[i,j  + 1] = 0
                    s_pixels[i,j     ] = 1
                    s_pixels[i,j  + 1] = 0
    
    first.save(filename.split('.')[0] + "_1.png") #save first share
    second.save(filename.split('.')[0]  + "_2.png")# save second share 





def generate():
    
    for i in range(10):
        shares("data/"+str(i)+".png")
    
    image_list = []
    for i in range(10):
        for j in range(10):
            if(array[i][j]==0):
                image_list.append('data/0.png')
            elif(array[i][j]==1):
                image_list.append('data/1.png')
            elif(array[i][j]==2):
                image_list.append('data/2.png')
            elif(array[i][j]==3):
                image_list.append('data/3.png')
            elif(array[i][j]==4):
                image_list.append('data/4.png')
            elif(array[i][j]==5):
                image_list.append('data/5.png')
            elif(array[i][j]==6):
                image_list.append('data/6.png')
            elif(array[i][j]==7):
                image_list.append('data/7.png')
            elif(array[i][j]==8):
                image_list.append('data/8.png')
            else:
                image_list.append('data/9.png')

    images = [Image.open(x) for x in image_list]
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width*10, max_height*10))



    x_offset = 0
    y_offset = 0
    n=0


    for j in range(100):
        x_offset = 0
        for i in range(10):
            if(n<=99):
                new_im.paste(images[n], (x_offset,y_offset))
                x_offset += images[n].size[0]
                n+=1
            else:
                break
        if(n<=99):
            y_offset += images[n].size[1] 
        else:
            break

    
     
    new_im.save('Matrix.jpg')
    
    
    image_list.clear()







    for i in range(10):
        for j in range(10):
            if(array[i][j]==0):
                image_list.append('0_2.png')
            elif(array[i][j]==1):
                image_list.append('1_2.png')
            elif(array[i][j]==2):
                image_list.append('2_2.png')
            elif(array[i][j]==3):
                image_list.append('3_2.png')
            elif(array[i][j]==4):
                image_list.append('4_2.png')
            elif(array[i][j]==5):
                image_list.append('5_2.png')
            elif(array[i][j]==6):
                image_list.append('6_2.png')
            elif(array[i][j]==7):
                image_list.append('7_2.png')
            elif(array[i][j]==8):
                image_list.append('8_2.png')
            else:
                image_list.append('9_2.png')

    images = [Image.open(x) for x in image_list]
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width*10, max_height*10))



    x_offset = 0
    y_offset = 0
    n=0


    for j in range(100):
        x_offset = 0
        for i in range(10):
            if(n<=99):
                new_im.paste(images[n], (x_offset,y_offset))
                x_offset += images[n].size[0]
                n+=1
            else:
                break
        if(n<=99):
            y_offset += images[n].size[1] 
        else:
            break

    
     
    new_im.save('UserShare.jpg')


    print("OTP  generated :")


    rand = []

    while len(rand) <pin_lenth :
        range_start = 0
        range_end = 99
        r =  randint(range_start, range_end)
        if r not in rand:
            rand.append(r)


    print(rand)

    


    img_list=[]
    for i in range(10):
        for j in range(10):
            flag=0
            for k in range(pin_lenth):
                #print(rand[k])
                if int(rand[k]/10) ==i and rand[k]%10 == j:
                    if(array[i][j]==0):
                        img_list.append('0_1.png')
                        flag =1
                    
                    elif(array[i][j]==1):
                        img_list.append('1_1.png')
                        flag =1
                    
                    elif(array[i][j]==2):
                        img_list.append('2_1.png')
                        flag =1
                    
                    elif(array[i][j]==3):
                        img_list.append('3_1.png')
                        flag =1
                    
                    elif(array[i][j]==4):
                        img_list.append('4_1.png')
                        flag =1
                    
                    elif(array[i][j]==5):
                        img_list.append('5_1.png')
                        flag =1
                    
                    elif(array[i][j]==6):
                        img_list.append('6_1.png')
                        flag =1
                    
                    elif(array[i][j]==7):
                        img_list.append('7_1.png')
                        flag =1
                    
                    elif(array[i][j]==8):
                        img_list.append('8_1.png')
                        flag =1
                    
                    else:
                        img_list.append('9_1.png')
                        flag =1
                    if flag==1:
                        break   
            if flag==0:
                img_list.append('light_gray.png')

    images = [Image.open(x) for x in img_list]
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width*10, max_height*10))



    x_offset = 0
    y_offset = 0
    n=0


    for j in range(100):
        x_offset = 0
        for i in range(10):
            if(n<=99):
                new_im.paste(images[n], (x_offset,y_offset))
                x_offset += images[n].size[0]
                n+=1
            else:
                break
        if(n<=99):
            y_offset += images[n].size[1] 
        else:
            break

    
     
    new_im.save('ServerShare.jpg')



 
    

if __name__ == '__main__': #__name__ variable will be set as __main__if the module that is being run is the main program.
    '''parser = argparse.ArgumentParser()
    parser.add_argument("IMAGE", help="The image to encrypt")
    args = parser.parse_args()

    two_of_two(args.IMAGE)'''
    generate()
    combine("UserShare.jpg","ServerShare.jpg")
    
     

   
   

