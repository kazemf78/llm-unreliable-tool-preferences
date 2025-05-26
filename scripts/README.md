# 🧪 `whole_pipeline.sh` — Dataset Modification, Generation, and Evaluation Pipeline

This script automates **modification**, **generation**, and **evaluation** of BFCL datasets using local or API-based
language models. It handles:

- Dynamic mode combinations
- Local vs API model settings
- Intelligent skipping of already-processed files
- Full logging for reproducibility

---

## 🚀 Usage

```bash
./scripts/whole_pipeline.sh [OPTIONS]
```

---

## ⚙️ Options

| Option                  | Description                                                                                         |
|-------------------------|-----------------------------------------------------------------------------------------------------|
| `--enable-modification` | Run the dataset modification step via `modify_bfcl_func.py`.                                        |
| `--enable-generation`   | Run `bfcl generate` for the constructed categories.                                                 |
| `--enable-evaluation`   | Run `bfcl evaluate` on generated outputs.                                                           |
| `--skip-existing`       | Skip steps where matching output files already exist.                                               |
| `--use-local-model`     | Use a local LLM backend (adds `--backend vllm` etc.).                                               |
| `--model <model_name>`  | Override the default model (`gpt-4.1-2025-04-14-FC`). Accepts both local paths and API model names. |

---

## 🧾 Example Usage

### ✅ Full pipeline using the default API model

```bash
./scripts/whole_pipeline.sh \
  --enable-modification \
  --enable-generation \
  --enable-evaluation \
  --skip-existing
```

### ✅ Use a **local model** (`meta-llama/Llama-3.1-8B-Instruct`)

```bash
./scripts/whole_pipeline.sh \
  --enable-generation \
  --enable-evaluation \
  --use-local-model \
  --model meta-llama/Llama-3.1-8B-Instruct \
  --skip-existing
```

Adds the following flags to generation:

```bash
--backend vllm --num-gpus 1 --gpu-memory-utilization 0.9
```

### ✅ Use an **API-based reasoning model** (e.g., `o1`, `o3-mini`, `o4-mini`)

```bash
./scripts/whole_pipeline.sh \
  --enable-generation \
  --enable-evaluation \
  --model o4-mini-2025-04-16-FC \
  --skip-existing
```

📌 When the model name **starts with** `o1`, `o3-mini`, or `o4-mini`, the script **automatically appends**:

```bash
--temperature 1
```

to improve **reasoning performance**.

---

## 🧩 Customizing Modes with `atomic_modes`

The script supports **pairwise combinations** of atomic optimization modes. To customize:

### Add or remove atomic transformations here:

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

### ✅ To add a new mode:

Just append it to the list.

### ✅ To limit what’s run:

Remove or comment out unwanted modes. This controls:

- What gets modified
- What gets generated
- What gets evaluated

---

## 📁 Project Structure

The script expects this layout:

```
your-project-root/
│
├── data/
├── score/
├── possible_answer/
├── logs/               # created if not present
├── scripts/
│   └── whole_pipeline.sh
├── modify_bfcl_func.py
```

You can run it from either the **project root** or `scripts/`.

---

## 📓 Logging

- Logs are written to:
  ```
  logs/run_<TIMESTAMP>.log
  ```
- Uses `tee` so you see real-time output and save everything for debugging.

---

## 🛠️ Top-Level Configuration (Inside Script)

You can customize defaults at the top of the script:

```bash
original_category="combined_simple_live_simple"
duplication_times=2
model="gpt-4.1-2025-04-14-FC"
export PRIORITY_WITH_V2=true
```