import os
import string
import time
import old_posts

def title_slug(title):
  slug = ''.join([x for x in title.lower() if x in (string.ascii_lowercase + "0123456789" + " ")]).strip().replace(" ", "_")
  while "__" in slug:
    slug = slug.replace("__", "_")
  return slug

fnames = set()
disqus_csv = open('disqus.csv', 'w')
for (id_, title, body, slug, tags, created_at) in old_posts.posts:
  old_url = "?p=%d" % id_
  new_url = created_at.split()[0].replace("-", "_") + "_" + title_slug(title)
  disqus_csv.write("http://www.caswenson.com/%s,http://www.caswenson.com/%s\n" % (old_url, new_url))
  old_url = "past/" + created_at.split()[0].replace("-", "/") + "/" + slug
  disqus_csv.write("http://www.caswenson.com/%s,http://www.caswenson.com/%s\n" % (old_url, new_url))
  fname = "posts/%s.md" % slug
  if fname in fnames:
    exit("ERROR: duplicate name" + fname)
  fnames.add(fname)
  with open(fname, "w") as postout:
    postout.write(title + "\n")
    postout.write("=" * len(title) + "\n")
    postout.write(body)
  timestamp = time.mktime(time.strptime(created_at, "%Y-%m-%d %H:%M:%S"))
  os.utime(fname, (timestamp, timestamp))
  print id_, slug, slug == title_slug(title)

disqus_csv.close()
