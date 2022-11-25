
pip install -r requirements.txt --target ./search_engine_metrics/modules/

zip -r ./deploy_archives/search_engine_metrics.zip ./search_engine_metrics 

python env_setup.py

aws lambda create-function \
    	--function-name "search_engine_metrics" \
    	--runtime python3.9 \
    	--zip-file "fileb://deploy_archives/search_engine_metrics.zip" \
    	--handler "lambda-handler.lambda_function" \
    	--role "${AWS_LAMBDA_ARN}" \
		--timeout 900 \
		--description "Python app to calculate search engine metrics"
        --profile personal