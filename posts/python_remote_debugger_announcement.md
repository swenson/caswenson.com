Python Remote Debugger Announcement
===================================
<div style="margin: 5px; float:right;"><img src="http://m.caswenson.com/images/python_debugger_web_page_v0.2.png" /></div>
Recently, I desired to have a simple Python function I could call with as little fuss as possible that would start up some kind of server that I could use to tell what is going on inside my program at a later date, without resorting to some kind of logging system or console output.

Behold, a simple <a href="http://github.com/swenson/python_remote_debugger">Python Remote Debugger</a>.

Well, it's not really a debugger (yet).  It's more of a "Current State of the System".

There are two servers shipped with it: a plain, pickle-based server (meant to be used to develop richer applications, though it may be abandoned in the future), and a simple web server, based on <a href="http://www.cherrypy.org">CherryPy</a>.

It's still in beta, but has many neat features, including:
<ul>
  <li>Listing of all currently running threads.  Each entry includes a snapshot of the values of all of their local and global variables, as well as the current stack trace.</li>
  <li>Listing of all loaded modules</li>
  <li><code>sys.path</code> listing</li>
  <li>SSL support</li>
  <li>Simple username / password authentication</li>
</ul>

I would be more than happy to take feature requests.  Though, the source is available, fairly simple (and hopefully easy to use), and licensed under the MIT license, so you are free to use or modify it as you see fit.

If I have time in the future, I would love to develop some kind of fancy Ajax-based actual remote debugger, with IPython-like functionality, but it probably won't happen for a while.