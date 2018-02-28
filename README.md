# Grayscaler

This project is used to convert images from RGB/GRB to grayscale. It uses Open CV2 for easy grayscale conversion

# To Do - 
```
  Crop images
```

### Prerequisites


**Open CV 3.0+ - https://opencv.org/**

To install using Anaconda - 
Open prompt and type command
```
conda install -c menpo opencv
```

## Getting Started

To run the program, you need to download the grayscale.py file located in the Src folder of this project. 

Once you have downloaded the file, 
open up the command line (cmd, powershell, etc) and navigate to the directory where grayscale.py is located (cd where/the/file/is). Then run this command to convert the images to grayscale.

```
grayscale.py -d path/to/images
```
This will convert all images in all subdirectories of that path into grayscale and dump them in a folder called "grayScaledImages"
The file format for these images are "gray0.png","gray1.png","gray2.png" and so on.

## Authors

* **Derek Vawdrey** - *Initial work* - [cow9000](https://github.com/cow9000)



