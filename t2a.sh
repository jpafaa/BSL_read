#! /bin/sh
# Shell script to do a mass convert of 
# tiff to bsl files based on a input prefix ($1)
# a start number ($2) and an end number ($3)
# the output is directed to an incremental bsl file
# whose first letter is given by the variable $4
# The extension to the filename is given by 
# the number in the name of the file.
# the output from xotoko is not directed to the screen
# instead it goes to a file specified by the OUT+$5 input with
# an extension .TXT

inprefix=$1
start=$2
end=$3
out=$4
intfile=$5


while [ $start -le $end ]
do
	ext=`printf "%03s" "${start}" `
	tiff2bsl $inprefix$start'.tif' ${out}000.$ext 
	bsl2ascii ${out}000.$ext
done
rm ${out}00*.*
exit
