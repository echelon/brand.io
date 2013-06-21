#!/bin/bash 
# Upload to website
# Login requires SSH key

shopt -s expand_aliases
alias rsync="rsync -zrpvu -e ssh --exclude-from=exclude.txt --progress"

function print_status() {
	status=$1
	length=${#1}
	echo ''
	echo $status
	for i in $(seq $length); do echo -n '-'; done
	echo ''
}

print_status 'Built Files: Running rsync to brand.io...'
rsync ./output/ possibilistic@brand.io:/home/possibilistic/brand.io/public

print_status 'Assets: Running rsync to brand.io...'
rsync ./assets/ possibilistic@brand.io:/home/possibilistic/brand.io/public

print_status 'Javascript: Running rsync to brand.io...'
rsync ./js/ possibilistic@brand.io:/home/possibilistic/brand.io/public/js

print_status 'CSS: Running rsync to brand.io...'
rsync ./css/ possibilistic@brand.io:/home/possibilistic/brand.io/public

