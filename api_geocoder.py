from flask import Blueprint, jsonify, request, Response
from requests import get
from conf import API_KEY
from logger.logger import writer_log
from calc_distance import calc_distance


api_geo = Blueprint('api_geo', __name__)


@api_geo.route('/geo_data', methods=['GET'])
def get_geo_data() -> Response:
    """контроллер для получения расстояния в километрах от Мкад до 
    другого адреса"""

    # получаем параметр target из запроса
    address = request.args.get('target', None)
    
    # если нет данных в target параметре
    if not address:
        return jsonify({'error': 'Missing target parameter'}),  400
    # если есть мкад в target
    elif 'мкад' in address.lower() or 'mkad' in address.lower():
        return jsonify({'error': 'The address must be outside the MKAD'}),  400
    else:
        target = address.replace(', ', '%2C%').replace(' ', '%20')
    
    yandex_url = 'https://geocode-maps.yandex.ru/1.x/'
    url_geo = f'{yandex_url}?apikey={API_KEY}&geocode={target}&format=json'

    # запрашиваем данные
    response = get(url=url_geo)
    lat_mkad, lon_mkad = 55.898947, 37.632215

    # если get запрос корректный (при ответе 200)
    if response.status_code ==  200:
        try:
            data = response.json()
            # если есть данные по ключам
            if data['response']['GeoObjectCollection']['featureMember']:
                geo_object = data['response']['GeoObjectCollection']\
                    ['featureMember'][0]['GeoObject']
                coordinates = geo_object['Point']['pos'].split()
                lat, lon = float(coordinates[1]), float(coordinates[0])
                # вычисляем дистанцию
                distance = calc_distance(
                    lon1=lon, 
                    lat1=lat, 
                    lon2=lon_mkad, 
                    lat2=lat_mkad
                )
                # записываем в файл лога полученые данные
                writer_log(target=address, distance=round(distance, 6))
                return jsonify({
                    'address1': address, 
                    'address2': 'МКАД', 
                    'distance': round(distance, 6)
                }),  200
            # если нет нужных ключей с данными
            return jsonify({'error': 'The required data is missing'}), 400
        # если данные не в json формате
        except ValueError:
            return jsonify({
                'error': 'Response content is not in JSON format'
            }),  400
    else:
        # при некорректном ответе
        return jsonify({
            'error': 'Unable to get geo_data'
        }), response.status_code
