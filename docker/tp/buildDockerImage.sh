#!/bin/bash

# Build docker image tp:1

if [ -z $1 ]
then
  echo 'You must indicate a docker image name in 1st parameter'
else
  sudo docker build -t $1 .
fi