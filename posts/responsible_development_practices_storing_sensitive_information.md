Responsible Development Practices: Storing Sensitive Information
================================================================
I build and maintain web sites.  I manage probably hundreds of online accounts or logins or passwords that I need access to semi-regularly.  Organizing all of this information can be a bit of a pain.

I've heard people swear by spreadsheets or plain text files for storing this information, and there are some specialized programs out there meant to catalog and organize this for you.

My solution is one of the simpler: <a href="http://www.tiddlywiki.com/">TiddlyWiki</a>.  It's a small (few hundred K), self-contained (one HTML file), free file you can carry with you to store lots of information.  I simply create some big list tiddlers (what they call their wiki pages), each one of which links to a specific tiddler for one particular task.  So, I have a list for all of the web sites I maintain, and the tiddler for each has MySQL information, passwords, and any other crucial information.

This is great, but there are two problems.  One, I am putting all of critical info in one place.  To fix this, I maintain copies of this wiki file in several places, such as my thumb drive, laptop, and DropBox.

The second catch is then, what if someone finds this file?  Wouldn't they have access to everything?  This is why encryption is important.  Whenever the file needs to be transported somewhere (like, on my thumb drive or put into DropBox), I first encrypt it.  <a href="http://www.gnupg.org/">GPG is nice for this</a>, but in a pinch, you can just use the ever-present OpenSSL to encrypt a file with something <a href="http://www.madboa.com/geek/openssl/#encrypt-simple">like</a>:

<pre>openssl enc -aes-256-cbc -salt -in file.html -out file.html.encrypted</pre>

Now, as long as I remember <strong>this</strong> password, I can safely pass this encrypted file around without any worries about losing my thumb drive in the airport.

For most of the actual machines I log into via SSH, I simply use <a href="http://sial.org/howto/openssh/publickey-auth/">public key authentication</a>, that way I don't have to remember the passwords.