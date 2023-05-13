# InvokeAwslambdaFunctionFromAnotherLambda
we first create a new lambda client instance using the boto3 library ,we  then define a handler function named lambda_handler which will be triggered when this Lambda function is invoked. 
Inside this function, we create a dictionary called inputForInvoker which contains the input parameters to be passed to the Lambda function we want to invoke.

We then use the invoke() method of the lambda client to invoke the Lambda function we want to call. The FunctionName parameter specifies the ARN (Amazon Resource Name) of the Lambda function we want to call. The InvocationType parameter specifies whether we want to invoke the function synchronously (i.e., RequestResponse) or asynchronously (i.e., Event). Finally, we pass the input parameters as a JSON string in the Payload parameter.

The invoke() method returns a response object which contains the output of the invoked function. We then load this output from the Payload attribute of the response object as a JSON object using the json.load() method and print it to the console.
