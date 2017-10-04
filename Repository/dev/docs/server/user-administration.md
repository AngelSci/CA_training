User administration
===================

Add a user
----------

New users can navigate to the Anaconda repository web page and sign up
there, or an administrator can add them using the command line:

    anaconda-server-create-user --username "jsmith" --password "abc123DEF"  --email "jsmith@acme.com"

NOTE: Replace jsmith, abc123DEF, and <jsmith@acme.com> with the actual
username, password, and email address of the new user.

Resending welcome emails to new users
-------------------------------------

If a user reports not receiving their welcome email after registering
with the graphical user interface, it may have been caught in a spam
filter. You can regenerate and manually send this email.

Resend welcome email:

1.  Log into your Anaconda repository administrative account.
2.  Navigate to the following url:
    <http://your.anaconda.server>:&lt;port&gt;/admin/resend\_email/password\_reset
3.  Click the "Confirmation" tab.
4.  Enter the user's email address and re-generate the email template.
5.  Send the email to the user.

Resetting user passwords
------------------------

If a user forgets their password, you can request a reset link to
provide to the user.

1.  Go to the following url:
    <http://your.anaconda.server>:&lt;port&gt;/admin/resend\_email/password\_reset
2.  Select the "Password Reset" tab.
3.  Enter the user's email address.
4.  The graphical user interface will generate a password reset link.
5.  Email the link to the user.

