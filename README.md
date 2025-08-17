
# Medical AI System for Bone Fracture Detection

## Project Overview
This project implements an automated bone fracture detection and classification system using deep learning techniques. It leverages the EfficientNet B4 architecture along with attention mechanisms and Class Activation Mapping (CAM) for explainability. The system achieves high accuracy (~98%) on X-ray images of bone fractures.

## Features
- Uses EfficientNet B4 as the base model pretrained on ImageNet.
- Custom attention gate to highlight important image regions.
- Class Activation Mapping (CAM) to visualize model focus and decisions.
- Hybrid loss combining Cross-Entropy and Focal Loss for robust training.
- Handles multiple fracture types with high precision and recall.
- Early stopping and learning rate scheduling for efficient training.

## Dataset
The Human Bone Fractures image dataset is sourced from Kaggle:

[https://www.kaggle.com/datasets/jockeroika/human-bone-fractures-image-dataset/data](https://www.kaggle.com/datasets/jockeroika/human-bone-fractures-image-dataset/data)

It contains X-ray images categorized into several fracture types along with healthy bone images.

## Setup Instructions

### 1. Clone this repository

### 2. Download Dataset
Download and prepare the dataset by running the provided `download_dataset.py`:

```bash
pip install kaggle
```

- Place your Kaggle API token file (`kaggle.json`) in the appropriate directory:
  - Linux/macOS: `~/.kaggle/kaggle.json`
  - Windows: `C:\Users\<YourUsername>\.kaggle\kaggle.json`

- Run the dataset download script:

```bash
python download_dataset.py
```

This will download, unzip, and organize the dataset into the project directory.


(or install libraries individually: `torch`, `torchvision`, `numpy`, `matplotlib`, `scikit-learn`, `opencv-python`, `seaborn`)

### 3. Train the Model

Run the training script/notebook to train the model on the dataset. Hyperparameters such as batch size, learning rate, and epochs are configured within the code.

### 4. Evaluate and Visualize

After training, evaluate the model on the test set and use Grad-CAM visualizations to interpret model decisions.

## Project Structure
- `download_dataset.py`: Script to download and prepare the Kaggle dataset.
- Notebook: Contains model training and evaluation code.
