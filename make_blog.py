#!/usr/bin/env python2.7

from datetime import date
import glob
import os
import os.path
import shutil
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

posts_text = ""
for mtime, post in posts:
	posts_text += """<div id="post">%s</div>""" % post
disqus_text = disqus_template % DISQUS_SHORTNAME

static_files = [os.path.join(x[0], y) for x in os.walk("static") for y in x[2]]

if os.path.exists("public"):
	shutil.rmtree("public")

for fname in static_files:
	run_cmd("mkdir -p " + os.path.join("public", os.path.dirname(fname[len("static/"):])))
	shutil.copy(fname, os.path.join("public", fname[len("static/"):]))

with open("public/index.html", "w") as index:
	index.write(index_template.format(posts=posts_text, disqus=disqus_text))