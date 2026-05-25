# Stereo Vision 101: Calibration, Rectification & 3D Reconstruction

Welcome to **Stereo Vision 101**, a "not so well-documented" notebook for hands-on exploration of core computer vision concepts. 

This is for the beginners. If you're the John Carmack of the computer vision, I'm fully prepared for my public execution in the GitHub issues section.

This repo is not optimized for comfort. It is designed to slowly drag you from:  
"yeah yeah I know the theory"  
to  
"what do you mean the baseline direction is wrong?"

You might:
- discover that rectification is black magic with linear algebra branding
- question why your point cloud looks like abstract modern art
- develop trust issues with reprojection error
- finally understand what `Q` actually does after pretending for weeks

The objective is simple:
break things, question everything, suffer productively, and eventually understand stereo vision from first principles instead of API rituals.

---

## Topics:

* **Camera Calibration & Photogrammetry**:
  * Intrinsic Camera Matrix ($K$) calibration representing focal length ($f_x, f_y$) and principal point ($c_x, c_y$).
  * Lens Distortion coefficients (estimating radial and tangential distortion to undistort images).
  * Extrinsic parameters (calculating rotation $R$ and translation $T$ vectors relative to the world coordinate system).
  * World-to-Image coordinate projection and coordinate space transformations.
* **Epipolar Geometry**:
  * Understanding epipoles, epipolar planes, and epipolar line projection (epilines).
  * Estimating the **Fundamental Matrix ($F$)** and **Essential Matrix ($E$)**.
  * The mathematical constraints governing corresponding points in stereo camera pairs ($x'^T F x = 0$).
* **Stereo Rectification**:
  * Bouguet's rectification algorithm for aligning camera optical axes.
  * Rectification homography mapping.
  * Undistortion and remapping via pixel coordinate transforms.
  * Feature matching-based rectification comparing SIFT descriptors, feature matching, and RANSAC homography against standard calibration-driven rectification.
* **Stereo Depth & Disparity Estimation**:
  * Block matching algorithms and **Semi-Global Block Matching (SGBM)**.
* **3D Point Cloud Reconstruction**:
  * Triangulation and disparity-to-depth reprojection using a perspective transformation matrix ($Q$).
  * Interactive 3D point cloud generation and visualization.
  * Spatial downsampling and coordinate transforms.
* **Feature Extraction & Matching**:
  * SIFT (Scale-Invariant Feature Transform) keypoint detection and descriptor computation.
  * FLANN or Brute-Force feature matching across stereo pairs.

---

## Installation & Setup

### Prerequisites
Make sure you have Python 3.11+ installed. It is highly recommended to use a virtual environment.

### 1. Clone the repository
```bash
git clone <repository_url>
cd stereo-101
```

### 2. Set up a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all required libraries via `pip`:
```bash
pip install opencv-python numpy matplotlib plotly jupyter
```

### 4. Run the Jupyter Notebook
Start the Jupyter Notebook server:
```bash
jupyter notebook
```
Open `stereo_vision_101.ipynb` and execute the cells sequentially to visualize each step!


## Interactive Tuning GUI (`stereo_control_ui_.py`)

Sourced from: https://learnopencv.com/depth-perception-using-stereo-camera-python-c/

Tuning the StereoSGBM matcher is vital for clean disparity maps. This is a standalone OpenCV utility script to tune matching parameters in real time using slider trackbars. It helps in understanding the effect of different parameters on the disparity map.

### How to Run:
```bash
python stereo_control_ui_.py
```
*Press `ESC` to exit the trackbar window.*

---

