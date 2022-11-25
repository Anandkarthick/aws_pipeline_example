### Python Application to calculate search engine metrics.



### Deployment

Make file is created to deploy the function easily in AWS as lambda function. Any dependencies should be specified in requirements.txt before the packge is deployed. 

```
make create-app
```

- Installs dependencies from requirements.txt 
- creates deployment package
- creates lambda function

```
make update-app
```

- Installs dependencies from requirements.txt 
- creates deployment package
- creates lambda function

