test:
	@clear
	nosetests -dvs

test-workers:
	@clear
	nosetests -dsv tests/test_worker_*.py

test-x:
	@clear
	nosetests -dvsx

doc:
	@clear
	./make-docs.sh -vg

clean:
	rm -rf MANIFEST build/ dist/ pypln.egg-info/ reg-settings.py*
	find -regex '.*\.pyc' -exec rm {} \;
	find -regex '.*~' -exec rm {} \;


.PHONY:	test test-x doc clean test-workers
