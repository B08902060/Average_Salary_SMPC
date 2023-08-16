#!/usr/bin/python3

import sys

sys.path.append('.')

from client import *
from domains import *

n_parties = int(sys.argv[1])
finish = int(sys.argv[2])
ip = sys.argv[3]
port_num = int(sys.argv[4])

if(len(sys.argv)!=5):
    raise Exception('invalid arguments\nUsage:python3 ./PATH/average_salary.py <n_parties> <finish> <ip> <port number>')


client_id = int(input("Please enter your ID:"))
salary = float(input("Please enter your salary:"))
gender = int(input("\n1.Male 2.Female 3.Other \nPlease choose your gender:"))

if gender not in [1,2,3]:
    raise ValueError("invalid gender type")

client = Client([ip] * n_parties, port_num, client_id)

type = client.specification.get_int(4)

if type == ord('R'):
    domain = Z2(client.specification.get_int(4))
elif type == ord('p'):
    domain = Fp(client.specification.get_bigint())
else:
    raise Exception('invalid type')

for socket in client.sockets:
    os = octetStream()
    os.store(finish)
    os.Send(socket)

multiple = 2 ** 16
client.send_private_inputs([domain(salary * multiple)])
client.send_private_inputs([domain(gender)])

# print('Average Salary is :',(client.receive_outputs(domain, 1)[0].v % 2 ** 64)/multiple)
