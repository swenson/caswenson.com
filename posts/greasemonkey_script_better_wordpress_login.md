Greasemonkey Script: Better WordPress Login
===========================================
A problem I've always had: WordPress blogs transmit passwords in the clear by default.  The only way to remedy this was to break down and buy an SSL certificate for each of your WordPress blogs.

Until now.

I wrote a simple <a href="https://addons.mozilla.org/en-US/firefox/addon/748">Greasemonkey</a> script for Firefox that secures your password as it is transmitted to any WordPress site.  <a href="http://www.caswenson.com/wp-content/uploads/gm/betterloginwp.user.js">Click here to install it</a> (assuming you are running Firefox and have Greasemonkey installed).  It seems to work with WordPress version 2.4 or better (possibly earlier &hellip; I just haven't tested it with them).

Naturally, I had to modify the WordPress change password screen.  Assuming you are logged in, just go ahead and go to change your password to a new secure one.  Notice the "SECURED" text that indicates that the script is working its magic.

<a href="http://www.caswenson.com/wp-content/uploads/2008/07/wp-change-password.png"><img src="http://www.caswenson.com/wp-content/uploads/2008/07/wp-change-password-300x111.png" alt="" title="Modified WordPress Change Password" width="300" height="111" class="alignnone size-medium wp-image-64" /></a>

Now, if you log out, you would normally see this login screen:

<a href="http://www.caswenson.com/wp-content/uploads/2008/07/wp-login-insecure.png"><img src="http://www.caswenson.com/wp-content/uploads/2008/07/wp-login-insecure-300x222.png" alt="Insecure WordPress Login" title="WordPress Login (Normal, Insecure)" width="300" height="222" class="size-medium wp-image-59" /></a>

However, with the new script installed, it should look like this (note the word "Secure" has been added to the login button).

<a href="http://www.caswenson.com/wp-content/uploads/2008/07/wp-login.png"><img src="http://www.caswenson.com/wp-content/uploads/2008/07/wp-login-300x220.png" alt="" title="WordPress Login (More Secure)" width="300" height="220" class="alignnone size-medium wp-image-62" /></a>

After you type in your password and click on the "Secure Login Button", the script automatically rewrites your password by hashing it (with a salt), which will produce an identical output for an identical input on the same site.  You can see it in action here:

<a href="http://www.caswenson.com/wp-content/uploads/2008/07/wp-login-replace.png"><img src="http://www.caswenson.com/wp-content/uploads/2008/07/wp-login-replace-300x221.png" alt="" title="WordPress Login (More secure, with replaces password)" width="300" height="221" class="alignnone size-medium wp-image-63" /></a>

Technical notes:
<ul>
	<li>it replaces your password with a SHA-1 hash of the SHA-1 hash of your password appended with a salt.  Nothing too fancy.</li>
	<li>The salt is the DNS name of the web server you are connected to.  This way, your password for different sites will have different hashes.

If you didn't do this, and just used a plain hash for your password, then this would not really give you too much security.  For example, if you really think that your password "secret" is made more secure by using the MD5 hash of it instead, just do a Google search on the hash (<a href="http://www.google.com/search?q=dd02c7c2232759874e1c205587017bed">dd02c7c2232759874e1c205587017bed</a>) to see how secure your password <b>really</b> is.</li>
	<li>This is important: <b>you will have to have the script installed on every computer you expect to login with</b>.  The password is permanently changed to be a hash, and if you could still login with the old password, that would be silly.</li>
	<li>You have to login normally first (Greasemonkey script off) with your old password, and then change the password with the Greasemonkey script turned on.  Then, just leave it on.</li>
	<li>The script is licensed under the BSD license, so it is easy to adapt to your own purposes.  Feel free to do so.</li>
	<li>I will also make this into a WordPress plugin if there is a desire for that.  (I actually prefer having it as a Greasemonkey script so that I know that it is working and hasn't been changed, but I know some people don't want to use Greasemonkey to do this.)</li>
	<li>A Twitter version is also in testing and cleanup (Twitter does secure your password when you login, but not when you change your password).</li>
</ul>




If you like what you see, then <a href="http://www.caswenson.com/wp-content/uploads/gm/betterloginwp.user.js">click here to install the script</a>.

