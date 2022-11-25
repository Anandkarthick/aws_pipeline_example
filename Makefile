lambda_arn = $1

all:
	@echo "Not a valid command. Try 'create-function' or 'update-function'"

create-app:
	@echo "Trying to create function : search engine metrics"
	deploy/environment_export.sh
	deploy/create_function.sh $(lambda_arn)

update-app:
	@echo "Trying to update function : search engine metrics"
	deploy/update_function.sh
