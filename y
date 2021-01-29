version = 0.1
[y]
[y.deploy]
[y.deploy.parameters]
stack_name = "todo-list-aws"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-5o7xoj5nq4pn"
s3_prefix = "todo-list-aws"
region = "us-east-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
parameter_overrides = "stage=\"develop\" service=\"serverless-rest-api-with-dynamodb\" serviceTest=\"todo-list-aws\""

[default]
[default.deploy]
[default.deploy.parameters]
stack_name = "todo-list-aws"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-5o7xoj5nq4pn"
s3_prefix = "todo-list-aws"
region = "us-east-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
parameter_overrides = "stage=\"develop\" service=\"serverless-rest-api-with-dynamodb\" serviceTest=\"todo-list-aws\""
