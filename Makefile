lambda_arn = $1

all:
	@echo "Not a valid command. Try 'create-function' or 'update-function'"

create-app:
	@echo "Trying to create function : search engine metrics"
	./environment_export.sh
	./create_function.sh $(lambda_arn)

update-app:
	@echo "Trying to update function : search engine metrics"
	./update_function.sh
