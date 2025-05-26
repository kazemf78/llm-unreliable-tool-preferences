#!/bin/bash


# Set project root relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_DIR="$PROJECT_ROOT/logs"
mkdir -p "$LOG_DIR"

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
LOG_FILE="$LOG_DIR/run_${timestamp}.log"

exec > >(tee -a "$LOG_FILE") 2>&1


# Default: everything is OFF
ENABLE_GENERATION=false
ENABLE_EVALUATION=false
ENABLE_MODIFICATION=false
SKIP_EXISTING=false
USE_LOCAL_MODEL=false
model="gpt-4.1-2025-04-14-FC"
#model="o4-mini-2025-04-16-FC"
#model="meta-llama/Llama-3.1-8B-Instruct"
#model="Qwen/Qwen2.5-7B-Instruct-FC"

usage() {
  echo "Usage: $0 [--enable-generation] [--enable-evaluation] [--enable-modification] [--skip-existing]"
  exit 1
}

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
  case $1 in
    --enable-generation) ENABLE_GENERATION=true ;;
    --enable-evaluation) ENABLE_EVALUATION=true ;;
    --enable-modification) ENABLE_MODIFICATION=true ;;
    --skip-existing) SKIP_EXISTING=true ;;
    --use-local-model) USE_LOCAL_MODEL=true ;;
    --model)
      shift
      if [[ -z "$1" || "$1" == --* ]]; then
        echo "Error: --model requires a value"
        usage
      fi
      model="$1"
      ;;
    *) usage ;;
  esac
  shift
done

should_skip_category() {
  local glob_path=$1
  if $SKIP_EXISTING && compgen -G "$glob_path" > /dev/null; then
    echo "Skipping — output(s) already exist:"
    for file in $glob_path; do
      echo " ------ $file"
    done
    return 0
  fi
  return 1
}

echo "Shell: $SHELL"
echo "BASH_VERSION: $BASH_VERSION"
echo "==== RUN CONFIG ===="
echo "Model: $model"
echo "Enable Generation: $ENABLE_GENERATION"
echo "Enable Evaluation: $ENABLE_EVALUATION"
echo "Enable Modification: $ENABLE_MODIFICATION"
echo "Use Local Model: $USE_LOCAL_MODEL"
echo "Skip Existing: $SKIP_EXISTING"
echo "Project Root: $PROJECT_ROOT"
echo "===================="
original_category="combined_simple_live_simple"
duplication_times=2
export PRIORITY_WITH_V2=true
declare -A mode_args_map

#atomic_modes=("original" "addExample" "companyName" "increaseLength" "makeCasual" "makeProfessional" "endorsementLine" "maintenanceLine" "numbersLine")
atomic_modes=("original" "addExample" "companyName" "increaseLength" "makeCasual" "makeProfessional" "endorsementLine" "maintenanceLine" "numbersLine" "fusion")

modes=()
for ((i = 0; i < ${#atomic_modes[@]}; i++)); do
  for ((j = i + 1; j < ${#atomic_modes[@]}; j++)); do
    mode1="${atomic_modes[i]}"
    mode2="${atomic_modes[j]}"
    modes+=("${mode1}_${mode2}")
  done
done
orders=("none")

for mode in "${modes[@]}"; do
  for order in "${orders[@]}"; do
    args="${mode_args_map[$mode]}"
    args=${args:-"-1"}  # If empty, use -1
    for arg in ${args}; do
      if [[ "$arg" == "-1" ]]; then
        # Special case: treat as "no argument"
        mode_args_str=""
        if [[ "$order" == "none" ]]; then
          base_category="${original_category}_dup${duplication_times}_${mode}"
        else
          base_category="${original_category}_dup${duplication_times}_${mode}_${order}"
        fi
      else
        mode_args_str="$arg"
        if [[ "$order" == "none" ]]; then
          base_category="${original_category}_dup${duplication_times}_${mode}_${mode_args_str}"
        else
          base_category="${original_category}_dup${duplication_times}_${mode}_${mode_args_str}_${order}"
        fi
      fi
      echo $base_category
      echo "Processing configuration: mode=$mode, arg=$mode_args_str, order=$order"

      mod_output_glob="$PROJECT_ROOT/data/BFCL_v3_${base_category}_*.json"
      if $ENABLE_MODIFICATION; then
        if ! should_skip_category "$mod_output_glob"; then
          python "$PROJECT_ROOT/modify_bfcl_func.py" \
            --input_path data/BFCL_v3_${original_category}.json \
            --output_path data/BFCL_v3_${base_category}.json \
            --answer_path data/possible_answer/BFCL_v3_${original_category}.json \
            --answer_output_path data/possible_answer/BFCL_v3_${base_category}.json \
            --duplication_times ${duplication_times} \
            --modes ${mode} \
            --order ${order} \
            --random_pick \
  #          --mode_args ${mode_args_str}

          echo "Dataset for $base_category generated"
        fi
      fi


      if [[ "$order" == "none" ]]; then
        IFS='_' read -ra mode_parts <<< "$mode"
        mode1="${mode_parts[0]}"
        mode2="${mode_parts[1]}"
        category1="${base_category}_${mode1}_first"
        category2="${base_category}_${mode2}_first"

        for category in "$category1" "$category2"; do
#          echo "Running category: $category"

          output_glob="$PROJECT_ROOT/score/${model}/BFCL_v3_${category}_*.json"
          $ENABLE_GENERATION && should_skip_category "$output_glob" && continue
          if $ENABLE_GENERATION; then
            echo "Running bfcl generate for $category"

            CMD=(bfcl generate
              --model "$model"
              --test-category "$category"
              --include-input-log
            )

            if $USE_LOCAL_MODEL; then
              CMD+=(--backend vllm --num-gpus 1 --gpu-memory-utilization 0.9)
            else
              CMD+=(--num-threads 20)
            fi

            if [[ "$model" == o4-mini* || "$model" == o1* || "$model" == o3-mini* ]]; then
              CMD+=(--temperature 1)
            fi

            "${CMD[@]}"
            echo "Generation completed for $category"
          fi

          $ENABLE_EVALUATION && bfcl evaluate \
            --model "$model" \
            --test-category "$category"

          $ENABLE_EVALUATION && echo "Evaluation completed for $category"
          echo "---------------------------------------------"
        done
      else
        category="$base_category"
#        echo "Running category: $category"

        output_glob="$PROJECT_ROOT/score/${model}/BFCL_v3_${category}_*.json"
        $ENABLE_GENERATION && should_skip_category "$output_glob" && continue
        if $ENABLE_GENERATION; then
          echo "Running bfcl generate for $category"

          CMD=(bfcl generate
            --model "$model"
            --test-category "$category"
            --include-input-log
          )

          if $USE_LOCAL_MODEL; then
            CMD+=(--backend vllm --num-gpus 1 --gpu-memory-utilization 0.9)
          else
            CMD+=(--num-threads 20)
          fi

          if [[ "$model" == o4-mini* || "$model" == o1* || "$model" == o3-mini* ]]; then
            CMD+=(--temperature 1)
          fi

          "${CMD[@]}"
          echo "Generation completed for $category"
        fi

        $ENABLE_EVALUATION && bfcl evaluate \
          --model "$model" \
          --test-category "$category"

        $ENABLE_EVALUATION && echo "Evaluation completed for $category"
        echo "---------------------------------------------"
      fi

    done
  done
done