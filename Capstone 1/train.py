from tensorflow.keras import layers
from tensorflow.keras import models
from keras.datasets import mnist
import tensorflow as tf
from tensorflow import keras



def get_model_small(dropout=0.5,inner_layer=128): 

    input_shape = (28,28,1)
    model = models.Sequential()
    model.add(layers.Conv2D(32, kernel_size=(3, 3),
                    activation='relu',
                    input_shape=input_shape))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(dropout))
    model.add(layers.Flatten())
    model.add(layers.Dense(inner_layer, activation='relu'))
    model.add(layers.Dropout(dropout))
    model.add(layers.Dense(num_category, activation='softmax'))
    
    model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(), 
              metrics=['accuracy'])
    
    return model


def get_model_large(dropout=0.5,inner_layer=128): 

    input_shape = (28,28,1)
    model = models.Sequential()
    model.add(layers.Conv2D(32, kernel_size=(3, 3),
                    activation='relu',
                    input_shape=input_shape))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(dropout))
    model.add(layers.Flatten())
    model.add(layers.Dense(100, activation='relu'))
    model.add(layers.Dropout(dropout))
    model.add(layers.Dense(inner_layer, activation='relu'))
    model.add(layers.Dropout(dropout))
    model.add(layers.Dense(num_category, activation='softmax'))
    
    model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(), 
              metrics=['accuracy'])
    
    return model

def model_train(model,num_epoch=2,version='model'):
    batch_size = 256
    checkpoint = keras.callbacks.ModelCheckpoint(
        version+'_{val_accuracy:.3f}.h5',
        save_best_only=True,
        monitor='val_accuracy',
        initial_value_threshold=0.6,
        mode='max'
    )
    
    history = model.fit(X_train, y_train,
            batch_size=batch_size,
            epochs=num_epoch,
            verbose=1,
            callbacks=[checkpoint],
            validation_data=(X_test, y_test))

    return history

def export(model):
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()

    with open('digits.tflite', 'wb') as f_out:
        f_out.write(tflite_model)


(X_train, y_train), (X_test, y_test) = mnist.load_data() 

#Prepare data
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255


num_category = 10
y_train = keras.utils.to_categorical(y_train, num_category)
y_test = keras.utils.to_categorical(y_test, num_category)


#Train model
model = get_model_small(dropout=0.1,inner_layer=100)
history = model_train(model,num_epoch=2,version='model_n')


#Export model
export(model)