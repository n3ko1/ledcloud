export ANDROIDNDK="/home/lcsbader/dev/android/android-ndk-r7";
export ANDROIDSDK="/home/lcsbader/dev/android/android-sdk-linux/";
export PATH=$PATH:/home/lcsbader/dev/android/android-sdk-linux/tools/;
export PATH=$PATH:/home/lcsbader/dev/android/android-sdk-linux/platform-tools/;
~/dev/kivy/android/python-for-android/dist/default/build.py --dir ~/dev/electro/arduino/kivy --package org.arduino.ledcloud --name "LED Cloud Remote Control" --version 0.1 debug installd;