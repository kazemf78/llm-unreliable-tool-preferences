#!/bin/bash


categories=( "live_simple_dup1_makeMultiLingual_original_first", 
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

# for category in "${categories[@]}"; do
#   echo "Running category: $category"
#   bfcl generate \
#     --model "$model" \
#     --test-category "$category" \
#     --num-threads 20 \
#     --include-input-log
# done

for category in "${categories[@]}"; do
  echo "Running category: $category"
  bfcl generate \
    --model "$model" \
    --test-category "$category" \
    --backend vllm \
    --num-gpus 4 \
    --gpu-memory-utilization 0.9 \
    --local-model-path /fs/cml-scratch/yzcheng/cache2/Qwen2_5-7B-Instruct
done