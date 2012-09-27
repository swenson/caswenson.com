Bypassing the Python GIL with ctypes
====================================
I recently read an interesting <a href="http://entitycrisis.blogspot.com/2009/06/python-threading-is-fundamentally.html">article</a> (actually, the slides linked to) about the horror that is the Global Interpreter Lock in Python, especially with multicore CPUs.  And I agree — in these cases, the GIL is painful.

My favorite way of bypassing the GIL is to use <a href="http://docs.python.org/library/ctypes.html#finding-shared-libraries">ctypes</a>, a wonderful library that allows you to easily link to dynamic libraries and call the functions from C, with only a small amount of boilerplate (to map function calls, argument types, and return types).

The best feature of <tt>ctypes</tt> is that when a program is executing a ctypes function, it <strong>releases the GIL</strong>.  Meaning that if you have more than one thread threads, and one of them is busy with a <tt>ctypes</tt> call, the other threads can go along their merry way.

In the slides above, he shows that Python CPU-intensive multithreaded applications slow down as the number of CPUs increase.  Well, I decided to use a quick counterexample.

First, I create a C file to do some work for me, called <tt>test.c</tt>:
<pre name="code" class="c">int test(int from, int to)
{
  int i;
  int s = 0;
 
  for (i = from; i < to; i++)
    if (i % 3 == 0)
      s += i;
 
  return s;
}</pre>
To compile this as a dynamic shared library under OS X, the following two commands can be used:
<pre>gcc -g -fPIC -c -o test.o test.c
ld -dylib -o libtest.dylib test.o</pre>
(Under Linux, replace this last line with <tt>ld -shared -o libtest.so test.o</tt>)

Then, we can use the following Python program to load the dynamic library and run a quick test (should work in Linux or OS X):
<pre name="code" class="python">import ctypes
import ctypes.util
import threading
import time
 
testname = ctypes.util.find_library('test')
testlib = ctypes.cdll.LoadLibrary(testname)
 
test = testlib.test
test.argtypes = [ctypes.c_int, ctypes.c_int]
 
def t():
  test(0, 1000000000)
 
if __name__ == '__main__':
  start_time = time.time()
  t()
  t()
  print "Sequential run time: %.2f seconds" % (time.time() - start_time)
 
  start_time = time.time()
  t1 = threading.Thread(target=t)
  t2 = threading.Thread(target=t)
  t1.start()
  t2.start()
  t1.join()
  t2.join()
  print "Parallel run time: %.2f seconds" % (time.time() - start_time)</pre>
On my quad-core OS X box, I get the following output:
<pre>Sequential run time: 13.27 seconds
Parallel run time: 6.66 seconds</pre>
A pretty solid doubling of performance, which is what we would hope.