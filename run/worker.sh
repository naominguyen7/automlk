#!/bin/bash
while :
do
	echo "launching worker..."
	python run_worker.py $1
done
