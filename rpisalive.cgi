#!/bin/bash

for i in {1..9}
do
        ping rpi0$i -c 1 -W 1 > /dev/null
        if [ $? -eq 0 ]; then
                echo "rpi0$i : alive"
                else
                echo "rpi0$i : dead"
        fi
done


for i in {10..20}
do
        ping rpi$i -c 1 -W 1 > /dev/null
        if [ $? -eq 0 ]; then
                echo "rpi$i : alive"
                else
                echo "rpi$i : dead" 
        fi
done
echo "Done"
