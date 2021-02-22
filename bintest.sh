#!/bin/bash
workingDir=/home/michaelmcpherson/src;
targets=`ls $workingDir`;

for fn in "$targets"; 
do cat "$fn"; done

