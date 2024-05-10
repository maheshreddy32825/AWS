# Lambda funcation to copy objects from source S3 to destination S3

## 0. Create S3 Bucket ##
```
. Login to AWS console
. Go to S3
. Create two S3 buckets source and destination
```
## 1. Create policy ##
```
. Login to AWS console
. Go to IAM
. Create policy
. Paste code from Lambda/S3CopyLambdaPolicy.json
. Create

```
## 2. Create Role
```
. Under Role create a role
. Select lambda service
. Assign the above created policy, AWSLambdaBasicExecutionRole and AWSLambda_FullAccess(cloudwatch log access)
. Create 
```

## 3. Create Lambda Function
```
. Go to lambda
. Create a function with runtime as PYTHON
. Under permissions assign Role created above
. Create
. Under test tab create a sample test and run to verify if lambda is working as expected
. Under code replace code with Lambda/FunctionCopy.py
. Add the destination bucket name and save
. Hit deploy
```
## 4. Add trigger
```
. Select the lambda function
. Add the trigger
. Source: s3
. Bucket: yoursourcebucketname
. Select the check box
. Click on add

```

## 5. Test
```
. Upload objects (upload files make sure no space in the filenames) on source S3 bucket event trigger lambda and copys the objects to destination s3
```