#!/bin/bash

for i in $(seq 1 $1) ; do
	./db_layers.py $i &
	#pids[${i}]=$!
done

# # wait for all pids
# for pid in ${pids[*]}; do
#     wait $pid
# done

# wait for all pids
for pid in $(jobs -p); do
    wait $pid
done