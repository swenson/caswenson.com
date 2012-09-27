Task
====
I recently discovered <a href="http://taskwarrior.org/projects/show/taskwarrior/">task</a>, a powerful, yet simple, command-line to-do and task management tool.  Up until now, I hadn't found any way to manage to-do lists that felt "right".  But task has changed that for me.

One feature I feel is missing (though I think they are planning on <a href="http://taskwarrior.org/wiki/taskwarrior/Features">fixing this</a>) is the lack of email notifications.  I would really like to know what I have to do today, and I may not always remember to login and check, especially in my current transition period of getting used to using it everyday.

So, I set up <a href="http://en.wikipedia.org/wiki/Cron">cron</a> on my system to email my current list (that is due today) every day.  For those of you following along at home, you can do the same with something like so added to your crontab (<code>crontab -e</code>):

<pre>SHELL=/bin/bash
1 0 * * * task list due:today | mail -s "Due `date '+\%A, \%m/\%d/\%Y'`" your@emailaddress.com</pre>

(Note that you have to escape the percent signs in a crontab line.)

Just a quick update &mdash; trying to get back into the habit of posting.