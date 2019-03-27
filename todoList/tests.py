from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Tarea
import json

# Create your tests here.
class TestTodoList(APITestCase):
    
    def setUp(self):
        # arrange
        self.tarea1 = Tarea.objects.create(nombre="test1")
        self.tarea2 = Tarea.objects.create(nombre="test2")
    
    def test_get_todolist(self):
        # act
        response = self.client.get("/lista/")
        response_content = json.loads(response.content.decode('utf8'))
        
        # assert
        self.assertEqual(type(response_content), list)
        self.assertEqual(
            response_content, 
            [{'nombre': self.tarea1.nombre}, {'nombre': self.tarea2.nombre}])
        