.PHONY: prepare check-env
prepare: check-env
	docker run \
	--env TASK --rm -v ${PWD}:/var/www -w /var/www \
	-u $$(id -u ${USER}):$$(id -g ${USER}) \
	-v $(PWD):/repo \
	hairyhenderson/gomplate:v3.11.3-alpine \
	--input-dir /repo/tasks/template --output-dir /repo/tasks/$(TASK)

check-env:
ifndef TASK
	$(error Environment variable TASK is undefined)
endif