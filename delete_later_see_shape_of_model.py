from tensorflow import keras

# Load the model
# Replace with the correct path to your model
model_path = 'models/my_model/1/'
model = keras.models.load_model(model_path)

# Get the input shape
input_shape = model.input_shape
print(input_shape)
