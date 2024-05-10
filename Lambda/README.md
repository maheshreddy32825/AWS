# Lambda funcation to copy objects from source S3 to destination S3

## 0. Create S3 Bucket ##
```
Login to AWS console
Go to S3
create two S3 buckets source and destination
```
## 1. Create policy ##
```
Login to AWS console
go to IAM
create policy
Paste code from Lambda/S3CopyLambdaPolicy.txt
create

```
## 2. Create Role
```
under Role create a role
select lambda service
assign the above created policy, AWSLambdaBasicExecutionRole and AWSLambda_FullAccess(cloudwatch log access)
create 
```

## 3. Create Lambda Function
```
Go to lambda
create a function with runtime as PYTHON
under permissions assign Role created above
create
under test tab create a sample test and run to verify if lambda is working as expected
Under code replace code with Lambda/FunctionCopy.txt
add the destination bucket name and save
Hit deploy
```
## 4. Add trigger
```
select the lambda function
Add the trigger
source: s3
Bucket: yoursourcebucketname
select the check box
click on add

```

## 5. Test
```
upload objects (upload files make sure no space in the filenames) on source S3 bucket event trigger lambda and copys the objects to destination s3
```