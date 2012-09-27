Mac OS X Python
===============
<a href='http://www.caswenson.com/wp-content/uploads/2008/02/python.png' title='Python Logo'><img class="alignright" src='http://www.caswenson.com/wp-content/uploads/2008/02/python.png' alt='Python Logo' /></a>

Python on Mac OS X is poorly designed and all sorts of unfun to fix.  Certain packages work better with the built-in Python, certain work better with fink/ports/portage Python.  However, wxPython only works with the built-in one, since it integrates with Aqua, so I decided to switch everything over to using only the built-in version.

Here is what you need to do to get up to speed:
<ol>
	<li><a href="http://www.python.org/download/">Update</a> to the latest Python for OS X.</li>
	<li>If you are running on an Intel processor on OS X 10.5 Leopard, <a href="http://www.oreillynet.com/onlamp/blog/2007/12/pil_on_leopard_or_how_i_made_p.html">fix</a> (really, unbreak) your Python core Makefile to drop PPC support, since it breaks things like PIL.  (The link just stays to remove all <code>-arch ppc</code>'s from <code>/Library/&zwnj;Frameworks/&zwnj;Python.framework/&zwnj;Versions/&zwnj;Current/&zwnj;lib/&zwnj;python2.5/&zwnj;config/&zwnj;Makefile</code></li>
	<li>Install everything either with Framework packages (wxPython), or by manually building via <code>sudo python setup.py install</code>.</li></ol>

For my work, the core packages are <a href="http://www.wxpython.org/download.php">wxPython</a>, <a href="http://www.scipy.org/Download">numpy + scipy</a>, <a href="http://sourceforge.net/projects/matplotlib">matplotlib</a>, and the <a href="http://www.pythonware.com/products/pil/">Python Imaging Library</a>.  I've successfully installed them all now using the above method, but note that numpy and scipy will not install via the OS X package, but have to be compiled from source.