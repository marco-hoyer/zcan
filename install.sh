#!/bin/bash

source /root/zcan_env/bin/activate
cd /root/zcan
git pull -r
pip uninstall -y zcan
pyb install
killall zcan
cd /tmp
nohup zcan run &
