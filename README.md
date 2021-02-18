# Image Description
This project aims to generate the most out of an image by generating a brief caption for whatever that is happening inside an image and showing all the objects that are present inside of that image. That way a lot of information can be gathered about an image. The model utilises computer vision and natural language processing techniques to recognise the contents of an image followed by object detection model which recognises objects present in an image and produces a bounding box around them.

## Note 
* After cloning the repository you need to create a folder named 'static'. This folder is responsible for storing the images uploaded to the flask app and showing them on the output page. 
* You need to download the yolov3.weights (608) file from [here](https://pjreddie.com/darknet/yolo/) and place it inside the folder.
* You can download the Flickr8k training dataset from :
* [Dataset](https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip)
* [Text_for_images](https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip)

### Folder structure

    .
    ├── cfg                           
    │   ├── yolov3.cfg                # Yolov3 configuration file
    ├── models                        # Trained caption generating models
    │   ├── model_9.h5                
    │   ├── model_trained_9.h5        
    ├── templates                     
    │   ├── index.html                # Landing page of the flask app (HTML)
    │   ├── output.html               # Output page (HTML)
    ├── test images                   # Images for testing purpose
    ├── app.py                        # Flask app python script
    ├── cap.py                        # Caption generation python script
    ├── coco.names                    # Yolov3 class names
    ├── descriptions.txt              # Captions for each image (part of training data)
    ├── features.p                    # Trained features (from 
    ├── im_cap_train.ipynb            # Description generating model training script    
    ├── tokenizer.p                   # Saved tokenized words
    ├── yolo_detection_images.py      # Yolov3 object detection python script
    └── README.md
 
## Hardware used 
* All work is done on LENOVO IDEAPAD 320-15IKB (Laptop)
* Processor: Intel Core i5 7th Gen 7200U 
* Installed Physical Memory (RAM): 8.00 GB
* Graphics Processor: NVIDIA GeForce 920MX 
* Hard Disk: 2TB

## Software and tools used
* Operating System: Windows 10 Pro
* Text/code editor: Sublime
* Jupyter notebook
* Anaconda prompt
* WSL2
* Google Colab notebooks

## Technology used
* Natural Language processing 
* Computer Vision
* Transfer Learning
* Python programming language
* HTML
* CSS
* Flask


