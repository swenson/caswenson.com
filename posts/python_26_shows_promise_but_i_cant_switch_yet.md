Python 2.6? Shows promise, but I can't switch yet
=================================================
Python 2.6 was recently released, with 3.0 coming out soon.  Python 2.6 is meant to be sort of a stepping stone between the trusty old 2.x series and the hot, scary 3.0 series.  So, naturally, I downloaded 2.6 to play with.

One of the nicest features has to be true <a href="http://docs.python.org/library/multiprocessing.html#module-multiprocessing">multiprocessing support</a>, allowing you to have multiple processes going, all started from within the same program.  The Python docs even give a <a href="http://docs.python.org/whatsnew/2.6.html#pep-371-the-multiprocessing-package">short example</a> "demonstrating this", but it's probably the worst example ever.  For one thing, it crashes semi-regularly (Queue implementation problem?), and the <code>time.sleep()</code> in the inner loop makes no sense.

So, I had to write my own simple benchmarking program to see if there was much of a difference (adapted from their sample program):<pre name="code" class="python">from multiprocessing import Process
 
def factorial(N):
  fact = 1
  for i in range(1, N+1):
    fact = fact * i
  return fact
 
if __name__ == '__main__':
  import sys
  if len(sys.argv) > 1 and (sys.argv[1] == "1" or sys.argv[1] == "2"):
      N = int(sys.argv[1])
  else:
    print "Expected argument: N (1 for single-threaded, 2 for double-threaded)"
    sys.exit(1)
 
  numbers = range(15000, 15002)
  
  if N == 1:
    factorial(numbers[0])
    factorial(numbers[1])
  else:
    processes = [Process(target=factorial, args=(i,)) for i in numbers]
    for p in processes:
      p.start()
    for p in processes:
      p.join()</pre>
I tested it on my Core Duo (2 × 32-bit cores) on my MacBook Pro, with a single process and two processes, with run times of approximately 0.98 and 0.58 seconds, respectively, for a speedup of about <strong>1.7×</strong>!  Not too shabby at all.  (Single process performance was nearly identical to that under Python 2.5, sadly.)

Normally, I'd be installing this on all of my systems, but, alas: <code>scipy</code> does not currently run under 2.6 (it breaks when compiling it).  So, for now, I cannot afford to switch to 2.6.

Fat chance that any of my standard packages will work with Python 3.0, too.