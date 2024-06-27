# Computer Vision: Motion Detection with OpenCV

This repository contains a project focused on motion detection using the OpenCV library. The project is divided into several stages.

## Project Overview

### Part 1
In the first part, a technique is used to generate an image from a video by randomly selecting some frames and forming an image with the median value of each pixel. This technique helps discard unwanted objects that appear momentarily in the image. An example application of this technique is generating an image of tourist spots where the appearance of tourists in the image is discarded. However, this technique only works with a very well-stabilized camera where the scene of interest does not have any displacement in the frame.

### Parts 2, 3, and 4
These parts study filters and masks that can be applied to a video to detect motion.

### Part 5
The final part uses the knowledge from the previous stages to identify the movements of cars on a road and create an automated counter for the number of vehicles passing through a specific point.

## Course Details
This project was completed as part of the 'Computer Vision with OpenCV' course on Alura. For more information about the course, visit [Alura](https://cursos.alura.com.br/formacao-visao-computacional-opencv).

## Objectives Achieved
- Learn OpenCV resources applied to video analysis.
- Understand how videos are made and how to analyze video frame by frame.
- Learn to remove the background image from a video, even with various moving objects.
- Gain a better understanding of filters and techniques used in video analysis.
- Complete a practical project for detecting and counting moving objects.

## Project Structure
The directory structure of the project is as follows:
```
visao-computacional-deteccao-de-movimento-com-opencv/
│
├── project-01.py
├── project-02.py
├── project-03.py
├── project-04.py
├── project-05.py
├── project-03-results.csv
├── requirements.txt
├── images/          # Directory for images created during project execution
├── videos/          # Directory for videos used during the project
```

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/goosekiing/visao-computacional-deteccao-de-movimento-com-opencv.git
   ```
2. Navigate to the project directory:
   ```sh
   cd visao-computacional-deteccao-de-movimento-com-opencv
   ```
3. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install the required libraries:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Scripts
1. Ensure you have the required videos in the `videos/` directory.
2. Run the scripts in the following order to reproduce the results:
   ```sh
   python project-01.py
   python project-02.py
   python project-03.py
   python project-04.py
   python project-05.py
   ```

## Technologies Used
- Python (v3.11.4)
- Jupyter Notebook
- OpenCV (cv2 v4.6.0)
- Numpy

## Language
The language used in this project is Brazilian Portuguese (pt-br).

## Author
GitHub Username: [goosekiing](https://github.com/goosekiing)
