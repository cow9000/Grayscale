# Grayscaler

This project is used to convert images from RGB/GRB to grayscale. It uses Open CV2 for easy grayscale conversion

## Getting Started

Download the python file - grayscale.py (inside the src folder), and put it in any directory you like.
Then in command line go to the directory where you put "grayscale.py" and run the following command
grayscale.py -d path/to/files
This will convert all images in all subdirectories of that path into grayscale and dump them in a folder called "grayScaledImages"
The file format for these images are "gray0.png","gray1.png", and so on.

### Prerequisites

What things you need to install the software and how to install them

```
Open CV 3.0+ - https://opencv.org/
```
To install using Anaconda - 
Open prompt and type command
```
conda install -c menpo opencv
```
## Authors

* **Derek Vawdrey** - *Initial work* - [cow9000](https://github.com/cow9000)

## Acknowledgments

* CV2 for making this extremely easy
