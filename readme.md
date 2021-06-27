# Fan control raspberry pi #

Automatic fan control for raspberry pi GPIO
with On and Off Threshold values

### Manage GPIO lines with gpiod ###
gpiod is a set of tools for interacting with the linux GPIO character device that uses libgpiod library.

If you are using Debian install gpiod by typing these commands:
```
sudo apt update
sudo apt install gpiod
```
* Copy files to raspberry
* Add to cronjob by:
  * ```crontab -e```  
  at the end of file attach
  * ```@reboot /path/to/your/file/fancontrol.sh```
*  reboot
