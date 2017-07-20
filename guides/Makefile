PROJECT = project
.DEFAULT_GOAL := help

help:                ## Show available options with this Makefile
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

test_clean:          ## Remove all the docker containers.
test_clean:
	cd docker && docker-compose down -v

test_recreate_env:        ## Recreate the docker environment and create a default topic.
test_recreate_env:    test_clean
	cd docker && \
	docker-compose up -d && \
	chmod +x ./wait-for-it.sh && \
	./wait-for-it.sh localhost:19092 --timeout=0 --	docker exec -it kafka_test /usr/bin/kafka-topics --create --zookeeper localhost:22181 --replication-factor 1 --partitions 100 --topic test_produce_consume_with_partition_key_topic

test_all:            ## Test all will run all the tests in Shazam and generate coverage reports.
test_all:	test_recreate_env
	@echo "Run your test commands" && \
	pip uninstall -y $(PROJECT) || true && \
	pip install -e . --upgrade && \
	py.test --cov-report term-missing  --cov=$(PROJECT) tests/ -s -v

test_file:           ## This will test only one specific file
test_file:    test_recreate_env
	@echo "Run your test commands" && \
	pip uninstall -y $(PROJECT) || true && \
	pip install -e . --upgrade && \
	py.test --cov-report term-missing  --cov=$(PROJECT) $(file) -s -v

test_command:           ## This will test only one specific file
test_command:    test_recreate_env
	@echo "Run your test commands" && \
	$(command)

test_end2end:        ## Test end2end of project's functionality.
test_end2end:    test_recreate_env
	@echo "Run your test commands" && \
	pip uninstall -y $(PROJECT) || true && \
	pip install -e . --upgrade && \
	python tests/end2end.py


install_doc_deps:    ## Install sphinx dependencies
install_doc_deps:
	@pip install sphinx sphinx_rtd_theme

.PHONY: docs
docs:                ## Generate all the docs
docs:    install_doc_deps
	@cd docs && sphinx-apidoc -f -o source/ ../$(PROJECT) && make html
	@echo "docs are generated in docs/bu
