import boto3
from time import sleep

cf = boto3.resource('cloudformation')
stack = cf.Stack('TsetNTOP-2')

while stack.stack_status != "CREATE_COMPLETE":
    sleep(5)

with open('/tmp/python.out', 'w+') as f:
    f.write("Finished")
