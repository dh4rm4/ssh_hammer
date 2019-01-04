# SSH_HAMMER

SSH_Hammer is a script that will bruteforce an ssh gate via a password dictionnary file and execute few commands if needed.


### Prerequisites
python >= 3.


## Usage
```
python3 main.py --host <HOST> --user <USERNAME> -f <passwdDictionnary> --cmds <fileWithCmds>
* the file with cmd is optionnal, still, a default command will be execute
```

Practical exemple on a raspberry pi:
```
python3 main.py --host 192.168.XXX.XXX --user pi -f passwdDictionnary --cmds fileWithCmds
```


#### IF you use a desktop environment, be sure you don't have the ssh-askpass-gnome package install or any equivalent. Keeping it will open an authentification pop-up for each auth session.



### Dictionary source
You can find on [cracking-station](https://crackstation.net/buy-crackstation-wordlist-password-cracking-dictionary.htm) one of the largest password dictionary.






```
If the only tool you have is a hammer, you tend to see every problem as a nail.
--Abraham H. Maslow, Toward a Psychology of Being
```
