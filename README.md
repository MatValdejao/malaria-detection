# Malaria Detection Notebook

## Table of Contents
- [Objective](#objective)
- [Project Overview & Architecture](#project-overview--architecture)
- [Dataset](#dataset)
- [Dev and Execution Options:](#dev-and-execution-options)
- [Dependencies](#dependencies)
- [Results/Eval](#resultseval)


## Objective:
Objective of this notebook is to create a Deep Learning CNN model to classify single cell images as either parasitized or not with Malaria. The focus of this project will be optimization of recall on the parasitized class, aiming that no positive case is left unnoticed. 

## Project Overview & Architecture
Project utilized single cell images classified into infected or uninfected to train convolutional model for image classification. 
![Architecture Image](assets/arch_img.png)
- During training bias was introduced towards class 1 images via focal binary cross entropy, focusing on achieving higher recall on positive images. 

## Dataset
Dataset used for this project is from kagglehub.
https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria

## Dev and Execution Options:
- **To run project**: clone repo
- **To contribute**: fork and submit pull request

#### Option 1: Local Development (CPU or GPU):
- Clone repository into local machine
- Download dataset locally and update paths as needed
- Create and activate virtual environment, then register as a jupyter kernel
- Install dependencies: 
    From terminal:
        pip install -r requirements.txt 
    Within notebook: 
        Run cells 1 and 2

Works on CPU and GPU, thugh GPU is slower

#### Option 2: Google Colab (Quick Iteration and GPU)
- Clone or fork repository
- Upload cell_images and src python scripts into drive
- Open notebook in colab or using Colab-connected IDE
- Enable GPU runtime
- Ensure to run setup cells 1 and 2.

#### Option 3: Docker (GPU, Production-like)
- Clone or fork repository
- Create Docker image from provided Dockerfile
- Run inside GPU-enabled VM or in local machine with GPU support. GPU support requires compatible NVIDIA GPU, driver, and container toolkit. Create cloud instance VM and install manually if requirements not met.

        docker build -t project-name .
        docker run --gpus all -it -p 8888:8888 -p 8080:8080 project-name

## Dependencies
See requirements.txt file for dependency list

## Results/Eval
Objetive was to bias final model towards positive case recall, as the least desired result in a medical case is to leave a positive case untreated. Base model with convolutions, incrementing complexity and finally biasing towards positive class recall. 

- Final model achieved 97% recall on positive cases, ensuring minimal false negatives 

Final model without biasing still achieved really good results in recall, without same hit to precision. In this case, however, biased model might still be desirable.
