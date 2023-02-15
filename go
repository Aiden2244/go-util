#!/usr/bin/env bash

cd ~/.bookmarks
touch bookmarks.txt

if [[ $# == 0 ]] || [[ $# > 3 ]]; then
	echo "Error: invalid number of arguments"
	echo "Usage: go [-l] [-r alias] [-a alias link] [alias]"
	echo "Type 'go -h' for help"
elif [[ $# == 1 ]]; then
	python3 ~/.bookmarks/go.py "$1"
else
	if [[ $1 == "-r" ]] && [[ $# == 2 ]]; then
		grep -v "^$2" ~/.bookmarks/bookmarks.txt > ~/.bookmarks/temp.txt
		rm ~/.bookmarks/bookmarks.txt
		mv ~/.bookmarks/temp.txt ~/.bookmarks/bookmarks.txt
		echo "Removed link associated with alias $2"
	elif [[ $# == 3 ]] && [[ $1 == "-a" ]]; then
		python3 ~/.bookmarks/go.py "-a" "$2" "$3"
	else
		echo "Error: invalid arguments"
	fi 
fi

# © Aiden McCormack, 2023. All rights reserved.



