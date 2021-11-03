#!/usr/bin/bash
# 判断是否是root 用户

if [ $UID -eq 0 ]; then 
   echo "$(ls -l)"
   exit
elif [ $UID -ne 0 ]; then 
   echo "Please testing by root user!"
fi

