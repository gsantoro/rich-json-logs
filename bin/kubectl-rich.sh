#!/bin/bash
/usr/local/bin/kubectl logs $1 -n $2 --context $3 \
        | python main.py \
        | less -r