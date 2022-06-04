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
* Make files executable
 ``` chmod +x fancontrol.sh ```
* Add to cronjob by:
  * ```sudo crontab -e```  
  at the end of file attach
  * ```@reboot /path/to/your/file/fancontrol.sh```
*  reboot
