import json
import datetime

def bowling(event, context):
    print("Messaage receieved from step function :");
    print(event);
    
    response={};
    response['bowling']=event['bowling']
    response['Currenttime']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response['Message']='Hello from the bowling Lambda'
    
    return response
    