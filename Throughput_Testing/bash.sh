#!/bin/bash

stringsForDelay=(
    '50'
    '100'
    '200'
    '500'
    '800'
    '1000'
    '1200'
    '1500'
    '2000'
)
stringsForLossAndCorruptAndReorder=(
    '5'
    '10'
    '20'
    '30'
    '50'
    '60'
    '70'
    '90'
)
for i in "${stringsForDelay[@]}"
do
   echo ${i} >>Delay.txt
   out=`sudo tc qdisc add dev enp0s3 root netem delay ${i}ms`
   out=`python -i test.py`
   echo ${out} >> Delay.txt
   out=`sudo tc qdisc del dev enp0s3 root netem delay ${i}ms`
   # or do whatever with individual element of the array
done

for i in "${stringsForDelay[@]}"
do
    for j in "${stringsForLossAndCorruptAndReorder[@]}"
    do 
	echo ${i} >>DelayAndLoss.txt
	echo ${j} >> DelayAndLoss.txt
        out=`sudo tc qdisc add dev enp0s3 root netem delay ${i}ms`
	out=`sudo tc qdisc change dev enp0s3 root netem loss ${j}%`
        out=`python -i test.py`
	echo ${out} >> DelayAndLoss.txt
        out=`sudo tc qdisc del dev enp0s3 root netem delay ${i}ms`
    done
done

for i in "${stringsForDelay[@]}"
do
    for j in "${stringsForLossAndCorruptAndReorder[@]}"
    do 
	echo ${i} >>DelayAndCorrupt.txt
	echo ${j} >> DelayAndCorrupt.txt
        out=`sudo tc qdisc add dev enp0s3 root netem delay ${i}ms`
	out=`sudo tc qdisc change dev enp0s3 root netem corrupt ${j}%`
        out=`python -i test.py`
	echo ${out} >> DelayAndCorrupt.txt
        out=`sudo tc qdisc del dev enp0s3 root netem delay ${i}ms`
    done
done

for i in "${stringsForLossAndCorruptAndReorder[@]}"
do
   echo ${i} >>Reorder.txt
   out=`sudo  tc qdisc add dev enp0s3 root netem delay 10ms reorder ${i}%`
   out=`python -i test.py`
   echo ${out} >> Reorder.txt
   out=`sudo  tc qdisc del dev enp0s3 root netem delay 10ms reorder ${i}%`
   # or do whatever with individual element of the array
done

