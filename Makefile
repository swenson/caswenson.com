default: style.css blog

.PHONY: default blog

blog:
	python make_blog.py

style.css: style.scss _normalize.scss
	sassc style.scss $@
	cp $@ static/
