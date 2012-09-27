curl + twitter + crontab = Happiness
====================================
I've always wanted to know how my servers are doing.  I don't have time to check on every single one of them all of the time.  In the past, this meant perhaps an automatic email sent to me at some specified time during the day.

But emails are annoying.  RSS is definitely the technology that would be nice, but how to implement it?

<a href="http://www.twitter.com/">Twitter</a> is ideal for this purpose.  Multiple people (admins?) can check the status of a server as it is updated, and you can lock it down so that only authorized people can view the status.

Updating is easy using the Twitter API through <a href="http://www.sakana.fr/blog/2007/03/18/scripting-twitter-with-curl/">curl</a>.  I just wrote the following bash script to update a twitter feed for a specified user:

<pre lang="bash">#!/bin/bash

USER="server"
PASS="password"
URL="http://twitter.com/statuses/update.xml"
STATUS="[`hostname`] `uptime`, `df -h / | grep -o -e '[0-9][0-9]*%'` HD used"

curl --basic --user $USER:$PASS --data status="$STATUS" $URL</pre>

This automatically sends updates that look like:
<pre>[servname] 11:23:20 up 7 days, 14:43, 1 user, load average: 0.18, 0.36, 0.17, 83% HD used</pre>

Then I name it something useful, like <code>/root/twitter.sh</code>, and add a <a href="http://en.wikipedia.org/wiki/Cron">crontab</a> entry:

<pre>0 0 * * * /root/twitter.sh >& /dev/null</pre>

And I'm set.

Naturally, this was designed to work for Linux, and would probably work on OS X and Windows/<a href="http://en.wikipedia.org/wiki/Cygwin">Cygwin</a> as well.