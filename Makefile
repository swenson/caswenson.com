default: style.css blog

.PHONY: default blog

blog:
	python3 make_blog.py

style.css: style.scss _normalize.scss
	sassc style.scss $@
	cp $@ static/
