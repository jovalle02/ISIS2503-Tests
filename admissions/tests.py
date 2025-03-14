import json
import requests_mock
from django.test import TestCase
from django.http import JsonResponse
from admissions.models import Admission
from admissions.views import admitir_paciente

class AdmissionTests(TestCase):

    @requests_mock.Mocker()
    def test_admit_patient_success(self, mock_request):
        """Test admitting a patient when there are available beds"""
        # Mock the API response
        mock_request.get("http://127.0.0.1:8000/api/camas/disponibles/", json={"camas_disponibles": 5})

        # Call the function
        response = admitir_paciente(None)

        # Decode JSON response correctly
        data = json.loads(response.content.decode("utf-8"))

        # Assert the response is a success
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["mensaje"], "Paciente admitido exitosamente")

    @requests_mock.Mocker()
    def test_admit_patient_failure(self, mock_request):
        """Test admitting a patient when no beds are available"""
        # Mock the API response
        mock_request.get("http://127.0.0.1:8000/api/camas/disponibles/", json={"camas_disponibles": 0})

        # Call the function
        response = admitir_paciente(None)

        # Decode JSON response correctly
        data = json.loads(response.content.decode("utf-8"))

        # Assert the response fails
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "No hay camas disponibles")
