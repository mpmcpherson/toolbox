#!/bin/bash
workingDir=/home/michaelmcpherson/src;
ls $workingDir > 'gitScan2.config';
runDir=$(pwd);
while read line;
do
	cd "$workingDir/$line";
	echo $(pwd);
	#git add .;
	git pull;
	git log;
	cd $runDir;
	#echo $line
done < gitScan2.config

#Basically archival of public repos in a way that checks vs local diffs from prior runs such that even if a git history is altered every change the puller sees is arrived, so if a pull has x new conmits they're all preserved, and if someone hacks the history that's preserved as a separate commit