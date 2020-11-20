#!/bin/bash

# Run docker image

if [ -z $1 ]
then
  echo 'You must indicate a docker image name in 1st parameter'
else
  sudo docker run -p 5000:5000 $1
fi