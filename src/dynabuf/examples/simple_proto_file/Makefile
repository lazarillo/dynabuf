CURRENT_DIR := $(shell pwd)
CURRENT_USER_GROUP := $(shell id -u):$(shell id -g)

.PHONY: all
all: generate-proto

.PHONY: clean
clean:
	rm -rf build

.PHONY: generate-proto
generate-proto: clean
	mkdir build # if docker creates the build folder the current user will not have permissions to write on it
	echo current dir: $(CURRENT_DIR)
	docker run --volume "$(CURRENT_DIR):/workspace" --workdir /workspace bufbuild/buf:1.40.1 generate
