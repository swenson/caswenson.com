Please, please use UTF-8
========================
I am currently migrating a site from an older WordPress setup to a fresh new server.  I obtained MySQL backups and all of the files from the site.

My problem is that the primary way of posting was by writing a document in Microsoft Word, copy-pasting it to Firefox or IE into a version of WordPress set up for UTF-8, running on a PHP installation using ISO-8859-1, and ending up in a MySQL database setup as Latin1.  It is then exported out into the dump, and now I have to figure out how to clean up the dump or MySQL instance so that I get "don't" and not "donâ€™t".

So please, I beg of you, read <a href="http://www.joelonsoftware.com/articles/Unicode.html">this article</a> and always use UTF-8 in everything you do.

Edit: Also, if you run into such problems, two of the best helps I have found were <a href="http://myhep.com/2007/1/25/mysql-on-the-move-from-latin1-to-utf8">here</a> (though you may want to modify it a bit, since it changes smart quotes to dumb quotes) and <a href="http://www.oreillynet.com/onlamp/blog/2006/01/turning_mysql_data_in_latin1_t.html">here</a>.