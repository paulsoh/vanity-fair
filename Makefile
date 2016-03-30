migrate:
	python vanityfair/manage.py makemigrations user post tag vanityfair
	python vanityfair/manage.py migrate
