import json
import copy
import argparse
import logging
import random
from concurrent.futures import ThreadPoolExecutor
from typing import List, Optional
from func_description_optim import FuncDescripOptim
import re
from tqdm import tqdm
from pathlib import Path
import numpy as np


class ModifyFunction:
    def __init__(self, dataset_path: str):
        self.dataset_path = dataset_path
        self.samples = self._load_dataset()
        self.duplication_metadata = []  # For storing per-sample info

    def _load_dataset(self) -> List[dict]:
        with open(self.dataset_path, "r", encoding="utf-8") as f:
            data = [json.loads(line) for line in f]
        return data

    def _process_sample(self, sample, function_names_to_duplicate, modes, mode_arg, duplication_times, order,
                        new_id_prefix, random_pick):
        original_functions = sample.get("function", [])
        if not original_functions:
            return sample, {}

        if new_id_prefix:
            try:
                sample["id"] = new_id_prefix + "_" + sample["id"].rsplit("_", 1)[-1]
            except Exception:
                logging.warning("Couldn't update the sample id", exc_info=True)

        if random_pick and not function_names_to_duplicate:
            selected_funcs = [random.choice(original_functions)["name"]]
        else:
            selected_funcs = function_names_to_duplicate or []

        modified_functions = []
        for func in original_functions:
            is_selected = func["name"] in selected_funcs
            if is_selected:
                for i in range(duplication_times):
                    func_dup = copy.deepcopy(func)
                    dup_mode = modes[i] if modes and i < len(modes) else "naive"
                    dup_mode_arg = mode_arg[i] if mode_arg and i < len(mode_arg) else None
                    func_dup["description"] = FuncDescripOptim.design_description(
                        func_dup["description"], mode=dup_mode, mode_arg=dup_mode_arg,
                        func_name=func_dup["name"], func_params=func_dup["parameters"]
                    )
                    modified_functions.append((func_dup, dup_mode))
            modified_functions.append((copy.deepcopy(func), "original"))

        # order
        if order == "original_first":
            modified_functions.sort(key=lambda x: 1 if x[1] != "original" else 0)
        elif order == "duplicate_first":
            modified_functions.sort(key=lambda x: 0 if x[1] != "original" else 1)
        elif order == "random":
            random.shuffle(modified_functions)

        # rename
        renamed_functions = []
        per_sample_meta = {"duplicated_func_name": selected_funcs[0] if selected_funcs else None, "dup_mode": {}}
        for i, (func, mode) in enumerate(modified_functions):
            old_name = func["name"]
            new_name = f"{old_name}{i + 1}"
            per_sample_meta["dup_mode"][new_name] = mode
            func["name"] = new_name
            renamed_functions.append(func)

        sample["function"] = renamed_functions
        return sample, per_sample_meta

    def _process_sample_V2(self, sample, function_names_to_duplicate, modes, mode_arg, duplication_times, order,
                           new_id_prefix, random_pick):
        original_functions = sample.get("function", [])
        if not original_functions:
            return sample, {}

        if new_id_prefix:
            try:
                sample["id"] = new_id_prefix + "_" + sample["id"].rsplit("_", 1)[-1]
            except Exception:
                logging.warning("Couldn't update the sample id", exc_info=True)

        if random_pick and not function_names_to_duplicate:
            selected_funcs = [random.choice(original_functions)["name"]]
        else:
            selected_funcs = function_names_to_duplicate or []

        modified_functions = []
        for func in original_functions:
            is_selected = func["name"] in selected_funcs
            if is_selected:
                for i in range(duplication_times):
                    func_dup = copy.deepcopy(func)
                    dup_mode = modes[i] if modes and i < len(modes) else "naive"
                    dup_mode_arg = mode_arg[i] if mode_arg and i < len(mode_arg) else None
                    func_dup["description"] = FuncDescripOptim.design_description(
                        func_dup["description"], mode=dup_mode, mode_arg=dup_mode_arg,
                        func_name=func_dup["name"], func_params=func_dup["parameters"]
                    )
                    modified_functions.append((func_dup, dup_mode))
                # modified_functions.append((copy.deepcopy(func), "original"))

        # order
        # if order == "original_first":
        #     modified_functions.sort(key=lambda x: 1 if x[1] != "original" else 0)
        # elif order == "duplicate_first":
        #     modified_functions.sort(key=lambda x: 0 if x[1] != "original" else 1)
        # elif order == "random":
        #     random.shuffle(modified_functions)
        modified_functions_list = []
        modified_functions_list.append(modified_functions)
        modified_functions_list.append(reversed(copy.deepcopy(modified_functions)))

        samples = []
        per_sample_metas = []
        for modified_functions_item in modified_functions_list:
            # rename
            renamed_functions = []
            per_sample_meta = {"duplicated_func_name": selected_funcs[0] if selected_funcs else None, "dup_mode": {}}
            for i, (func, mode) in enumerate(modified_functions_item):
                old_name = func["name"]
                new_name = f"{old_name}{i + 1}"
                per_sample_meta["dup_mode"][new_name] = mode
                func["name"] = new_name
                renamed_functions.append(func)

            sample["function"] = renamed_functions
            samples.append(copy.deepcopy(sample))
            per_sample_metas.append(per_sample_meta)
        return samples, per_sample_metas

    def duplicate_selected_functions(
            self,
            function_names_to_duplicate: Optional[List[str]] = None,
            modes: Optional[List[str]] = None,
            random_pick: bool = False,
            duplication_times: int = 1,
            order: str = "original_first",
            new_id_prefix: str = None,
            mode_arg: Optional[List[str]] = None,
    ):
        updated_samples = [[], []]
        duplication_metadata = [[], []]

        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = []
            for sample in self.samples:
                # futures.append(executor.submit(
                #     self._process_sample,
                #     sample,
                #     function_names_to_duplicate,
                #     modes,
                #     mode_arg,
                #     duplication_times,
                #     order,
                #     new_id_prefix,
                #     random_pick
                # ))
                futures.append(executor.submit(
                    self._process_sample_V2,
                    sample,
                    function_names_to_duplicate,
                    modes,
                    mode_arg,
                    duplication_times,
                    order,
                    new_id_prefix,
                    random_pick
                ))

            for future in tqdm(futures):
                sample_results, metadatas = future.result()
                suffixes = [f"{mode}_first" for mode in modes] if modes else ["", ""]

                def update_ids(sample, suffix):
                    sample["id"] = new_id_prefix + "_" + suffix + "_" + sample["id"].rsplit("_", 1)[-1]
                    return sample

                updated_samples[0].append(update_ids(sample_results[0], suffixes[0]))
                updated_samples[1].append(update_ids(sample_results[1], suffixes[1]))
                duplication_metadata[0].append(metadatas[0])
                duplication_metadata[1].append(metadatas[1])

        self.sample_set = updated_samples
        self.duplication_metadata_set = duplication_metadata

    def save_dataset(self, output_path: str, meta_output_path: str = None, modes: tuple = None):
        suffixes = [f"{mode}_first" for mode in modes] if modes else ["", ""]
        for samples, meta_data, suffix in zip(self.sample_set, self.duplication_metadata_set, suffixes):
            with open(output_path.replace(".json", f"_{suffix}.json"), "w", encoding="utf-8") as f:
                print("=" * 20, output_path.replace(".json", f"_{suffix}.json"))
                for sample in samples:
                    json.dump(sample, f, ensure_ascii=False)
                    f.write("\n")

        if meta_output_path:
            for meta_data, suffix in zip(self.duplication_metadata_set, suffixes):
                np.save(meta_output_path.replace(".json", f"_{suffix}.json"), meta_data)


class ModifyAnswer:
    def __init__(self, answer_path: str):
        self.answer_path = answer_path
        self.answers = self._load_answer()

    def _load_answer(self) -> List[dict]:
        with open(self.answer_path, "r", encoding="utf-8") as f:
            data = [json.loads(line) for line in f]
        return data

    def update_answers(
            self,
            function_names_to_duplicate: Optional[List[str]] = None,
            duplication_times: int = 1,
            random_pick: bool = False,
            dataset_samples: List[dict] = None,
            new_id_prefix: str = None,
    ):
        id_to_answer = {item["id"]: item for item in self.answers}
        if new_id_prefix:
            new_entries = {}
            for item_id in id_to_answer.keys():
                try:
                    possible_id = new_id_prefix + "_" + item_id.rsplit("_", 1)[1]
                    new_entries[possible_id] = copy.deepcopy(id_to_answer[item_id])
                    new_entries[possible_id]["id"] = possible_id
                except Exception as e:
                    logging.warning("Couldn't find the new sample id.", exc_info=True)
            id_to_answer.update(new_entries)

        updated_answers = []

        for sample in dataset_samples:
            sample_id = sample["id"]
            answer_item = id_to_answer.get(sample_id)
            if not answer_item:
                continue
            answer_item = copy.deepcopy(answer_item)

            ground_truth = answer_item.get("ground_truth", [])

            # Collect existing function names
            existing_functions = [list(gt.keys())[0] for gt in ground_truth]

            if random_pick and not function_names_to_duplicate:
                selected_funcs = [random.choice(existing_functions)]
            else:
                selected_funcs = function_names_to_duplicate or []

            new_ground_truth = []

            for gt in ground_truth:
                func_name = list(gt.keys())[0]
                func_args = gt[func_name]

                # Always rename original function -> funcname1
                new_ground_truth.append({func_name + "1": func_args})

                if func_name in selected_funcs:
                    for i in range(duplication_times):
                        new_func_name = func_name + str(i + 2)
                        new_ground_truth.append({new_func_name: func_args})

            answer_item["ground_truth"] = new_ground_truth
            updated_answers.append(answer_item)
        self.answers = updated_answers

    def save_answers(self, output_path: str):
        with open(output_path, "w", encoding="utf-8") as f:
            print("=" * 20, output_path)
            for answer in self.answers:
                json.dump(answer, f, ensure_ascii=False)
                f.write("\n")


def extract_new_id_prefix_from_filename(file_path):
    file_stem = Path(file_path).stem  # remove '.json'

    # Match BFCL_v followed by digits, underscore, then capture the rest
    match = re.search(r'BFCL_v\d+_(.+)', file_stem)
    if not match:
        return None

    id_prefix = match.group(1)  # the part after BFCL_v<number>_
    return id_prefix


DS_PREFIX = "BFCL_v3"  # Update this to the correct version prefix


def extract_category_from_output_path(output_path: str) -> Optional[str]:
    file_stem = Path(output_path).stem  # e.g., BFCL_v1_live_simple_new
    prefix = f"{DS_PREFIX}_"
    if prefix in file_stem:
        return file_stem.split(prefix, 1)[-1]
    return None


def append_category_to_test_file_mapping(category: str, constants_file_path: str):
    new_entry = f'TEST_FILE_MAPPING["{category}"] = f"{{VERSION_PREFIX}}_{category}.json"'

    with open(constants_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    start_index = None
    end_index = None
    if new_entry in [line.strip() for line in lines]:
        return  # Already exists
    for i, line in enumerate(lines):
        if "TEST_FILE_MAPPING" in line and "=" in line:
            start_index = i
        if start_index is not None and line.strip() == "}":
            end_index = i
            break

    if end_index is not None:
        # Insert after the closing brace
        lines.insert(end_index + 1, "\n" + new_entry)

        with open(constants_file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
    else:
        raise ValueError("Could not find TEST_FILE_MAPPING block to append to.")


def main():
    parser = argparse.ArgumentParser(description="Duplicate and modify functions in a dataset and answer file.")
    parser.add_argument("--input_path", type=str, required=True, help="Path to input dataset JSON.")
    parser.add_argument("--output_path", type=str, required=True, help="Path to save modified dataset JSON.")
    parser.add_argument("--answer_path", type=str, required=True, help="Path to input answer JSON.")
    parser.add_argument("--answer_output_path", type=str, required=True, help="Path to save modified answer JSON.")
    parser.add_argument("--functions_to_duplicate", type=str,
                        help="Comma-separated function names to duplicate (e.g., func1,func2).")
    parser.add_argument("--modes", type=str,
                        help="'_' separated list of modes for each duplication (e.g., naive_synonym_swap).")
    parser.add_argument("--mode_args", type=str,
                        help="'_' separated list of mode parameters for each duplication (e.g., 0.5_0.5).")
    parser.add_argument("--random_pick", action="store_true",
                        help="Randomly pick one function per sample to duplicate if set.")
    parser.add_argument("--duplication_times", type=int, default=1,
                        help="Number of times to duplicate each selected function.")
    parser.add_argument("--order", type=str, default="original_first",
                        choices=["original_first", "duplicate_first", "random", "none"],
                        help="Order of functions in output: original_first, duplicate_first, or random.")

    args = parser.parse_args()
    category = extract_category_from_output_path(args.output_path)
    if not category:
        raise ValueError(
            "Couldn't extract category from output path. Ensure your output path follows the naming convention:\n"
            "data/BFCL_v3_{category}.json.\nFor example, with category=live_simple_new: data/BFCL_v3_live_simple_new.json")

    function_names = [name.strip() for name in
                      args.functions_to_duplicate.split(",")] if args.functions_to_duplicate else None
    modes = [m.strip() for m in args.modes.split("_")] if args.modes else None
    mode_args = [m.strip() for m in args.mode_args.split("_")] if args.mode_args else None

    if modes and len(modes) != args.duplication_times:
        raise ValueError("Length of --modes must match duplication_times")

    new_id_prefix = extract_new_id_prefix_from_filename(args.output_path)
    function_modifier = ModifyFunction(dataset_path=args.input_path)
    function_modifier.duplicate_selected_functions(
        function_names_to_duplicate=function_names,
        modes=modes,
        random_pick=args.random_pick,
        duplication_times=args.duplication_times,
        order=args.order,
        new_id_prefix=new_id_prefix,
        mode_arg=mode_args,
    )
    function_modifier.save_dataset(output_path=args.output_path, meta_output_path=args.output_path + ".meta.npy",
                                   modes=modes)

    suffixes = [f"{mode}_first" for mode in modes] if modes else ["", ""]
    for samples, suffix in zip(function_modifier.sample_set, suffixes):
        answer_modifier = ModifyAnswer(answer_path=args.answer_path)
        answer_modifier.update_answers(
            function_names_to_duplicate=function_names,
            duplication_times=args.duplication_times,
            random_pick=args.random_pick,
            dataset_samples=samples,
            new_id_prefix=new_id_prefix + "_" + suffix,
        )
        answer_modifier.save_answers(args.answer_output_path.replace(".json", f"_{suffix}.json"))
        # answer_modifier.update_answers(
        #     function_names_to_duplicate=function_names,
        #     duplication_times=args.duplication_times,
        #     random_pick=args.random_pick,
        #     dataset_samples=function_modifier.samples,
        #     new_id_prefix=new_id_prefix,
        # )
        # answer_modifier.save_answers(output_path=args.answer_output_path)

        category = extract_category_from_output_path(args.answer_output_path.replace(".json", f"_{suffix}.json"))
        append_category_to_test_file_mapping(category, "bfcl/constants/category_mapping.py")


if __name__ == "__main__":
    main()
