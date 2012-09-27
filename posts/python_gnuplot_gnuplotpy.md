Python + gnuplot = gnuplot-py
=============================
<a href='http://www.caswenson.com/wp-content/uploads/2008/02/gnuplot-py.png' title='Image from gnuplot'><img class="alignright" src='http://www.caswenson.com/wp-content/uploads/2008/02/gnuplot-py.thumbnail.png' alt='Image from gnuplot' /></a>

I recently discovered a fairly old (last updated in 2003), but still functional package for Python that provides nifty integration with <a href="http://www.gnuplot.info">gnuplot</a> called <a href="http://gnuplot-py.sourceforge.net/">gnuplot-py</a>.

For those of you unfamiliar with gnuplot, it is a simple, powerful, and free graphing program.  It's very slick, but sometimes a bit annoying to use if you are, say, generating your data in Python.  Normally, this would require you to produce your output to a file, and then run gnuplot as a separate program, and finally load and plot your file.  It can be tediously annoying at times.

Enter gnuplot-py.  Basically, it provides a few simple wrappers to gnuplot allowing you to control it from Python, and it can easily plot Python data structures.

The basic usage of this is demonstrated in the following ultra-basic Python program:

<pre lang="python"># basic declarations and setup
import Gnuplot, Gnuplot.funcutils
gplot = Gnuplot.Gnuplot(debug = 1)
gplot.title("Test")
gplot("set data style linespoints")

data = [1.0, 0.0, 1.0]  # the data to plot

gplot.plot(data) # plot the data</pre>

In OS X, this probably pulls up an AquaTerm window that displays the data plotted.  Simple, nay?

The hardest part of using it is the fact that the Python "Numeric" package is now called numpy.  To fix this, download <a href="http://mirrors.usc.edu/pub/linux/distributions/gentoo/dev-python/gnuplot-py/files/gnuplot-py-1.7-numpy.patch">this patch file</a> and run it against the sources you download (usually with <code>patch -p1 < gnuplot-py-1.7-numpy.patch</code>, if run from within the source directory itself).