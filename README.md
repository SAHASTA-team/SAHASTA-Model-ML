# SAHASTA - Sahabat Gizi Anak Untuk Cegah Stunting

## Project Overview

This project aims to develop a digital solution to address the issue of stunting in Indonesia. By utilizing machine learning techniques, specifically Convolutional Neural Networks (CNNs) and TensorFlow, we aim to create a model that can identify food items from images and provide valuable nutritional information. This information will empower health workers to make informed dietary choices, thereby it can contributing to improved child health and development.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Model Architecture](#model-architecture)
- [Model Training and Optimization](#model-training-and-optimization)
- [Model Deployment and Integration](#model-deployment-and-integration)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Dataset

The dataset used in this project is obtained from [Fruit and Vegetable Classification](https://www.kaggle.com/code/abdelrahman16/fruit-and-vegetable-classification/input). The included food items are:

- **Fruits:** Banana, Apple, Pear, Grapes, Orange, Kiwi, Watermelon, Pomegranate, Pineapple, Mango
- **Vegetables:** Cucumber, Carrot, Capsicum, Onion, Potato, Lemon, Tomato, Radish, Beetroot, Cabbage, Lettuce, Spinach, Soybean, Cauliflower, Bell Pepper, Chilli Pepper, Turnip, Corn, Sweetcorn, Sweet Potato, Paprika, Jalapeño, Ginger, Garlic, Peas, Eggplant

The dataset is divided into three main directories:

- **Training Data**: `train` directory
- **Validation Data**: `valid` directory
- **Test Data**: `test` directory (moved to validation during preprocessing)

## Data Preprocessing

We've curated a diverse dataset containing images of various food items. This dataset, sourced from Kaggle, includes a wide range of food categories, such as fruits and vegetables (36 Class)

To enhance the model's performance and generalization capabilities, we've implemented the following data preprocessing techniques:

**1. Image Resizing:** All images are resized to a standard size of 224x224 pixels.

**2. Image Normalization:** Pixel values are normalized to a specific range (e.g., 0-1) to ensure consistent input for the model.

**3. Data Augmentation:** To increase the dataset's size and diversity, we apply various augmentation techniques:
  - **Random Rotations:** Images are rotated randomly to introduce variations.
  - **Random Flips:** Images are flipped horizontally or vertically to create new perspectives.
  - **Random Cropping:** Random crops are taken from the original images to expose different parts of the food item.
  - **Color Jitter:** Random variations in color (brightness, contrast, saturation, hue) are applied to simulate real-world lighting conditions.
  - **Noise Addition:** Small amounts of noise are added to the images to make the model more robust to variations.

## Model Architecture



## Model Training and Optimization
To train our model effectively, we've employed the following techniques:

Optimizer and Loss Function
- **Optimizer**: Adam optimizer with a learning rate of 0.001 is used to efficiently update model weights.
- **Loss Function**: Sparse Categorical Crossentropy is chosen as the loss function to measure the model's prediction accuracy.

Performance Metrics
- **Metrics**: We monitor accuracy to assess the model's ability to correctly classify food images.

Callbacks for Improved Training
- **Model Checkpoint:** The best performing model is saved during training to prevent overfitting.
- **Early Stopping:** Training is stopped if validation accuracy doesn't improve for a certain number of epochs.
- **Learning Rate Reduction:** The learning rate is dynamically adjusted to avoid local minima and accelerate convergence.

## Model Deployment and Integration

To make the model accessible for our Android app, we've opted for a web API approach. Here's a breakdown of the steps involved:

1. Model Deployment:
    - **Backend Framework:** We'll use a backend framework like Flask to create a REST API.
    - **Model Serving:** The TensorFlow.js model will be loaded and served through this API.
    - **Hosting:** The API will be deployed to a cloud platform like Google Cloud Platform.

2. Android App Integration:
    - **API Calls:** The Android app will make HTTP requests to the deployed API to send image data.
    - **Image Preprocessing:** The app will preprocess images (resizing, normalization) before sending them.
    - **Response Handling:** The app will receive predictions from the API and display them to the user.

This approach allows for efficient model deployment and seamless integration with the mobile app, providing an user-friendly experience.

## Usage

Here's how to get started with the model:

1. **Grab the Code:** Clone this repository using Git.
   ```sh
   git clone https://github.com/dantidn/SAHASTA-Machine-Learning.git
2. **Set Up Your Environment:** Make sure you have the necessary libraries installed. You can do this in Google Colab or your Jupyter Notebook.
   ```sh
    pip install tensorflow pandas numpy opencv-python matplotlib
3. **Explore the Models:** Navigate to the Notebooks directory within the repository. You'll find notebooks that guide you through training and evaluating the models.
4. **Train and Evaluate:** Open the relevant notebook and run the code cells one by one. This will train the model and show you how well it performs.
5. **Save Your Work:** Once you're happy with the trained model, save it for later use. You can do this by running the provided code to save it as model.h5.
6. **Deploy on the Web (Optional):** If you want to use the model in a web application, you can convert it to the TensorFlow JS format using the provided code. Save the converted model as tfjs_model.zip.

## Contributing
We welcome your contributions! Share your ideas, suggestions, or code improvements through a pull request. Make sure your contributions align with the project's goals.

## Acknowledgments
This project is a result of the Bangkit Academy 2024 capstone project by Team C242-PS191. We are grateful to our advisors, Mrs. Dita Amallya and Mr. Wahyu Budi, for their invaluable guidance and support.
