#!/bin/bash

path="logs/"
files="";
n=3
function readf {
        files+=$1$' '
	for file in `cat $1`
	do
		echo $file
		if [ $(echo $files | grep $file | wc -c) == 0 ] ;  then
			readf $path$file.log
		fi
	done
}		

readf logs/10.0.3.2.log | sort | uniq

