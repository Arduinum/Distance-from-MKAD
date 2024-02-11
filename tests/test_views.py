import unittest
from app import app


class TestViewsApiGeocoder(unittest.TestCase):
    """Тесты view для Geocoder"""

    def setUp(self):
        """готовим приложение перед тестом"""
        self.app = app.test_client()
        self.context = app.app_context()
        self.context.push()
    
    def tearDown(self):
        """очистка данных после теста"""
        self.context.pop()
    
    def test_get_data_200(self):
        """тест корректного запроса"""
        response = self.app.get('/geo_data?target=Нижний%20Новгород')
        self.assertEqual(response.status_code, 200)

    def test_get_data_no_parametrs_400(self):
        """тест без параметров"""
        response = self.app.get('/geo_data')
        self.assertEqual(response.status_code, 400)

    def test_get_data_mkad_400(self):
        """тест с на исключение мкад из ответа"""
        response = self.app.get(
            '/geo_data?target=МКАД%2C%71-й%20километр%2C%Москва'
        )
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    # запуск тестов
    unittest.main()
