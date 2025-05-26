#!/bin/bash

categories=( 
    "live_simple_dup1_makeMultiLingual_original_first", 
    "live_simple_dup1_makeMultiLingual_duplicate_first",
    "live_simple_dup1_addExample_original_first",
    "live_simple_dup1_addExample_duplicate_first",
    "simple_dup1_makeMultiLingual_original_first",
    "simple_dup1_makeMultiLingual_duplicate_first",
    "simple_dup1_addExample_original_first",
    "simple_dup1_addExample_duplicate_first"
)

# model="gpt-4.1-2025-04-14-FC"
model="Qwen/Qwen2.5-7B-Instruct-FC"

for category in "${categories[@]}"; do
  echo "Running category: $category"
  bfcl evaluate \
    --model "$model" \
    --test-category "$category"
done