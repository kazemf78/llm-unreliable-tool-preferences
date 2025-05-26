# 🕹️ Gaming Tool Preferences — Description Optimization in Tool-Calling LLMs

This repository contains code and data for our investigation into the role of natural language descriptions in shaping tool usage behavior by large language models within tool-calling systems (e.g., MCP, OpenAI function calling). It extends the [BFCL framework](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard) with:

- New **description optimization** modes
- A complete **modification + generation + evaluation pipeline**

[//]: # (- Support for both **local and API-based models**)

[//]: # (📄 This is the official implementation for our paper:)

[//]: # ()
[//]: # (> **"Gaming Tool Preferences: Exposing Description-Induced Biases in Tool-Calling LLMs"**  )

[//]: # (> *[Authors Redacted]*  )

[//]: # (> [arXiv link coming soon])

---

## 🧠 Motivation

Tool selection in LLMs is surprisingly fragile. Simply tweaking a function’s natural language description—without changing what the tool does—can cause massive changes in usage.

This repo lets you **experiment with and evaluate** such description changes. In our paper, we show:
- Some edits increase tool usage by **10× or more**.
- Certain cues (assertiveness, examples, name-dropping) strongly bias usage.
- Combined edits consistently beat every single strategy across 10 models.

---

## 🛠️ Installation & Setup

### Basic Installation

```bash
# Create a new Conda environment
conda create -n tool_optim python=3.10
conda activate tool_optim

# Navigate to project directory before running the next command
cd <gaming-tool-preferences>

# Install dependencies
pip install -e .
```

### Local Model Support (Optional)

If you plan to run local models (like LLaMA or Mistral), install a backend:

**Using `vllm` (T4/V100/etc):**

```bash
pip install -e .[oss_eval_vllm]
```

### Environment Variables

Copy and configure your `.env` file:

```bash
cp .env.example .env
# Fill in required values like API keys (for GPT, Claude, etc.)
```

---

## 🚀 How to Run the Pipeline

All tasks (modification, generation, evaluation) are handled by:

```bash
./scripts/whole_pipeline.sh [OPTIONS]
```

### Common Options

| Option                  | Description                                                     |
|-------------------------|-----------------------------------------------------------------|
| `--enable-modification` | Run the dataset modification step via `modify_bfcl_func.py`.    |
| `--enable-generation`   | Run `bfcl generate` for the constructed categories.             |
| `--enable-evaluation`   | Run `bfcl evaluate` on generated outputs.                       |
| `--skip-existing`       | Skip steps where output files already exist.                    |
| `--use-local-model`     | Use local backend (`vllm`, `sglang`) with GPU flags.            |
| `--model <model_name>`  | Override the default model. Supports API and local model names. |

---

## 🔍 Example Usage

### Full pipeline using default API model

```bash
./scripts/whole_pipeline.sh \
  --enable-modification \
  --enable-generation \
  --enable-evaluation
```

### Use a local model

```bash
./scripts/whole_pipeline.sh \
  --enable-generation \
  --enable-evaluation \
  --use-local-model \
  --model meta-llama/Llama-3.1-8B-Instruct
```

Automatically appends:

```bash
--backend vllm --num-gpus 1 --gpu-memory-utilization 0.9
```

### Reasoning-focused API model (e.g., `o1`, `o3-mini`, `o4-mini`)

```bash
./scripts/whole_pipeline.sh \
  --enable-generation \
  --enable-evaluation \
  --model o4-mini-2025-04-16-FC
```

If the model name starts with `o1`, `o3-mini`, or `o4-mini` (if it is a reasoning model from openAI), the script will *
*append `--temperature 1`**.

---

## 🧩 Customizing Modes

All pairwise combinations of optimization strategies are defined in:

```bash
atomic_modes=(
  "original"
  "addExample"
  "companyName"
  "increaseLength"
  "makeCasual"
  "makeProfessional"
  "endorsementLine"
  "maintenanceLine"
  "numbersLine"
  "fusion"
)
```

To **add a new optimization mode**, implement the new mode in `func_description_optim.py`, and then just append that to
`atomic_modes` in this shell script.

To **limit what gets run**, remove modes from this list. This affects:

- Dataset modification
- Generation
- Evaluation

---

## 📁 Project Structure

Expected directory layout:

```
gaming-tool-preferences/
│
├── data/
│   └── possible_answer/
├── score/
├── logs/
├── scripts/
│   └── whole_pipeline.sh
├── func_description_optim.py
├── modify_bfcl_func.py
└── README.md
```

You can run the script from either the **project root** or the `scripts/` folder.

---

## 📝 Notes for Contributors

- To implement a new optimization strategy:
    - Add your logic as a separate method in `FuncDescripOptim` inside `func_description_optim.py`.
    - Then reference it in the public router function (You can find other examples inside that file for reference).

- After implementing your optimization strategy and adding it to `func_description_optim.py`, you can add the new
  defined mode in the `atomic_modes` variable in `scripts/whole_pipeline.sh` script and compare it against other
  optimization methods. Basically you need to create the new datasets using the modification flag. When you create a new
  dataset, an entry will be auto-added to:
  ```python
  bfcl/constants/category_mapping.py
  ```
  Please **do not remove others’ entries**.

