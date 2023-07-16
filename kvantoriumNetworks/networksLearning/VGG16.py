# 1 этап
#import numpy as np
#import matplotlib.pyplot as plt
#import keras
#from keras.datasets import cifar10
#from keras.models import Sequential
#from keras.layers import Dense, Flatten
#import base64
#import cv2
#from keras.optimizers import Adam

# 2 этап
# Load CIFAR-10 dataset
#(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize pixel values
#x_train = x_train / 255
#x_test = x_test / 255

# Convert labels to categorical
#y_train_cat = keras.utils.to_categorical(y_train, 10)
#y_test_cat = keras.utils.to_categorical(y_test, 10)

# Visualize some sample images
#encoded_images = []
#plt.figure(figsize=(6, 6))
#for i in range(16):
 #   plt.subplot(4, 4, i + 1)
 #   plt.xticks([])
 #   plt.yticks([])
  #  plt.imshow(x_train[i])
 #   img_str = cv2.imencode('.png', x_train[i])[1].tostring()
  #  encoded_img = base64.b64encode(img_str).decode('utf-8')
 #   print(encoded_img)
 #   encoded_images.append(encoded_img)

# Define the model architecture
#model = Sequential()
#model.add(Flatten(input_shape=(32, 32, 3)))
#model.add(Dense(128, activation="relu"))
#model.add(Dense(64, activation="relu"))
#model.add(Dense(10, activation="softmax"))

# Compile the model
#model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

# Train the model
#model.fit(x_train, y_train_cat, batch_size=32, epochs=10, validation_data=(x_test, y_test_cat))

# Evaluate the model on the test set
#_, accuracy = model.evaluate(x_test, y_test_cat)
#print("Accuracy: ", accuracy)

# Test the model on a sample image
#sample_image_index = 15
#sample_image = x_test[sample_image_index]
#plt.imshow(sample_image)
#sample_image = sample_image.reshape([1, 32, 32, 3])
#predictions = model.predict(sample_image)
#predicted_label = np.argmax(predictions)
#actual_label = y_test[sample_image_index][0]
#print("Predicted label: ", predicted_label)
#print("Actual label: ", actual_label)
