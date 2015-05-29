# Shell to use with Make
SHELL := /bin/sh

# Set important Paths
PROJECT := pelawak
LOCALPATH := $(CURDIR)/$(PROJECT)
PYTHONPATH := $(LOCALPATH)/
PYTHON_BIN := $(VIRTUAL_ENV)/bin

# Production Settings
DJANGO_SETTINGS_MODULE = $(PROJECT).settings
DJANGO_POSTFIX := --settings=$(DJANGO_SETTINGS_MODULE) --pythonpath=$(PYTHONPATH)

# Apps to test
APPS := pelawak

# Export targets not associated with files
.PHONY: test showenv coverage bootstrap pip virtualenv clean virtual_env_set

# Show Virtual Environment
showenv:
	@echo 'Environment:'
	@echo '------------------------'
	@$(PYTHON_BIN)/python -c "import sys; print 'sys.path:', sys.path"
	@echo 'PYTHONPATH:' $(PYTHONPATH)
	@echo 'PROJECT:' $(PROJECT)
	@echo 'DJANGO_SETTINGS_MODULE:' $(DJANGO_SETTINGS_MODULE)
	@echo 'DJANGO_LOCAL_SETTINGS_MODULE:' $(DJANGO_LOCAL_SETTINGS_MODULE)
	@echo 'DJANGO_TEST_SETTINGS_MODULE:' $(DJANGO_TEST_SETTINGS_MODULE)
	@echo 'VIRTUAL_ENV:' $(VIRTUAL_ENV)

# Show help for Django
djangohelp:
	$(PYTHON_BIN)/django-admin.py help $(DJANGO_POSTFIX)

# Run the development server
runserver:
	$(PYTHON_BIN)/django-admin.py runserver $(DJANGO_POSTFIX)

# Clean build files
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf $(PROJECT)/*.egg-info

# Targets for Django testing
test:
	$(PYTHON_BIN)/coverage run --source=$(LOCALPATH) $(LOCALPATH)/manage.py test $(LOCALPATH) $(DJANGO_POSTFIX)
	- $(PYTHON_BIN)/coverage report
