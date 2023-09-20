import tensorflow as tf

# Define a simple model


def simple_model():
    """Create a tensorflow dummy model to test the project"""
    input_layer = tf.keras.layers.Input(shape=(1,), name='input_layer')
    output_layer = tf.keras.layers.Dense(
        1, activation='linear', name='output_layer')(input_layer * 2)

    # Create a Model from the layers
    model = tf.keras.models.Model(inputs=input_layer, outputs=output_layer)

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    return model


# Instantiate and save the model
model = simple_model()
model.save("models/my_model/1/")
