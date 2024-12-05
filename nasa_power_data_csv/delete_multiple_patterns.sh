#!/bin/bash

# Define the patterns to match
patterns=("region_2_TS_" "region_3_TS_" "region_4_TS_" "region_5_TS_" "region_6_TS_")

# Iterate over each pattern and delete matching files
for pattern in "${patterns[@]}"; do
  find . -name "*$pattern*" -delete
done
