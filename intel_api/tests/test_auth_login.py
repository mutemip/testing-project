import pytest
from jsonschema import validate
from conftest import intel_auth_url
from rest_framework.test import APIClient



#@pytest.mark.skip
@pytest.mark.django_db(databases=['default'])
@pytest.mark.parametrize("session_key,username",[("lab","dummy@panabios.org"),("ll","victor@koldchain.com")])
def test_login(intel_auth_url,session_key,username):
    url = intel_auth_url
    payload = {
        "session_key":session_key,
        "username": username
    }
    client = APIClient()
    resp = client.post(url, data=payload,format='json')
    data = resp.json() 
#     import pdb
#     pdb.set_trace()
    assert resp.status_code == 200, resp
    assert data['data']['lab_id'] ==10, \
         "Data not matched! Expected : 10, but found : " + data['data']['lab_id']
    assert data['data']['lab_registration_number'] =="d2ad4a04-2aac-476f-83ad-003c2bd82c1e", \
         "Data not matched! Found : " +  data['data']['lab_registration_number'] 
    assert data['data']['user_name'] =="dummy@panabios.org", \
         "Data not matched! Found : " +  data['data']['user_name']  
    assert data['data']['user_group'] =="Lab Admin", \
         "Data not matched! Found : " +  data['data']['user_group'] 




 




