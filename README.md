# Password-Checker
Password Checker using Python

> This program uses an API to ['You may be using Have I been Pwned'](https://haveibeenpwned.com/)
> 
> In order to protect the password being searched for,
> Pwned Passwords API implements a k-Anonymity model that allows a password 
> to be searched for by partial hash. This allows the first 5 characters of either 
> An SHA-1 or an NTLM hash (not case-sensitive) to be passed to the API.
> 
> Hence, only the first 5 characters of the hashed passwords will be sent and the first making it safe to use

#### Note: Although k anonymity is safe, it is not advised to input your login information on any website other than the one you intended.

### How to run?
1. Clone this repository
2. Change directory to the location of the cloned repository 
3. run the command in the terminal ```python main.py password1 password2 password3 password4 passwordn ```