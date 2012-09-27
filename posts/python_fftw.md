Python (F)FTW!
==============
Some of the work I have been doing involves taking the <a href="http://en.wikipedia.org/wiki/Fast_Fourier_Transform">Fast Fourier Transform</a> of a set of samples.  I originally thought that this needed to be done in C, using <a href="http://www.fftw.org/">FFTW</a>. However, it leads to messes like

<pre lang="c">fftw_complex *in, *out;
in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
fftw_plan p;
p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

/* read in samples */

fftw_execute(p);

/* do stuff */

fftw_destroy_plan(p);
fftw_free(in);
fftw_free(out);
</pre>

In Python with <a href="http://numpy.scipy.org/"><code>numpy</code>/<code>scipy</code></a> installed, this is so much easier.
<pre lang="c">from numpy import *

# read in samples

fftout = fft(samples)
</pre>

And that's it! I should have been using nothing but Python for nearly everything from the start, and screw C.