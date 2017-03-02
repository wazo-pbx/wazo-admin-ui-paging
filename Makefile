install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/paging.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-paging
	rm /etc/wazo-admin-ui/conf.d/paging.yml
	systemctl restart wazo-admin-ui
