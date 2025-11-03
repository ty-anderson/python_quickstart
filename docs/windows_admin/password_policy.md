# Password Policy

An administrator can change all kinds of policies. If you want to 
make it so other users cannot change their local user password, use
the following command:

```
# turn off
net user "user name" /PasswordChg:No

# turn on
net user "username" /PasswordChg:Yes

```