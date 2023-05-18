#!/bin/bash

err=$(pip3 install pytube | echo "$?")

if [ $err = 0 ]; then 
clear
pip3 install pytube --break-system-packages 

fi