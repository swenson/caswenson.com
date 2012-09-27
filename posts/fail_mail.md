Fail Mail
=========
I do some freelance web development, and one of the things I've found most annoying is when a a 500 error occurs on my Rails sites, I hear about I from the customer.  What's even worse is that I often have no idea what the erorr that occurred is, and the customer may not know exactly how the application failed.  Pouring through the server logs can be a bit tedious, especially if there has been a lot of traffic.

Enter Fail Mail, a.k.a., the <a href="http://wiki.rubyonrails.org/rails/pages/ExceptionNotification">Exception Notification</a> plugin for Rails.  Assuming you have ActionMailer installed and configured, there are about three steps needed to ensure that you automatically receive an email message every time your application crashes.  (It doesn't notify you if it was a 404, which is probably for the best.)

Looks like I need to go reinvent the wheel for to make it work on this blog, now &hellip;
