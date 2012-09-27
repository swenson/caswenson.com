Responsible administration for you and your users
=================================================
When I was constructing my own websites, for myself or for clients, I was always bothered by one thing:

I didn't have an SSL certificate for any of my domains.

This is due to many reasons: SSL certificates are tied to a single domain, they cost a lot of money, and they are tied to an IP address, which can make shared hosting hard.  Furthermore, I don't feel that shelling out money for some SSL authority to issue me a certificate really <strong>means</strong> anything &ndash; why are they qualified to say anything (good or bad) about my website.

Unfortunately, there are only two alternatives: don't use SSL, or use a self-signed SSL certificate.

Not using SSL is not really an option if you are sending sensitive information of any kind over the Internet.  For example, the password to login to the backend of any site.

If you have a user-facing website that is selling things, i.e., asking people for their credit card information, you don't have much of a choice.  You really need to use SSL, and you have to use a real registered SSL certificate, since you don't want to scare away users.

However, for almost any other case, I think that they are just not necessary.  Take this website, for example: the only person who logs into this domain is me.  I certainly trust any certificate I sign, so a self-signed certificate makes a lot of sense.  I can go ahead and "Accept the risk", as Firefox asks me to, and confirm an exception for my own site.  I will then sleep easy knowing that my password is sent encrypted.

Even if I make a site for a client, I would be happy to give them the option: we can use this self-signed certificate for you to login to the backend, or they can front the cost for a "real" SSL certificate.  However, nobody likes to waste money, and buying a certificate for only a few people to use a backend is a silly idea.

Creating a self-signed certificate with OpenSSL is <a href="http://www.akadia.com/services/ssh_test_certificate.html">easy</a>, and installing it in Apache is also <a href="http://www.digicert.com/ssl-certificate-installation-apache.htm">easy</a>.

Don't let you or your clients down by neglecting to give them the option for free SSL.

Extra credit question: why aren't there are any free SSL signing authorities out there?