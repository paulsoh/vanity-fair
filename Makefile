migrate:
	python vanityfair/manage.py makemigrations vanityfair user post
	python vanityfair/manage.py migrate
