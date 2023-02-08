# IDS721-Project1
This project is going to write a AWS-based microservice that you can search for the books and add books.
It is based on flask, and use AWS cloud9 as IaC to deploy code and implemented the app inside Azure in cloud.
Github Action is also used to build system.
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
##
1. github action
<img width="342" src="/img/action.jpg">
2. AWS cloud9
<img width="342" src="/img/cloudformation.jpg">
<img width="342" src="/img/stack.jpg">
3. Azure App 
<img width="342" src="/img/azure.jpg">
<img width="342" src="/img/log.jpg">
4. AWS container
![aws_container](https://user-images.githubusercontent.com/122926209/217411225-ce9c842a-ed25-4143-978e-0c83b40ed07b.jpg)
5. AWS Elastic Container Registry
![aws_EC](https://user-images.githubusercontent.com/122926209/217411406-fe15d12c-859d-4660-8e8e-4a995e1bc4a2.jpg)

## Web
my web link is: 
in Azure(https://book-search.azurewebsites.net/) 
in AWS App Runner: https://9ecvjbmkyb.us-east-1.awsapprunner.com/
1. index page
<img width="342" src="/img/index_page.jpg">
2. add page
<img width="342" src="/img/add_page.jpg">
3. search page
<img width="342" src="/img/search_page.jpg">
