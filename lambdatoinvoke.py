import json
import uuid


def lambda_handler(event, context):
    #1 read off the input arguments
    customerId = event['CustomerId']
    
    #2 Generate a random Id
    transactionId = str(uuid.uuid1())
    
    #3 format and return statement
    return {'customerId': customerId,'Success':'true','TransactionId': transactionId}