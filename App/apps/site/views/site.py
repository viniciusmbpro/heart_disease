# flake8: noqa
import requests
from django.shortcuts import render
from apps.site.forms import HeartDiseasePredictionForm


def prediction_form(request):
    form = HeartDiseasePredictionForm()

    if request.method == 'POST':
        # Extrair os dados do formulário
        data = request.POST
        
        url_base = "http://127.0.0.1:8000/api/heart_disease/"
        headers = {'content-type': 'application/json'}

        # Enviar os dados para a API
        response = requests.post(url_base, json=data, headers=headers)

        if response.status_code == 200:
            prediction_result = response.json()
        else:
            prediction_result = "Error while making prediction"

        return render(request, 'site/prediction_form.html', {'form': form, 'prediction_result': prediction_result})

    return render(request, 'site/prediction_form.html', {'form': form})
