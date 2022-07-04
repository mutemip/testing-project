import pytest
from jsonschema import validate
from rest_framework.test import APIClient

#@pytest.mark.skip
@pytest.mark.django_db(databases=['default'])
@pytest.mark.parametrize("lab_regno",[("d2ad4a04-2aac-476f-83ad-003c2bd82c1e"),("d2ad4a04-gfdfgdc-476f-83ad-003c2bd82c1e")])
def test_fetch_byregno(intel_lab_regno_url,lab_credentials,lab_regno):
    url = intel_lab_regno_url + "?reg_number="+ lab_regno
    client = APIClient()
    resp = client.get(url, headers=lab_credentials)
    data = resp.json()
#     import pdb
#     pdb.set_trace()
    assert resp.status_code == 200, resp
    assert data['data']['id'] ==10, \
         "Data not matched! Found : " +data['data']['id']
    assert data['data']['name'] =="Ghana Reference Laboratory", \
         "Data not matched! Found : " +  data['data']['name']
    assert data['data']['country'] =="Ghana", \
         "Data not matched! Found : " +  data['data']['country']
    assert data['data']['streetAddress1'] =="Korlebu", \
         "Data not matched! Found : " +  data['data']['streetAddress1'] 
    assert data['data']['streetAddress2'] =="Korlebu", \
         "Data not matched! Found : " +  data['data']['streetAddress2']  
    assert data['data']['email'] =="dummylab@panabios.org", \
         "Data not matched! Found : " +  data['data']['email'] 
    assert data['data']['registrationNumber'] =="d2ad4a04-2aac-476f-83ad-003c2bd82c1e", \
         "Data not matched! Found : " +  data['data']['registrationNumber'] 
    assert data['data']['phoneNumber'] =="(+233)001010469", \
         "Data not matched! Found : " +  data['data']['phoneNumber'] 



                

 




