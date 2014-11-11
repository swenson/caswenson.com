#!/usr/bin/env python2.7

from datetime import date
import xml.etree.ElementTree as et
import glob
import os
import os.path
import shutil
import string
import subprocess as sp
import time
import uuid

uuid_namespace = uuid.UUID('fcd0d678-5e95-4d62-9551-ac14caa3ce22')

INDEX_POSTS = 10
RSS_POSTS = 10
DISQUS_SHORTNAME = "swenson"

MARKDOWN = glob.glob("vendor/markdown*/Markdown.pl")[0]

def title_slug(title):
  slug = ''.join([x for x in title.lower() if x in (string.ascii_lowercase + "0123456789" + " ")]).strip().replace(" ", "_")
  while "__" in slug:
    slug = slug.replace("__", "_")
  return slug

def run_cmd(cmd):
  return sp.Popen(cmd, shell=True, stdout=sp.PIPE).communicate()[0]

def markdown(fname):
  return run_cmd(MARKDOWN + " " + fname)

posts = []

for post in glob.glob("posts/*.md"):
  print "Reading " + post
  mtime = os.path.getmtime(post)
  posts.append((mtime, markdown(post)))

posts.sort(reverse=True)

disqus_template = open("templates/disqus.template").read()

index_template = open("templates/index.html.template").read()

rss_template = open("templates/feed.template").read()

disqus_text = '' # disqus_template % DISQUS_SHORTNAME

static_files = [os.path.join(x[0], y) for x in os.walk("static") for y in x[2]]

print "Cleaning"
# Copy static files.
if os.path.exists("public"):
  shutil.rmtree("public")

print "Static files"
for fname in static_files:
  run_cmd("mkdir -p " + os.path.join("public", os.path.dirname(fname[len("static/"):])))
  shutil.copy(fname, os.path.join("public", fname[len("static/"):]))

months = 'xxx jan feb mar apr may jun jul aug sep oct nov dec'.split()

# Create posts.
print "Posting"
posts_text = ""
archive_text = """<ul id="archive">"""
atom_text = ""
rss_text = ""
processed = 0
for mtime, post in posts:
  lines = post.split("\n")
  post_title = lines[0][4:-5]
  slug = title_slug(post_title)
  pdate = str(date.fromtimestamp(mtime))
  link = "%s_%s" % (pdate.replace("-", "_"), slug)
  post_h1 = "<h1><a href=\"%s\">%s</a></h1>" % (link, post_title)
  post_body = "\n".join(lines[1:])
  if processed < INDEX_POSTS:
    posts_text += """<div class="post">"""
    posts_text += """<div class="date">%s</div>""" % pdate
    posts_text += """%s%s</div>""" % (post_h1, post_body)
  if processed < RSS_POSTS:
    # Atom
    entry = et.Element("entry")
    title = et.SubElement(entry, "title")
    title.text = post_title
    linker = et.SubElement(entry, "link")
    linker.set('href', 'http://www.caswenson.com/' + link)
    linker.set('rel', 'alternate')
    ident = et.SubElement(entry, 'id')
    ident.text = link
    published = et.SubElement(entry, "published")
    published.text = time.strftime("%Y-%m-%dT%H:%M:%S-00:00", time.gmtime(mtime))
    updated = et.SubElement(entry, "updated")
    updated.text = time.strftime("%Y-%m-%dT%H:%M:%S-00:00", time.gmtime(mtime))
    author = et.SubElement(entry, "author")
    name = et.SubElement(author, "name")
    name.text = "Christopher Swenson"
    summary = et.SubElement(entry, "summary")
    summary.set("type", "html")
    summary.text = post_body[:100]
    content = et.SubElement(entry, "content")
    content.set("type", "html")
    content.text = post_body
    atom_text += et.tostring(entry, "utf-8")

    # RSS
    item = et.Element("item")
    title = et.SubElement(item, "title")
    title.text = post_title
    linker = et.SubElement(item, "link")
    linker.text = 'http://www.caswenson.com/' + link
    guid = et.SubElement(item, "guid")
    guid.text = str(uuid.uuid5(uuid_namespace, post_body))
    published = et.SubElement(item, "pubDate")
    published.text = time.strftime("%a, %d %b %Y %H:%M:%S %z", time.gmtime(mtime))
    content = et.SubElement(item, "description")
    content.text = post_body
    rss_text += et.tostring(item, "utf-8")

  processed += 1

  archive_text += """<li><a href="%s">%s</a></li>""" % (link, post_title)
  run_cmd("mkdir -p " + os.path.join("public", os.path.dirname(link)))
  with open(os.path.join("public", link), "w") as post_out:
    url = "http://www.caswenson.com/" + link
    #disqus = """<div id="disqus_thread"></div><script type="text/javascript" src="http://disqus.com/forums/%s/embed.js"></script><noscript><a href="http://%s.disqus.com/?url=%s">View the discussion thread.</a></noscript><a href="http://disqus.com" class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a>"""
    #disqus = disqus % (DISQUS_SHORTNAME, DISQUS_SHORTNAME, url)
    disqus = ''
    post_text = """<div class="postzoom">%s%s</div>""" % (post_h1, post_body)
    post_out.write(index_template.format(title=post_title, posts=post_text, disqus=disqus))
archive_text += "</ul>"

print "Index"

# Create index.
with open("public/index.html", "w") as index:
  index.write(index_template.format(title="Main", posts=posts_text, disqus=disqus_text))

print "Archive"
# Create archive at /archive
with open("public/archive", "w") as archive:
  archive.write(index_template.format(title="Archive", posts=archive_text, disqus=""))

print "Atom"
# Create Atom
with open("public/feed", "w") as rss:
  mtime = posts[0][0]
  modified_time = time.strftime("%Y-%m-%dT%H:%M:%S-00:00", time.gmtime(mtime))
  rss.write(rss_template % (modified_time, atom_text))

print "RSS 2.0"
# Create RSS
with open("public/rss", "w") as rss:
  mtime = posts[0][0]
  modified_time = time.strftime("%a, %d %b %Y %H:%M:%S %z", time.gmtime(mtime))
  rss.write(rss_template % (modified_time, rss_text))

print "Pages"
# Create Pages
for page in glob.glob("pages/*"):
  name = os.path.basename(page)
  with open("public/" + name, "w") as page_out:
    page_out.write(index_template.format(title=name.replace("_", " ").capitalize(), posts=open(page).read(), disqus=""))



