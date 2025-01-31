# The purpose of this makefile is to update pydantic classes and graph output

VERSION = $(shell git tag | tail -1)

MAKEFLAGS += --warn-undefined-variables

SCHEMA_NAME = ai-risk-ontology
LINKML_SCHEMA_NAME = ai-risk-ontology
SOURCE_SCHEMA_PATH = src/risk_atlas_nexus/ai_risk_ontology/schema

SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN=pipenv run

help: status
	@echo ""
	@echo "make test -- runs tests"
	@echo "make help -- show this help"
	@echo "make regenerate_pydantic -- update pydantic classes"
	@echo "make regenerate_documentation -- regenerate the documentation"
	@echo "make regenerate_graph_output -- export the graph with all instances"
	@echo ""

status: 
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Datafolder: $(SOURCE_SCHEMA_PATH)"

regenerate_documentation:
	gen-doc -d docs/ontology $(SOURCE_SCHEMA_PATH)/${LINKML_SCHEMA_NAME}.yaml

regenerate_pydantic:
	gen-pydantic $(SOURCE_SCHEMA_PATH)/${LINKML_SCHEMA_NAME}.yaml > src/risk_atlas_nexus/ai_risk_ontology/datamodel/ai_risk_ontology.py

regenerate_graph_output:
	python ./src/risk_atlas_nexus/ai_risk_ontology/util/export_graph.py

test:
	pytest
