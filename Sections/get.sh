#!/bin/bash

BASE_URL="https://web.stanford.edu/class/archive/cs/cs109/cs109.1212/section"

# Loop from 1 to 9 and download each file
for i in {1..9}; do
    wget "${BASE_URL}/${i}/section${i}_soln.pdf"
    wget  "${BASE_URL}/${i}/section${i}.pdf"
done

