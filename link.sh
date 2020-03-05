#!/bin/bash
# Script to create symbolic links to concatenate multiple run results together.
# Usage: say we want to concatenate runs 0-2
#  1. create directory run012 and cd there
#  2. execute ../link.sh run0 run1 run2
#  3. the script links batches from those directories into the current directory

RUNS="$@"

NO=0
for RUN in ${RUNS} ; do
	FILES=`find "../${RUN}" -type f -name '*_out.csv'`
	for FILE in ${FILES} ; do
		LOCAL_FILE="batch${NO}_out.csv"
		ln -s ${FILE} ${LOCAL_FILE}
		NO=$((NO+1))
	done
done

