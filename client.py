import grpc

import main_pb2
import main_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = main_pb2_grpc.gRPCExerciseStub(channel)

print("Hello and welcome to my super awesome gRPC client!")
print("==================================================")
print("This app will add any two int32-base numbers and return the int32-base result of their addition")

while True:
    num1 = input("What's your first number? ")
    num2 = input("What's your second number? ")
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError as e:
        print("Please use only int32-base numbers")
        continue
    break


result = stub.add2Numbers(main_pb2.Elements(elmt1=num1, elmt2=num2))

print(f"\nThe result is: {result.result}")
