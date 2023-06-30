# Genre

This repository contains a web application built using Django and K-Nearest Neighbors (KNN) algorithm for predicting the genre of music based on input audio files. The application allows users to upload their audio files and receive a predicted genre label.

## Features

- Web-based user interface for uploading audio files
- Predicts the genre of music based on the uploaded audio file
- Supports WAW audio file format
- Utilizes K-Nearest Neighbors (KNN) algorithm for genre prediction
- Provides an interactive and intuitive user experience

## Installation

To use this application locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/music-genre-prediction.git
   ```

2. Change into the project directory:

   ```bash
   cd musicgenre
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **Unix or Linux**:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

8. Open your web browser and navigate to `http://localhost:8000/home` to access the application.

## Usage

1. Open the web application in your browser by visiting `http://localhost:8000`.

2. Click on the "Choose File" button to select an audio file from your local machine.

3. After selecting the file, click the "Check" button to initiate the genre prediction process.

4. Wait for the prediction to complete. The predicted genre label will be displayed on the screen.


## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Make sure to follow the existing coding style and guidelines.


## Acknowledgments

- The genre classification model used in this project is trained on a publicly available music dataset. We would like to thank the creators of the dataset for making it accessible.

- This project is built using the Django web framework, which provides a robust foundation for developing web applications in Python.

- The scikit-learn library is utilized for implementing the K-Nearest Neighbors algorithm for genre prediction.

## Contact

If you have any questions or need further assistance, feel free to contact the project maintainer at [email protected]
