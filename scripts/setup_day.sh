#!/usr/bin/env bash

# Arg parsing
if [ $# -eq 0 ] || [ "$1" == "help" ] ; then
  echo "Usage: $0 DAY_NUMBER"
  echo "    Sets up files for the advent day"
  echo "Arguments:"
  echo "    DAY_NUMBER: (Required) the number of the calendar day"
  echo 
  exit
fi

PROJECT_HOME=$HOME/git/aoc2017
cp $PROJECT_HOME/day_template.py $PROJECT_HOME/day_$1.py
touch $PROJECT_HOME/briefs/day_$1.txt
touch $PROJECT_HOME/inputs/day_$1.txt
