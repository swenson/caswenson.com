#!/usr/bin/env python2.7

from datetime import date
import glob
import os
import os.path
import shutil
import string
import subprocess as sp

DISQUS_SHORTNAME = "swenson"

MARKDOWN = glob.glob("vendor/markdown*/Markdown.pl")[0]

def run_cmd(cmd):
	return sp.Popen(cmd, shell=True, stdout=sp.PIPE).communicate()[0]

def markdown(fname):
	return run_cmd(MARKDOWN + " " + fname)

posts = []

for post in glob.glob("posts/*.md"):
	mtime = os.path.getmtime(post)
	posts.append((mtime, markdown(post)))

posts.sort(reverse=True)

disqus_template = open("templates/disqus.template").read()

index_template = open("templates/index.html.template").read()	

disqus_text = disqus_template % DISQUS_SHORTNAME

static_files = [os.path.join(x[0], y) for x in os.walk("static") for y in x[2]]

# Copy static files.
if os.path.exists("public"):
	shutil.rmtree("public")

for fname in static_files:
	run_cmd("mkdir -p " + os.path.join("public", os.path.dirname(fname[len("static/"):])))
	shutil.copy(fname, os.path.join("public", fname[len("static/"):]))

# Create posts.
posts_text = ""
for mtime, post in posts:
	lines = post.split("\n")
	post_title = lines[0][4:-5]
	link_title = ''.join([x for x in post_title.lower() if x in (string.ascii_lowercase + " ")]).strip().replace(" ", "_")
	while "__" in link_title:
		link_title = link_title.replace("__", "_")
	link = "%s_%s" % (str(date.fromtimestamp(mtime)).replace("-", "_"), link_title)
	post_h1 = "<h1><a href=\"%s\">%s</a></h1>" % (link, post_title)
	posts_text += """<div id="post">%s%s</div>""" % (post_h1, "\n".join(lines[1:]))
	run_cmd("mkdir -p " + os.path.join("public", os.path.dirname(link)))
	with open(os.path.join("public", link), "w") as post_out:
		post_text = """<div id="postzoom">%s%s</div>""" % (post_h1, "\n".join(lines[1:]))
		post_out.write(index_template.format(posts=post_text, disqus=""))

# Create index.
with open("public/index.html", "w") as index:
	index.write(index_template.format(posts=posts_text, disqus=disqus_text))

# Create posts.