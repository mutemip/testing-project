from django.urls import reverse,resolve 
import pytest


@pytest.fixture
def intel_auth_url():
	return reverse('intel_api:intel_auth_login')

@pytest.fixture
def intel_lab_regno_url():
	return reverse('intel_api:intel_get_lab_by_registration_number')

@pytest.fixture
def lab_credentials():
 headers = {
		"session-key": "lab",
		"Authorization": "Token bac6a1621bc82c2f0a631a942c9a186e645f2551"
	} 
 return headers
    

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

