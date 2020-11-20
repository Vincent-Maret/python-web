#!/bin/bash

# Build and run docker image tp:1

if [ -z $1 ]
then
  echo 'You must indicate a docker image name in 1st parameter'
else
  ./buildDockerImage.sh $1
  ./runDockerImage.sh $1
fi