# **Raspberry Pi Live Temperature Monitor - AdafruitIO**

### **Setup**

First off, you'll need to ensure python and pip are working. This code only works on Python3. You can do this with:
```
sudo apt install python3 python3-pip
```
Next, ensure pip3 is up-to-date with:

```
sudo pip3 install --upgrade setuptools
```
Now, onto the python libraries:
```
pip3 install RPI.GPIO && pip3 install adafruit_blinka
```
Obviously, if you run into any permission errors, run with sudo.

Almost done, now it's time to install the [Adafruit IO Python Library](https://github.com/adafruit/Adafruit_IO_Python).
```
pip3 install adafruit-io
```
Finally, you need to setup the code with your unique details. First, copy your username from AIO and paste to into the `YOUR_USERNAME` line. Do the same thing with your AIO Key and paste it into the `YOUR_KEY' line. 

Now you can make you AIO feed. In this example I called the feed `pitemp`, you can call it whatever you like, just ensure you replace `pitemp` with your chosen name.

### Usage

It's simple really, just type `python3 pitemp.py` and away you go! There is one problem though. It won't start on boot. I fixed this by adding it as a system daemon, although that approach is more complicated than it has to be. Simply putting `/usr/bin/python3 /home/pi/pitemp.py` (or wherever it is) above `exit 0` in /etc/rc.local should do the trick. Or add a cron job with `crontab -e`. If you run into issues, just open a issue and I will be happy to work with you on finding a solution!

- [ ] Make issue for timeout. Edit: Done: #1
- [ ] Build relase package
- [ ] Add prompt to enter key and username during setup
- [ ] Improve debugging
