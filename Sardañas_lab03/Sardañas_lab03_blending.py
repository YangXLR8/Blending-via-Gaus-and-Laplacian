# imports
import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage

def main():
   
    while True:

        blend_type = int(input("Blending type Vertical(1)/Crazy(2): "))

        if blend_type == 1:
            img_A, img_B, img_Mask = blend_vert()
            break
        elif blend_type == 2:
            img_A, img_B, img_Mask = blend_crz()
            break
        else:
            print("Invalid. Please choose only (1) vertical or (2) crazy.")

    
    # make a lowpass filter (gaussian blur)
    img_GA = makeGaussianStack(img_A)
    img_GB = makeGaussianStack(img_B)
    img_GC = makeGaussianStack(img_Mask)


    img_LA = makeLaplacianStackfromGS(img_GA)
    img_LB = makeLaplacianStackfromGS(img_GB)


    img_LS = []

    for i in range(len(img_LA)):
        img_LS.append(((img_LA[i]*img_GC[i]) + (img_LB[i]*(1-img_GC[i]))))
    
    img_Res = sum(img_LS)   
    
    
    if blend_type == 1:
        blendVert = plot_Img(img_A, img_B, img_Mask, img_Res)
        blendVert.savefig('output/blendVert.png', bbox_inches='tight')
        plt.imsave('output/blendVert_res.png', np.clip(img_Res, 0, 1))
        plt.show()

    elif blend_type == 2: 
        blendCrz = plot_Img(img_A, img_B, img_Mask, img_Res)
        blendCrz.savefig('output/blendCrz.png', bbox_inches='tight')
        plt.imsave('output/crzVert_res.png', np.clip(img_Res, 0, 1))

        plt.show()
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def blend_vert():

    # inputs for blend vertically
    vert_A = process_img("input/cooper.png")
    vert_B = process_img("input/ghoul.png")

    # creating the mask
    height, width = vert_A.shape[:2]
    vert_Mask = np.zeros((height, width, 3)).astype(np.float32)
    vert_Mask[:, :width // 2] = 1

    return vert_A, vert_B, vert_Mask


def blend_crz():
    # inputs for blend crazy
    crz_A = process_img("input/shino.png")
    crz_B = process_img("input/beach.png")
    crz_Mask = process_img("input/czy-mask.png")

    return crz_A, crz_B, crz_Mask


def process_img(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (500, 500))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = skimage.img_as_float(img)
    return img


# function for creating the gaussian stack
def makeGaussianStack(img, count=5, sigmaValues=[0,2,4,6,8]):
    _temp = []

    for i in range(count):
        if sigmaValues[i] > 0:
            ksize = [0, 0]  # If sigma is greater than 0
        else:
            ksize = (5, 5)  # If sigma is 0 or less

        # Applying Gaussian blur to the input image with the specified sigma value and kernel size
        blurred_img = cv2.GaussianBlur(img, ksize=ksize, sigmaX=sigmaValues[i])
        
        # Adding the blurred image to the list
        _temp.append(blurred_img)
    
    return _temp


# make a laplacian stack from the gaussian stack created
def makeLaplacianStackfromGS(GS_img):
    _temp = []
    count = len(GS_img ) - 1        # Laplacian pyramid has one less level than the Gaussian pyramid
    for i in range(count):
        _temp.append(GS_img[i] - GS_img[i+1]) #captures the details lost

    _temp.append(GS_img[i])

    return _temp


# plot the images
def plot_Img(img_A, img_B, img_C, img_Res):
    
    # Titles for the subplots
    titles = ["Image A", "Image B", "Mask", "Blending Result"]
    images = [img_A, img_B, img_C, img_Res]


    # Create a figure with the specified size
    fig, axes = plt.subplots(1, 4, figsize=(12, 6))

    # Loop through images and titles to add them to the subplots
    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img)
        ax.set_title(title)
        ax.axis('off')  # Optionally turn off axes

    # Adjust layout to prevent overlap
    plt.tight_layout()

    return fig



if __name__ == "__main__":
    main()
