#!/bin/bash

read -p $'Warning !!! Are you sure about that ? y/n:\n' userConfirmation 

if [ $userConfirmation = 'y' ]
then
  sudo docker container prune
  sudo docker rmi -f $(sudo docker images -qa)
fi