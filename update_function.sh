
# remove previous deployment package
rm -f /deploy_archives/search_engine_metrics.zip
rm -rf /deploy_archives/current

# create directory for deployment
mkdir deploy_archives/current

# install dependencies
pip install -r requirements.txt --target ./deploy_archives/current

# copy modules to current deployment dir
cp -r ./search_engine_metrics/modules/ deploy_archives/current/

# copy application code to current deployment dir
cp ./search_engine_metrics/* deploy_archives/current/

# create deployment archive
cd ./deploy_archives/current && zip -r ../../deploy_archives/search_engine_metrics.zip .

# back to base directory
cd ../../

python env_setup.py

# running test cases

python search_engine_metrics/data_patterns.py

aws lambda update-function-code \
    	--function-name "search_engine_metrics" \
    	--zip-file "fileb://deploy_archives/search_engine_metrics.zip" \
        --profile personal