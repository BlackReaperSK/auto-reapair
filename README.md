# 🔧 Auto-Reapair == Auto ROM Install📱
![Android Bootloader](https://www.centralandroid.com.br/wp-content/uploads/2018/09/android-bootloader-1280x720.jpg)


So you bricked your cell phone and you can't start it at all? Infinite loop on home screen? Corrupted partitions? Recovery failed? Yeah,I have the solution for you my dear, Auto-Reapair is an easy-to-use auto-repair tool that automatically downloads and installs the ROM for your device, making it factory default again (and sometimes even more up to date), Auto-Reapair will end your device's problems in just a few minutes (Requires unlocked bootloader for ROM installation)

# 📙 About The Project

So, we can say that I "hard bricked" my cell phone trying to do stupid things, like modifying the ROM, etc etc, the problem is that I have an extremely restrictive cell phone in ROM acceptance issues, most of the ROMs I installed wrong or it was a downgrade from the version I really needed to install. 

So after a lot of time spent trying to "revive" my cell phone, I got it, I thought to myself "Why did I have to do so much research and do so many things if I can do it with a simple script?", that's when I came up with the idea of the Auto-Reapair, and I ended up doing

# 🔗 Usage

Note: If you choosed the compiled C script, it's just move the script to the folder that was extracted the ROM, open a terminal/cmd (not tested in windows)on local and ./auto-reapair (in location where is the script) on cmd/terminal;
- The script has been tested on linux (Ubuntu) and a windows port will soon be made
- First, it will check if you already have ADB-Tools and Fastboot, if you don't have, don't worry, it will download it for you
- Second, it will ask you if you want to download the ROM to your device (highly recommended, as it comes from a fully updated mirror)
- Enter the Product/Variant found on your device's Fastboot screen, or in the box itself, so the script can find the appropriate ROM
- While the image is downloading, put your phone in Fastboot mode (by pressing and holding the power button and the volume down) and plug it into your computer via usb, if you haven't already done it.
- Wait and watch the magic happen!
- If your device was restarted and the ROM successfully installed, congratulations, you managed to get out of the hard brick!

![Android Bootloader](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqCxFLoxwUZkSZWlAC0TpW4HIGD8QnVw5pZ999acZey5JUJuFJoW93d0eolC1FIzvRoBs&usqp=CAU)

 
