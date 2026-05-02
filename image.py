from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import numpy as np
from tensorflow.keras.preprocessing import image
import os


train_dir = "C:/Users/mauli/Downloads/archive/PetImages"


if os.path.exists("model.h5"):
    print(" Loading saved model...")
    model = load_model("model.h5")

else:
    print(" Training new model...")

    
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )

    train_data = train_datagen.flow_from_directory(
        train_dir,
        target_size=(150,150),
        batch_size=32,
        class_mode='binary',
        subset='training'
    )

    val_data = train_datagen.flow_from_directory(
        train_dir,
        target_size=(150,150),
        batch_size=32,
        class_mode='binary',
        subset='validation'
    )

    
    model = Sequential()

    model.add(Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)))
    model.add(MaxPooling2D(2,2))

    model.add(Conv2D(64,(3,3),activation='relu'))
    model.add(MaxPooling2D(2,2))

    model.add(Conv2D(128,(3,3),activation='relu'))
    model.add(MaxPooling2D(2,2))

    model.add(Flatten())

    model.add(Dense(512,activation='relu'))
    model.add(Dense(1,activation='sigmoid'))

    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    
    model.fit(train_data, epochs=3, validation_data=val_data)

    
    model.save("model.h5")
    print("💾 Model saved!")


img_path  = "C:/Users/mauli/Downloads/dog_images.jpg"  # 👈 apni image ka path daal

img = image.load_img(img_path, target_size=(150,150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0

result = model.predict(img_array)

if result[0][0] > 0.5:
    print("Dog 🐶")
else:
    print("Cat 🐱")