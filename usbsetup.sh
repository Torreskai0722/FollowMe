#!/usr/bin/env bash

for f in /dev/ttyMOTOR*; do
	sudo chmod 777 $f
	echo "Set permission for $f"
done

sudo chmod 666 /dev/ttyLIDAR
echo "Set permission for /dev/ttyLIDAR"
