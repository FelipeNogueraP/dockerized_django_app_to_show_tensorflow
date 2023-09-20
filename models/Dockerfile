# Use the official TensorFlow Serving image as the base image
FROM tensorflow/serving

# Set environment variables
ENV MODEL_NAME=my_model
ENV MODEL_VERSION=1

# Expose ports
EXPOSE 8501

# Set the entrypoint to run TensorFlow Serving with your model
ENTRYPOINT [ "tensorflow_model_server", "--rest_api_port=8501", "--model_name=my_model", "--model_base_path=/models/my_model" ]
