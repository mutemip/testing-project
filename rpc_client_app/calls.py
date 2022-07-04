import grpc
# from google.protobuf.json_format import MessageToJson
from panabios_rpc.lab_test_proto import lab_test_pb2,lab_test_pb2_grpc
from django.conf import settings
from panabios_rpc.userprofile_proto import user_profile_pb2,user_profile_pb2_grpc
import json
# import logging
from rpc_client_app.certs.get_creds import get_credential
from panabios_rpc.lab import lab_pb2,lab_pb2_grpc

def retrieve_labtest(id):
    with grpc.secure_channel('{}:{}'.format(settings.RPC_SERVER_HOST,settings.RPC_SERVER_PORT),get_credential()) as channel:
        stub = lab_test_pb2_grpc.LabTestControllerStub(channel)
        try:
            obj = stub.Retrieve(lab_test_pb2.LabTestRetrieveRequest(id=id))
            return obj
        except Exception as e:
            return None 


def all_tests():
    tests = list()
    with grpc.secure_channel('{}:{}'.format(settings.RPC_SERVER_HOST,settings.RPC_SERVER_PORT),get_credential()) as channel:
        stub = lab_test_pb2_grpc.LabTestControllerStub(channel)
        for labtest in stub.List(lab_test_pb2.LabTestListRequest()):
            tests.append(labtest.id)
        return tests



def fetch_user_profile(username):
    with grpc.secure_channel('{}:{}'.format(settings.RPC_SERVER_HOST,settings.RPC_SERVER_PORT),get_credential()) as channel:
        stub = user_profile_pb2_grpc.UserProfileControllerStub(channel)
        try:
            obj = stub.RetrieveUserProfile(user_profile_pb2.UserProfileRetrieveRequest(username=username))
            return obj
        except Exception as e:
            return None

def fetch_user_lab(userprofile_id):
    with grpc.secure_channel('{}:{}'.format(settings.RPC_SERVER_HOST,settings.RPC_SERVER_PORT),get_credential()) as channel:
        stub = user_profile_pb2_grpc.UserProfileControllerStub(channel)
        try:
            obj = stub.RetrieveUserLab(user_profile_pb2.UserProfileLabRetrieveRequest(userprofile_id=userprofile_id))
            return obj
        except Exception as e:
            return None

def retrieve_lab(lab_id):
    with grpc.secure_channel('{}:{}'.format(settings.RPC_SERVER_HOST,settings.RPC_SERVER_PORT),get_credential()) as channel:
        stub = user_profile_pb2_grpc.UserProfileControllerStub(channel)
        try:
            obj = stub.RetrieveLab(user_profile_pb2.LabRetrieveRequest(lab_id=lab_id))
            return obj
        except Exception as e:
            return None

def get_lab_by_registration_number(reg_number):
    with grpc.secure_channel('{}:{}'.format(settings.RPC_SERVER_HOST,settings.RPC_SERVER_PORT),get_credential()) as channel:
        stub = lab_pb2_grpc.LabControllerStub(channel)
        try:
            lab = stub.GetLabByRegistrationNumber(lab_pb2.RegNumberRequest(registration_number=reg_number))
            return lab

        except Exception as e:
            return None

def get_lab_by_lab_name(lab_name):
    with grpc.secure_channel('{}:{}'.format(settings.RPC_SERVER_HOST,settings.RPC_SERVER_PORT),get_credential()) as channel:
        stub = lab_pb2_grpc.LabControllerStub(channel)
        try:
            lab = stub.GetLabByLabName(lab_pb2.LabNameRequest(lab_name=lab_name))
            return lab
        except Exception as e:
            return None




