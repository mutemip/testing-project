import os
import grpc
from django.conf import settings

def get_credential():


    #with open(str(settings.BASE_DIR) + "/" + 'rpc_client_app/certs/cred_files/sandbox_roots.pem', 'rb') as f:

    with (open(os.path.join('rpc_client_app/certs/cred_files', 'sandbox_roots.pem'), 'rb')) as f:

        creds = grpc.ssl_channel_credentials(f.read())
    return creds