from django.db import models


class Prediction(models.Model):
    # Store the raw input data as a string
    input_data = models.CharField(max_length=255)
    # Store the prediction result as a float
    prediction_result = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Prediction made on {self.created_at}"
