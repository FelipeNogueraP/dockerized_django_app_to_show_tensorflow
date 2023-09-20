from django.shortcuts import render
from django.utils import timezone
from .models import Prediction
import requests
from django.http import JsonResponse
import json


def home(request):
    return render(request, 'myapp/home.html')


def predict(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data')

        # Validate input_data here (if necessary)
        if not input_data:
            return JsonResponse({'error': 'Input data is required'}, status=400)

        try:
            # Attempt to parse the input data as JSON
            parsed_data = json.loads(input_data)
        except json.JSONDecodeError:
            # If JSON decoding fails, return an error response
            return JsonResponse({'error': 'Invalid input data format'}, status=400)

        # Additional validation can be added here based on the specific requirements of your model

        try:
            # Make a request to the TensorFlow Serving server
            response = requests.post(
                "http://tf_serving:8501/v1/models/my_model:predict",
                # Wrap parsed_data in a list to form a batch
                json={"instances": [parsed_data]}
            )

            # Check if the request was successful
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            return JsonResponse({'error': str(e)}, status=400)

        try:
            # Get prediction re∫sult
            # Extract the first prediction result
            # Extract the single number from the list
            prediction_result = response.json()["predictions"][0][0]
        except (KeyError, IndexError, ValueError) as e:
            # Handle JSON decode errors
            return JsonResponse({'error': 'Invalid response from prediction server'}, status=500)

        # Create a new prediction record in the database
        Prediction.objects.create(
            input_data=input_data,
            prediction_result=prediction_result,
        )

        return render(request, 'myapp/result.html', {'prediction_result': prediction_result})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
