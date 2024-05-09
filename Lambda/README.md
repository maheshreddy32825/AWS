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
assign the above created policy
create 
```

## 3. Create Lambda Function
```
Go to lambda
create a function
paste code Lambda/FunctionCopy.txt
create
```

## 4. Test
```
upload files on source S3 bucket event trigger lambda and copys the objects to destination s3
```