# Makefile

# Define the name of your git commit message
#GIT_COMMIT_MSG = "modified:   main/serializers.py (updated GetFilterNotificationCountSerializer serializer)"
#GIT_COMMIT_MSG = "3-updated: script like clean code"
GIT_COMMIT_MSG = "6-setup: pytest for unit tests"

# Command for run tests
run_tests:
	python -m pytest

# Command to push a commit to the repository
push:
	git status
	sleep 2
	clear
	echo "# # # # # # # # # # # # # # # # # # # # # # # # #"
	echo "Running to push a commit to the repository"
	echo "# # # # # # # # # # # # # # # # # # # # # # # # #"
	python -m black .
	git add .
	git commit -m $(GIT_COMMIT_MSG)
	git push origin master
	git status
	sleep 2
	clear
	echo "# # # # # # # # # # # # # # # # # # # # # # # # #"
	echo "Done to push a commit to the repository"
	echo "Yahoo everything is working"
	echo "# # # # # # # # # # # # # # # # # # # # # # # # #"
	sleep 2
	clear
