# flake8: noqa
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from joblib import load
from rest_framework.viewsets import ViewSet
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter, OpenApiTypes
from apps.api.serializers import PredictionInputSerializer


class HeartDiseasePredictionViewSet(ViewSet):
    @extend_schema(
        description="Predict heart disease.",
        request=PredictionInputSerializer,
        responses={
            200: PredictionInputSerializer,
        },
        examples=[
            OpenApiExample(
                name="Example Request",
                value={
                    "age": 60.0,
                    "sex": 1.0,
                    "trestbps": 140.0,
                    "chol": 293.0,
                    "fbs": 0.0,
                    "thalach": 170.0,
                    "exang": 0.0,
                    "oldpeak": 1.2,
                    "ca": 2.0,
                    "cp_0": 0.0,
                    "cp_1": 0.0,
                    "cp_2": 0.0,
                    "cp_3": 1.0,
                    "restecg_0": 0.0,
                    "restecg_1": 0.0,
                    "restecg_2": 1.0,
                    "slope_0": 0.0,
                    "slope_1": 1.0,
                    "slope_2": 0.0,
                    "thal_0": 0.0,
                    "thal_1": 0.0,
                    "thal_2": 1.0
                },
            ),
        ]
    )
    def create(self, request):
        loaded_model = load(
            '/home/viniciusmb/Projects/python/heart_disease/App/bin/best_random_forest_model.joblib')

        # Receber os dados da requisição POST
        input_data = request.data

        # Preencher valores faltantes com zero
        input_data_filled = {
            "age": input_data.get("age", 0.0),
            "sex": input_data.get("sex", 0.0),
            "trestbps": input_data.get("trestbps", 0.0),
            "chol": input_data.get("chol", 0.0),
            "fbs": input_data.get("fbs", 0.0),
            "thalach": input_data.get("thalach", 0.0),
            "exang": input_data.get("exang", 0.0),
            "oldpeak": input_data.get("oldpeak", 0.0),
            "ca": input_data.get("ca", 0.0),
            "cp_0": input_data.get("cp_0", 0.0),
            "cp_1": input_data.get("cp_1", 0.0),
            "cp_2": input_data.get("cp_2", 0.0),
            "cp_3": input_data.get("cp_3", 0.0),
            "restecg_0": input_data.get("restecg_0", 0.0),
            "restecg_1": input_data.get("restecg_1", 0.0),
            "restecg_2": input_data.get("restecg_2", 0.0),
            "slope_0": input_data.get("slope_0", 0.0),
            "slope_1": input_data.get("slope_1", 0.0),
            "slope_2": input_data.get("slope_2", 0.0),
            "thal_0": input_data.get("thal_0", 0.0),
            "thal_1": input_data.get("thal_1", 0.0),
            "thal_2": input_data.get("thal_2", 0.0),
        }

        # Preprocessar os dados conforme necessário (transformar em array 2D)
        sample_input = np.array([list(input_data_filled.values())])

        # Fazer a previsão usando o modelo carregado
        prediction = loaded_model.predict(sample_input)
        prediction_proba = loaded_model.predict_proba(sample_input)

        # Formatar a resposta
        response_data = {
            "prediction": prediction[0],
            "probabilities": [x * 100 for x in prediction_proba[0].tolist()]
        }

        return Response(response_data, status=status.HTTP_200_OK)
