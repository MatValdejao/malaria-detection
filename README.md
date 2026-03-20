# Malaria Detection Notebook

## Table of Contents

## Objective:
Objective of this notebook is to create a Deep Learning CNN model to classify single cell images as either parasitized or not with Malaria. The focus of this project will be optimization of recall on the parasitized class, aiming that no positive case is left unnoticed. 

## Project Overview & Architecture

## Dataset

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
- Clone or forck repository
- Upload cell_images and src python scripts into your drive
- Open notebook in colab or using Colab-connected IDE
- Emable GPU runtime
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



