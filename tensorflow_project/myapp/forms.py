from django import forms

class PredictionForm(forms.Form):
    input_field = forms.CharField(label='Input for prediction', max_length=1000)