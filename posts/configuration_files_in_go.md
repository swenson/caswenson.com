Configuration files in Go
=========================

The other day, I was starting to port an existing service I had into Go.
There were a lot of issues that I had to tackle to get the functionality I wanted,
including being able to run in at least four different environments:
test, dev, stage, and prod.

There are a lot of "standard" ways to do this, most focusing on some sort
of text or structured file that you load at runtime using file I/O.

However, in dynamic languages, a somewhat common practice is to use a file
in that programming language as your configuration. So, in Python, you might
have a `settings.py` file that is actual executed Python.

In non-scripting languages, like Java, you normally have an XML, YAML, INI,
or JSON file that you read in.
But, I've seen at least one non-scripting language, Clojure, that encourages using
an executable Clojure file for configuration.

The primary argument against using a file in your programming language itself
is that the compile time may be long, and deploying a brand new binary just to
change the config file is laborious and slow.

But, I thought, Go doesn't have this limitation:
Go compiles super fast, and the binaries tend to be reasonably sized,
so deploys won't be that big of a deal.

So, can we just use Go code to be our configuration file?

Definitely.
I wrote up a quick template (released under CC0, so feel free to copy and use)
for a configuration file in Go.
There's a small amount of boilerplate, but it is super easy to compromise.

<a href="https://github.com/swenson/goconf">https://github.com/swenson/goconf</a>

There are four key parts:

* `var config = getConfig()` &ndash; this triggers the configuration file to be
  read at initialization time. You can also use an `init()` function to do this.
* `type Config struct { ... }` &ndash; specify all the variables you want in your
  config file
* `func readConfig() Config { ... }` &ndash; populate a `Config` struct based
  on your environment, which I do via a `switch` statement.
* Set your environment (`ENV` environment variable) when running

That's it.
This is a pretty straightforward and easy way to do config files in Go.