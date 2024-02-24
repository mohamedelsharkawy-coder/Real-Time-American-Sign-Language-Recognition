<h1> It is a sign language detection project, Used to ease the communication between the normal people and deaf-mute people.</h1> <br>
<h2> Used ASL [American Sign Languages] are Goodbye, Hello, Help, Sorry, Thankyou </h2> <br>

<h3>Goodbye</h3>
<img src='Goodbye.jpg'>

<h3>Hello</h3>
<img src='Hello.jpg'>

<h3>Help</h3>
<img src='Help.jpg'>

<h3>Sorry</h3>
<img src='Sorry.jpg'>

<h3>Thankyou</h3>
<img src='Thankyou.jpg'>

Steps: <br>
  <pre>1- Collecting the images for the 5 sign languages:<br>
    - There is no Given Dataset for such a problem --> so we have to create own dataset.<br>
    - Using webcam to capture images of me doing the sign langauges.<br>
    - Extract the frames from the downloaded tutorial videos to increase the size of data and apply the variaty in the collceted images.<br>
        link_1 : https://www.signingsavvy.com/<br>
        link_2 : https://www.signasl.org/<br>
  
  2- Extract the features from the images using mediapipe module:<br>
    - It is an important step because we want the model to only focus on a specific place in the image not the whole image.<br>
    - So, We detect the hand gestures using mediapipe and extract the landmarks from both hands then we can use them as a features to train our model.<br>
    - After this step the dataset is : extracted features and labels --> data.pickle file.<br>

  3- Split dataset:<br>
    - Specify 80% of the dataset for the training process and the rest considered as a test data for the final evaluation step.<br>
    - The balance in the dataset is preseved, So each class of the five has the same number of data.<br>
    - We avoid the bias to specifc class --> Balanced Dataset.<br>

  4- Train the model:<br>
    - Random Forest used as algorithm for my model.<br>
    - Then we train this model on the train data.<br>
    - Finally, we saved the model for later usage --> model.pickle.<br>

  5- Evaluation step:<br>
    - Test data used to make this process.<br>
    - Confusion Matrix and another metrics are calculated for this step.<br>
    - 98.5% acheived as accuracy score for this task.<br>

  
