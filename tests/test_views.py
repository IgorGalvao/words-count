class TestViews:
  def test_index_get(self, client):
    response = client.get('/')
    assert response.status_code == 200


  def test_index_post(self, client):
    form_data = {
      'text_data': 'This is a test'
    }
    response = client.post('/', data=form_data)

    assert response.status_code == 200
    assert "Number of words in text: 4" in response.data.decode('utf-8')


  def test_index_post_with_no_data(self, client):
    form_data = {}
    response = client.post('/', data=form_data)

    assert response.status_code == 400
    assert "400 Bad Request" in response.data.decode('utf-8')
