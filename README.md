It is a sign language detection project, Used to ease the communication between the normal people and deaf-mute people.

Used ASL [American Sign Language] --> Goodbye, Hello, Help, Sorry, Thankyou.

Steps: 
  1- Collecting the images for the 5 sign languages:
    - There is no Given Dataset for such a problem --> so we have to create own dataset.
    - Using webcam to capture images of me doing the sign langauges.
    - Extract the frames from the downloaded tutorial videos to increase the size of data and apply the variaty in the collceted images.
      link_1 : https://www.signingsavvy.com/   
      link_2 : https://www.signasl.org/
  
  2- Extract the features from the images using mediapipe module:
    - It is an important step because we want the model to only focus on a specific place in the image not the whole image.
    - So, We detect the hand gestures using mediapipe and extract the landmarks from both hands then we can use them as a features to train our model.
    - After this step the dataset is : extracted features and labels --> data.pickle file.

  3- Split dataset:
    - Specify 80% of the dataset for the training process and the rest considered as a test data for the final evaluation step.
    - The balance in the dataset is preseved, So each class of the five has the same number of data.
    - We avoid the bias to specifc class --> Balanced Dataset.

  4- Train the model:
    - Random Forest used as algorithm for my model.
    - Then we train this model on the train data.
    - Finally, we saved the model for later usage --> model.pickle.

  5- Evaluation step:
    - Test data used to make this process.
    - Confusion Matrix and another metrics are calculated for this step.
    - 98.5% acheived as accuracy score for this task.

  
