#!/bin/bash

original_category="live_simple"
duplication_times=1
modes="fusionV2" # if you have multiple modes, please separate them with "_", e.g., "naive_detailed_paraphrase" for 3 different modes
order="duplicate_first"
mode_args="74389"
if [[ "$mode_args" == "-1" ]]; then
  # Special case: treat as "no argument"
  mode_args_str=""
  new_category_name="${original_category}_dup${duplication_times}_${modes}_${order}"
else
  mode_args_str="$mode_args"
  new_category_name="${original_category}_dup${duplication_times}_${modes}_${mode_args_str}_${order}"
fi

echo $new_category_name
#new_category_name="${original_category}_dup${duplication_times}_${modes}_${order}"
python modify_bfcl_func.py \
    --input_path data/BFCL_v3_${original_category}.json \
    --output_path data/BFCL_v3_${new_category_name}.json \
    --answer_path data/possible_answer/BFCL_v3_${original_category}.json \
    --answer_output_path data/possible_answer/BFCL_v3_${new_category_name}.json \
    --duplication_times ${duplication_times} \
    --modes ${modes} \
    --mode_args ${mode_args} \
    --order ${order} \
    --random_pick