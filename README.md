<h1 align="center">Image Blending using Gaussian and Laplacian Pyramids</h1>
<h3 align="center">Laboratory Output #3 for Computer Vision</h3>

## Description

This Laboratory Output blends two input images using Gaussian and Laplacian pyramids with a mask to control the blending effect. It offers two blending modes: Vertical and Crazy.

### Vertical Blending
<p align="center">
  <img width="700" src="https://github.com/YangXLR8/Multiresolution/blob/main/output/blendVert.png" alt="cli output"/>
</p>

### Crazy Blending
<p align="center">
  <img width="700" src="https://github.com/YangXLR8/Multiresolution/blob/main/output/blendCrz.png" alt="cli output"/>
</p>



## Features

- **Blending Modes**:
  - **Vertical Blend**: Blends two images vertically.
  - **Crazy Blend**: Uses a provided mask to blend two images in a custom manner.

- **Image Processing**:
  - **Gaussian Stack**: Generates multiple levels of Gaussian-blurred images.
  - **Laplacian Stack**: Constructs Laplacian images from the Gaussian stack to preserve image details.

- **Plotting**: Visualizes the original images, mask, and the resulting blended image using Matplotlib.

- **Input Images**:
  - Modify the input image paths (`cooper.png`, `ghoul.png`, `shino.png`, `beach.png`, `czy-mask.png`) as needed.
  
- **Output**:
  - Saves the blended images (`blendVert.png` and `blendCrz.png`) and their resulting images (`blendVert_res.png` and `crzVert_res.png`) in the `output` directory.


## Project Structure

- `Input/`: Input images
- `Output/`: Output folder.
- `00-README.txt`: Laboratory Instructions
- `blending.py`: Main script to run the Hybrid Image Generation
- `Sardañas_lab03.zip`: submitted final laboratory output
- `spline83.pdf` : reference
- Jupyter Notebook
  - `BlendvertNB.ipynb`: Blend Vertical Notebook (grayscale version)
  - `BlendvertNBforRGB.ipynb`: Blend Vertical Notebook (RGB Version)
  - `BlendczyNBforRGB.ipynb` : Blend Crazy Notebook

## Requirements

- Python 3
- OpenCV (`cv2`)
- NumPy (`numpy`)
- Matplotlib (`matplotlib`)
- Scikit-image (`skimage`)

Install these dependencies using pip if you haven't already:

```bash
pip install opencv-python numpy matplotlib scikit-image
```

## Usage

1. Run the script:
```bash
python blending.py
```
2. Choose either the Vertical (1) or Crazy (2) blending mode.
3. Follow the prompts and inputs to complete the blending process.
4. View the blended images displayed using Matplotlib and saved in the output directory.

## Results

This laboratory generates the the following outputs:

- `output/blendVert.png` : Blended image for Vertical mode.
- `output/blendVert_res.png` : Resulting blended image for Vertical mode.
- `output/blendCrz.png` : Blended image for Crazy mode.
- `output/crzVert_res.png` : Resulting blended image for Crazy mode.
