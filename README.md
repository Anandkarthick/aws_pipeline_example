### Python Application to calculate search engine metrics.

### Pre-requisities

- Valid AWS account with access key and secret
- run aws configure to set up a profile "personal" with the account

### High level flow of the problem

![high level flow - business problem ](search_engine.jpg)


### Local execution

Create virtual environment with python 3.9

```bash
python3.9 -m venv .venv
```

check version of the virtual environment

```bash
.venv/bin/python --version
```

run following command to active
```bash
source .venv/bin/activate
```

to deactivate, type
```bash
deactivate
```

### Deployment

Make file is created to deploy the function easily in AWS as lambda function. Any dependencies should be specified in requirements.txt before the packge is deployed. 

```bash
make create-app
```

- Installs dependencies from requirements.txt 
- creates deployment package
- creates lambda function

```bash
make update-app
```

- Installs dependencies from requirements.txt 
- creates deployment package
- updates lambda function

