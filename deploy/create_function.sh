# remove previous deployment package
rm -f ../deploy_archives/search_engine_metrics.zip
rm -rf ../deploy_archives/current/

# create directory for deployment
mkdir ../deploy_archives/
mkdir ../deploy_archives/current

# install dependencies
pip install -r deploy/requirements.txt --target deploy_archives/current --upgrade

# copy application code to current deployment dir
cp ./search_engine_metrics/* deploy_archives/current/

# create deployment archive
cd ./deploy_archives/current && zip -r ../deploy_archives/search_engine_metrics.zip .

# back to base directory
cd ../../

python deploy/env_setup.py


# running test casess
python search_engine_metrics/data_patterns.py


# copy deployment package to s3
aws s3 cp deploy_archives/search_engine_metrics.zip "s3://${DEPLOY_BUCKET}/" --profile personal

aws lambda create-function \
    	--function-name "search_engine_metrics" \
    	--runtime python3.8 \
    	--code S3Bucket=${DEPLOY_BUCKET},S3Key=search_engine_metrics.zip \
    	--handler "lambda-handler.lambda_function" \
    	--role "${AWS_LAMBDA_ARN}" \
		--timeout 900 \
		--description "Python app to calculate search engine metrics" \
        --profile personal 