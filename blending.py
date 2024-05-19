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
    
    img_Res = blending(img_A, img_B, img_Mask)
    
    
    if blend_type == 1:
        blendVert = plot_Img(img_A, img_B, img_Mask, img_Res)
        blendVert.savefig('trial/blendVert.png', bbox_inches='tight')
        plt.imsave('trial/blendVert_res.png', np.clip(img_Res, 0, 1))
        plt.show()

    elif blend_type == 2: 
        blendCrz = plot_Img(img_A, img_B, img_Mask, img_Res)
        blendCrz.savefig('trial/blendCrz.png', bbox_inches='tight')
        plt.imsave('trial/crzVert_res.png', np.clip(img_Res, 0, 1))

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

def blending(img_A, img_B, img_Mask):
    count = 5
    sigmaValues = [0, 2, 4, 6, 8]

    # Create Gaussian stacks
    img_GA = []
    img_GB = []
    img_GC = []

    for i in range(count):
        ksize = [0, 0] if sigmaValues[i] > 0 else (5, 5)
        
        blurred_A = cv2.GaussianBlur(img_A, ksize=ksize, sigmaX=sigmaValues[i])
        blurred_B = cv2.GaussianBlur(img_B, ksize=ksize, sigmaX=sigmaValues[i])
        blurred_C = cv2.GaussianBlur(img_Mask, ksize=ksize, sigmaX=sigmaValues[i])
        
        img_GA.append(blurred_A)
        img_GB.append(blurred_B)
        img_GC.append(blurred_C)

    # Create Laplacian stacks from Gaussian stacks
    img_LA = []
    img_LB = []

    for i in range(count - 1):
        laplacian_A = img_GA[i] - img_GA[i + 1]
        laplacian_B = img_GB[i] - img_GB[i + 1]
        img_LA.append(laplacian_A)
        img_LB.append(laplacian_B)

    img_LA.append(img_GA[-1])
    img_LB.append(img_GB[-1])

    # Blend Laplacian stacks
    img_LS = []

    for la, lb, gc in zip(img_LA, img_LB, img_GC):
        ls = la * gc + lb * (1 - gc)
        img_LS.append(ls)

    # Reconstruct the blended image from the Laplacian stack
    img_Res = np.zeros_like(img_LS[0])
    
    for img in img_LS:
        img_Res += img

    return img_Res



if __name__ == "__main__":
    main()
