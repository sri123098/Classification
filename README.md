# Classification
Please download ex1/train ex1/test some of the images to give a test for the classification of the images.

Issue here is that the model_cnn.evaluate is giving the better result where as 

model_cnn.predict --- tensor of shape with number of classes 6 --- (taking the maximum of the predicted output and finding the index ) np.argmax and checking with the assigned label Y_test. 

Both giving different results


Please go through the keras documentation below:
https://keras.io/models/sequential/
    evaluate(self, x=None, y=None, batch_size=None, verbose=1, sample_weight=None, steps=None)
    predict(self, x, batch_size=None, verbose=0, steps=None)
