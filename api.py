import requests

base_url='https://petstore.swagger.io/v2'

def test_get_request():
    """тест для GET-запроса, питомцы в наличии"""
    response = requests.get(f'{base_url}/pet/findByStatus?status=availible')
    print(response.json())
    assert response.status_code == 200

def test_post_request():
    """тест для запроса POST, add a new pet"""
    json_data = {
        "id": 1,
        "category": {
            "id": 1,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 1,
                "name": "string"
            }
        ],
        "status": "available"
    }
    headers = {'Content-type': 'application/json'}
    response = requests.post(f'{base_url}/pet', json=json_data, headers=headers)
    print(response.json())
    assert response.status_code == 200

def test_delete_request():
    """тест для запроса DELETE, удаляем питомца"""
    response = requests.delete(f'{base_url}/pet/1')
    print(response.json())
    assert response.status_code == 200

def test_put_request():
    """тест для запроса PUT, обновление информации о питомце"""
    json_data = {
        "id": 1,
        "category": {
            "id": 1,
            "name": "string"
        },
        "name": "doggie updated",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 1,
                "name": "string"
            }
        ],
        "status": "available"
    }
    headers = {'Content-type': 'application/json'}
    response = requests.put(f'{base_url}/pet', json=json_data, headers=headers)
    print(response.json())
    assert response.status_code == 200