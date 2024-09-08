import cv2
import matplotlib.pyplot as plt

image = cv2.imread('img0.jpg') # your file here
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img = img.tolist()

#function to compare images side by side
def compare(original, manipulated, title_1="Original", title_2="Manipulated"):
    plt.figure(figsize=(15, 25))
    plt.subplot(1, 2, 1)
    plt.title(title_2)
    plt.imshow(manipulated)
    plt.subplot(1, 2, 2)
    plt.title(title_1)
    plt.imshow(original)
    plt.show()
    
def print_shape(img):
    try:
        print("Shape of the array is:", len(img), "x", len(img[0]), "x",
              len(img[0][0]))
    except:
        print("Shape of the array is:", len(img), "x", len(img[0]))


def add_list(img1, img2):
    return [[img1[i][j] + img2[i][j] for j in range(len(img1[0]))]
            for i in range(len(img1))]

def channel_last(img):
    return [[[img[k][i][j] for k in range(len(img))]
             for j in range(len(img[0][0]))] for i in range(len(img[0]))]
    
    
# grayscale
def grey(img):
    return [[[sum(j) // 3 for k in j] for j in i] for i in img]

grey_img = grey(img)
compare(img, grey_img)

# binerization
def binarization(img, threshold=128):
    return [[[(255 if sum(j) // 3 >= threshold else 0) for k in j] for j in i] for i in img]

bn_img = binarization(img)
compare(img, bn_img)

# negative
def negative(img):
    return [[[255 - k for k in j] for j in i] for i in img]

ng_img = negative(img)
compare(img, ng_img)

#mirror horizontal
def mirror_h(img):
    return [[img[i][-j - 1] for j in range(len(img[0]))]
            for i in range(len(img))]

#mirror vertical
def mirror_v(img):
    return [img[-i - 1] for i in range(len(img))]

mh_img = mirror_h(img)
mv_img = mirror_v(img)

compare(img, mh_img)
compare(img, mv_img)

# blur
def blur(img, strength=1):

    def blur_strength_1(img):
        temp1 = []
        for i in range(len(img)):
            temp2 = []
            for j in range(len(img[0])):
                temp3 = []
                for k in range(len(img[0][0])):
                    a_pixels = 1
                    temp = img[i][j][k]
                    try:
                        temp += img[i + 1][j + 1][k]
                        a_pixels += 1
                    except:
                        True
                    try:
                        temp += img[i + 1][j][k]
                        a_pixels += 1
                    except:
                        True
                    try:
                        temp += img[i + 1][j - 1][k]
                        a_pixels += 1
                    except:
                        True
                    try:
                        temp += img[i][j - 1][k]
                        a_pixels += 1
                    except:
                        True

                    try:
                        temp += img[i - 1][j - 1][k]
                        a_pixels += 1
                    except:
                        True
                    try:
                        temp += img[i - 1][j][k]
                        a_pixels += 1
                    except:
                        True
                    try:
                        temp += img[i - 1][j + 1][k]
                        a_pixels += 1
                    except:
                        True
                    try:
                        temp += img[i][j + 1][k]
                        a_pixels += 1
                    except:
                        True

                    temp3.append(int(temp / a_pixels))
                temp2.append(temp3)
            temp1.append(temp2)
        return temp1

    temp = img.copy()
    for i in range(strength):
        temp = blur_strength_1(temp)
    return temp

blur_img = blur(img, 2)
compare(img, blur_img)

# resize
def resize(img, size):

    return [[[
        img[int(len(img) * i / size[0])][int(len(img[0]) * j / size[1])][k]
        for k in range(3)
    ] for j in range(size[1])] for i in range(size[0])]

rs_img = resize(img, (100, 100))
compare(img, rs_img)

# lightness
def lightness(img, b=50):

    return [[[
        int((255 * (b / 100)) + (img[i][j][k] * (1 - (b / 100))))
        for k in range(len(img[0][0]))
    ] for j in range(len(img[0]))] for i in range(len(img))]

lg_img = lightness(img)
compare(img, lg_img)

# brightness
def brightness(img, strength=0):
    return [[[
        int((510 / (1 + (2.7183**(-strength * img[i][j][k] / 255)))) - 255)
        for k in range(len(img[0][0]))
    ] for j in range(len(img[0]))] for i in range(len(img))]

bg_img = brightness(img, 10)
compare(img, bg_img)

# contrast
def contrast(img, strength=0):
    return [[[
        int(255 / (1 + (2.7183**(-strength *
                                 ((img[i][j][k] - 127.5) / 127.5)))))
        for k in range(len(img[0][0]))
    ] for j in range(len(img[0]))] for i in range(len(img))]

ct_img = contrast(img, 5)
compare(img, ct_img)