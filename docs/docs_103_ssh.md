# SSH

To SSH into a server its ``ssh username@ipaddress`` or ``ssh username@servername``.

SSH uses port 22.

Typically when you SSH into a system, it will ask for your password. Instead of
using a password everytime, you can create a ssh key. These keys are essentially 
a file that sits on both machines and grants access without needing a password.

To generate ssh keys:

1. On local machine ``ssh-keygen -t rsa -b 4096``. It will ask for a passphrase, but you can leave it empty.
2. Copy the ssh key to the server ``ssh-copy-id user@server``

If it worked correctly, you should now be able to login without needing a password.

