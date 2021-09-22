import json
import datetime

def batting(event, context):
    print("Messaage receieved from step function :");
    print(event);
    
    response={};
    response['batting']=event['batting']
    response['Currenttime']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response['Message']='Hello from the batting Lambda'
    
    return response
    