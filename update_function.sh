
pip install -r requirements.txt --target ./search_engine_metrics/modules/

zip -r ./deploy_archives/search_engine_metrics.zip ./search_engine_metrics 

python env_setup.py

aws lambda update-function-code \
    	--function-name "search_engine_metrics" \
    	--zip-file "fileb://deploy_archives/search_engine_metrics.zip" \
        --profile personal