# Pyway or the highway

[Pyway](https://github.com/swenson/pyway) is a database migration tool that I wrote to solve the problem of: I want database migrations, but I don't want to bring [Rails](http://guides.rubyonrails.org/migrations.html) or the entire [JVM](http://flywaydb.org/) with me just to do them.

So, I wrote a little script that does the most simple thing you can do with database migrations: keep track of them by file name, and run any new ones in sorted order.
Python is pretty much universally present at this point in server environments, so that's the tool that I used.

This is nothing sophisticated, and currently has `sqlite3` hardcoded in it, but it should be trivial to modify for any other databases.
I didn't even use Python bindings for `sqlite3`: I just called the command-line program to do the migrations.
That way, it should be easy to modify it for other databases in the near future.

I'll probably end up adding Postgres or MySQL support sometime soon (when one of my projects that uses those technologies needs to be updated).