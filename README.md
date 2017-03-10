# SSH_HAMMER

SSH_Hammer is a script how will bruteforce an ssh gate via a password dictionnary file

### Prerequisites
You only need a version >= 3 for python.

If you still live in the past, you can delete all the output function to make it work

## Usage
```
python3 ssh_hammer --host <HOST> --user <USERNAME> -f <passwdDictionnary> --cmds <fileWithCmds>
* the file with cmd is optionnal, still, a default command will be execute
```
Practical exemple on a raspberry pi:
```
python3 ssh_hammer --host 192.168.1.XXX --user pi -f passwdDictionnary --cmds fileWithCmds
```

#### Before you run it, be sure you don't have the ssh-askpass-gnome package install. In this case, it will open a authentification pop-up for each try of connection

### Dictionniary source
You can find on [cracking-station](https://crackstation.net/buy-crackstation-wordlist-password-cracking-dictionary.htm) one of the biggest password dictionnary.



```
If the only tool you have is a hammer, you tend to see every problem as a nail.
--Abraham H. Maslow, Toward a Psychology of Being
```
