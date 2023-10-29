# flake8: noqa
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from joblib import load
from rest_framework.viewsets import ViewSet
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter, OpenApiTypes
from bin.pre_process_data import process_data
from apps.api.serializers import PredictionInputSerializer


class HeartDiseasePredictionViewSet(ViewSet):
    column_categories = {
        'age': 'Exemplo: 45',
        'sex': 'Exemplo: 0 (Feminino) ou 1 (Masculino)',
        'cp': 'Exemplo: 1 (Angina típica), 2 (Angina atípica), 3 (Dor não anginal), 4 (Assintomático)',
        'trestbps': 'Exemplo: 130 (mm Hg)',
        'chol': 'Exemplo: 220 (mg/dl)',
        'fbs': 'Exemplo: 1 (Açúcar no sangue em jejum > 120 mg/dl) ou 0 (Açúcar no sangue em jejum <= 120 mg/dl)',
        'restecg': 'Exemplo: 0 (Normal), 1 (Anormalidades de ST-T), 2 (Hipertrofia Ventricular Esquerda Provável)',
        'thalach': 'Exemplo: 150 (bpm - batimentos por minuto)',
        'exang': 'Exemplo: 1 (Sim - Angina induzida por exercício) ou 0 (Não - Sem angina induzida por exercício)',
        'oldpeak': 'Exemplo: 1.5 (Depressão do segmento ST induzida por exercício)',
        'slope': 'Exemplo: 1 (Subida), 2 (Plano), 3 (Descida)',
        'ca': 'Exemplo: 2 (Número de principais vasos coloridos por fluoroscopia)',
        'thal': 'Exemplo: 3 (Normal), 6 (Defeito fixo), 7 (Defeito reversível)',
        'num': 'Exemplo: 0 (Sem doença), 1, 2, 3, ou 4 (Diferentes níveis de doença)',
        'colesterol_class': 'Exemplo: "Desejável", "Limítrofe alto", "Alto"'
    }

    @extend_schema(
        description="Predict heart disease.",
        request=PredictionInputSerializer,
        responses={
            200: PredictionInputSerializer,
        },
        examples=[
            OpenApiExample(
                name="Example Request",
                value=column_categories
            ),
        ]
    )
    def create(self, request):
        loaded_model = load(
            '/home/viniciusmb/Projects/python/heart_disease/App/bin/best_models/MLP.joblib')

        # Receber os dados da requisição POST
        input_data = request.data
        print(f"Input data: {input_data} - {type(input_data)}")

        # Preencher valores faltantes com zero
        input_data_filled = {
            key: float(input_data.get(key, 0.0)) for key in self.column_categories.keys()
        }

        sample_input = process_data(input_data_filled)

        print(f"Sample input: {sample_input} - {type(sample_input)}")

        # Fazer a previsão usando o modelo carregado
        prediction = loaded_model.predict(sample_input)
        prediction_proba = loaded_model.predict_proba(sample_input)

        print(f"Prediction: {prediction} - {type(prediction)}")
        print(f"Prediction proba: {prediction_proba} - {type(prediction_proba)}")

        # Formatar a resposta
        response_data = {
            "prediction": prediction[0],
            "probabilities": [x * 100 for x in prediction_proba[0].tolist()]
        }

        return Response(response_data, status=status.HTTP_200_OK)
