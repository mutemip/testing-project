from .service import UserBookServiceServices
from intel_rpc.userbookservice import user_book_service_pb2_grpc

def grpc_handlers(server):
    user_book_service_pb2_grpc.add_UserBookServiceControllerServicer_to_server(UserBookServiceServices.as_servicer(), server)