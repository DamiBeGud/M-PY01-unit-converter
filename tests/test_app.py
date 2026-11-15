from fastapi.testclient import TestClient
from unit_converter.app import app
client=TestClient(app)
def test_temperature_and_distance():
    assert client.post('/convert',json={'kind':'temperature','value':100,'source':'C','target':'F'}).json()=={'value':'212.000000','unit':'F'}
    assert client.post('/convert',json={'kind':'distance','value':1250,'source':'m','target':'km'}).json()['value']=='1.250000'
def test_invalid_units_and_bounds():
    assert client.post('/convert',json={'kind':'temperature','value':-274,'source':'C','target':'F'}).status_code==400
    assert client.post('/convert',json={'kind':'distance','value':1,'source':'m','target':'inch'}).status_code==400
    assert client.get('/status').status_code==200
