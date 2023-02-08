# IDS721-Project1: Cloud Continuous Delivery of Microservice
In project 1, our target is to create a microservice in Flask. My project is going to write a AWS-based microservice that you can search for the books and add books.It is based on flask, and use AWS cloud9 as IaC to deploy code and implemented the app inside AWS App Runner in cloud. I create a customized docker container to deploy this application. Then push image to AWS EDR. Thus the code in aws will automatically update with github.Github Action is also used to build system to show the workflow.
## SetUp
1. Create venv
```terminal
python3 -m venv env
source env/bin/activate
```
2. Install requirements
```python
make install
```
3. run it
```python
python app.py
```
## Implement
1. github action
<img width="500" src="/img/action.jpg">
2. AWS cloud9
<img width="500" src="/img/cloudformation.jpg">
<img width="500" src="/img/stack.jpg">
3. App Runner
<img width="500" src="/img/aws_app.jpg">
4. AWS container
<img width="500" src="/img/aws_container.jpg">
5. AWS Elastic Container Registry
<img width="500" src="/img/aws_EC.jpg">

## Web Function
my web link is: 
in Azure(https://book-search.azurewebsites.net/) 
in AWS App Runner: https://9ecvjbmkyb.us-east-1.awsapprunner.com/
1. index page
<img width="500" src="/img/index_page.jpg">
2. add page
<img width="500" src="/img/add_page.jpg">
3. search page
<img width="500" src="/img/search_page.jpg">
