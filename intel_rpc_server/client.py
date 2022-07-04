import grpc

from google.protobuf.json_format import MessageToJson
from intel_rpc.userbookservice import user_book_service_pb2,user_book_service_pb2_grpc



print("################ User Book Service clients #############################")

with grpc.insecure_channel('localhost:50051') as channel:
    stub = user_book_service_pb2_grpc.UserBookServiceControllerStub(channel)

    print("----------Get User Book Service By code-------------")
    try:
        user_book_service = stub.GetBookedServiceByCode(user_book_service_pb2.UserBookServiceCodeRequest(code="BO45368021"))
        print(MessageToJson(user_book_service))

    except Exception as e:
        import pdb; pdb.set_trace()
        print(json.dumps({"error":"Not Found"}))


