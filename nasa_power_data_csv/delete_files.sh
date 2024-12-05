#!/bin/bash

# Replace 'region_1_TS_' with the desired pattern
pattern="region_1_TS_"

# Find and delete files matching the pattern
find . -name "*$pattern*" -delete
