
# def test_about(client):
#     response = client.get('/about/')
#     assert response.status_code == 200
#     response = response.content.decode('utf-8')
#     assert 'Текст о нас' in response
#
#
# def test_contacts(client):
#     response = client.get('/contacts/')
#     assert response.status_code == 200
#     response = response.content.decode('utf-8')
#     assert 'Контакты' in response
