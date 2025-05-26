# Competing Function Calls with Description Optimization

This Codebase is directly adapted from the original BFCL function calling leaderboard [here](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard). For environment set up, check their original README file.


## How to run
- First run `bash scripts/modify_bfcl_func.sh` to generate the new dataset with duplicated functions with optimized descriptions. 
    - Modify the four variables `original_category`, `duplication_times`, `modes`, and `order` defined on top based on your need, and the new_category_name is automatically defined based on that with a predefined naming format.
    - Use lowerCamelCase for the `modes` names, **do not have under_scores in the mode name for any single mode.** Mode names are supposed to be separated by under_score when `duplication_times` >= 2.
- After the new dataset is created, run `bash scripts/run_generate.sh` to get the model inference results.
    - Modify the `categories` variable in the script accordingly.
- After the inference results are obtained, run `bash scripts/run_evaluate.sh` to get the scores.
    - Modify the `categories` variable in the script accordingly.

## A few notes
- Whenever you create a new dataset of new category, there will automatically be a new entry written to `TEST_FILE_MAPPING` at `bfcl/constants/category_mapping.py`. Git will track this as well. Please make sure you do not remove previously added entries, and push your new changes in time.
- To add new description optimization methods, add you new private function in class `FuncDescripOptim` in `func_description_optim.py`, and add your case in the public router function.





