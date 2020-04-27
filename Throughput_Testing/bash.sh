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
out=`sudo tc qdisc add dev wlp3s0 root netem delay 10ms`
for i in "${stringsForDelay[@]}"
do
   echo ${i} >>Delay.txt
   out=`sudo tc qdisc change dev wlp3s0 root netem delay ${i}ms`
   out=`python test1.py &`
   c=${out}
   out=`python test.py`
   echo ${out} >> Delay.txt
   out=`kill ${c}`
   # or do whatever with individual element of the array
done

for i in "${stringsForDelay[@]}"
do
    out=`sudo tc qdisc change dev wlp3s0 root netem delay ${i}ms`
    for j in "${stringsForLossAndCorruptAndReorder[@]}"
    do 
	echo ${i} >>DelayAndLoss.txt
	echo ${j} >> DelayAndLoss.txt
	out=`sudo tc qdisc change dev wlp3s0 root netem loss ${j}%`
        out=`python test1.py &`
        c=${out}
        out=`python test.py`
        echo ${out} >> DelayAndLoss.txt
        out=`kill ${c}`
    done
done

out=`sudo tc qdisc del dev wlp3s0 root netem delay 10ms`
out=`sudo tc qdisc add dev wlp3s0 root netem delay 10ms`
for i in "${stringsForDelay[@]}"
do
    out=`sudo tc qdisc change dev wlp3s0 root netem delay ${i}ms
    for j in "${stringsForLossAndCorruptAndReorder[@]}"
    do 
	echo ${i} >>DelayAndCorrupt.txt
	echo ${j} >> DelayAndCorrupt.txt
        out=`sudo tc qdisc change dev wlp3s0 root netem corrupt ${j}%`
        out=`python test1.py &`
        c= ${out}
        out=`python test.py`
        echo ${out} >> DelayAndCorrupt.txt
        out=`kill ${c}`
    done
done

out=`sudo tc qdisc del dev wlp3s0 root netem delay 10ms`
out=`sudo tc qdisc add dev wlp3s0 root netem delay 10ms`

for i in "${stringsForLossAndCorruptAndReorder[@]}"
do
   echo ${i} >>Reorder.txt
   out=`sudo  tc qdisc change dev wlp3s0 root netem delay 10ms reorder ${i}%`
   out=`python test1.py &`
   c=${out}
   out=`python test.py`
   echo ${out} >> Reorder.txt
   out=`kill ${c}`
   # or do whatever with individual element of the array
done
out=`sudo tc qdisc del dev wlp3s0 root netem delay 10ms`
