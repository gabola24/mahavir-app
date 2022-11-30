

token=$("aws ecr get-login-password --region us-east-1")

$("aws ecr --region us-east-1") 

docker login -u AWS -p token 393640206988.dkr.ecr.us-east-1.amazonaws.com/sentiment

docker tag v1 464349273927.dkr.ecr.us-east-1.amazonaws.com/app-backend

docker push 464349273927.dkr.ecr.us-east-1.amazonaws.com/app-backend