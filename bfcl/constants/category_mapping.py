VERSION_PREFIX = "BFCL_v3"

# These are in the PROMPT_PATH
# Commented out ones are not used in the current version of benchmarking
TEST_FILE_MAPPING = {
    # V1 Non-Live Dataset
    # "exec_simple": f"{VERSION_PREFIX}_exec_simple.json",
    # "exec_parallel": f"{VERSION_PREFIX}_exec_parallel.json",
    # "exec_multiple": f"{VERSION_PREFIX}_exec_multiple.json",
    # "exec_parallel_multiple": f"{VERSION_PREFIX}_exec_parallel_multiple.json",
    "simple": f"{VERSION_PREFIX}_simple.json",
    "irrelevance": f"{VERSION_PREFIX}_irrelevance.json",
    "parallel": f"{VERSION_PREFIX}_parallel.json",
    "multiple": f"{VERSION_PREFIX}_multiple.json",
    "parallel_multiple": f"{VERSION_PREFIX}_parallel_multiple.json",
    "java": f"{VERSION_PREFIX}_java.json",
    "javascript": f"{VERSION_PREFIX}_javascript.json",
    # "rest": f"{VERSION_PREFIX}_rest.json",
    # "sql": f"{VERSION_PREFIX}_sql.json",
    # "chatable": f"{VERSION_PREFIX}_chatable.json",

    # V2 Live Datasets
    "live_simple": f"{VERSION_PREFIX}_live_simple.json",
    "live_multiple": f"{VERSION_PREFIX}_live_multiple.json",
    "live_parallel": f"{VERSION_PREFIX}_live_parallel.json",
    "live_parallel_multiple": f"{VERSION_PREFIX}_live_parallel_multiple.json",
    "live_irrelevance": f"{VERSION_PREFIX}_live_irrelevance.json",
    "live_relevance": f"{VERSION_PREFIX}_live_relevance.json",

    # V3 Multi-turn Datasets
    "multi_turn_base": f"{VERSION_PREFIX}_multi_turn_base.json",
    "multi_turn_miss_func": f"{VERSION_PREFIX}_multi_turn_miss_func.json",
    "multi_turn_miss_param": f"{VERSION_PREFIX}_multi_turn_miss_param.json",
    "multi_turn_long_context": f"{VERSION_PREFIX}_multi_turn_long_context.json",
    # "multi_turn_composite": f"{VERSION_PREFIX}_multi_turn_composite.json",

    # newly added
    "combined_simple_live_simple": f"{VERSION_PREFIX}_combined_simple_live_simple.json",
}

TEST_FILE_MAPPING["combined_simple_live_simple_dup2_numbersLine_fusion_fusion_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_numbersLine_fusion_fusion_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_numbersLine_fusion_numbersLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_numbersLine_fusion_numbersLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_maintenanceLine_fusion_fusion_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_maintenanceLine_fusion_fusion_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_maintenanceLine_fusion_maintenanceLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_maintenanceLine_fusion_maintenanceLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_endorsementLine_fusion_fusion_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_endorsementLine_fusion_fusion_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_endorsementLine_fusion_endorsementLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_endorsementLine_fusion_endorsementLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeProfessional_fusion_fusion_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeProfessional_fusion_fusion_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeProfessional_fusion_makeProfessional_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeProfessional_fusion_makeProfessional_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeCasual_fusion_fusion_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeCasual_fusion_fusion_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeCasual_fusion_makeCasual_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeCasual_fusion_makeCasual_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_increaseLength_fusion_fusion_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_increaseLength_fusion_fusion_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_increaseLength_fusion_increaseLength_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_increaseLength_fusion_increaseLength_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_fusion_fusion_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_fusion_fusion_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_fusion_companyName_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_fusion_companyName_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_fusion_fusion_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_fusion_fusion_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_fusion_addExample_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_fusion_addExample_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_fusion_fusion_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_fusion_fusion_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_fusion_original_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_fusion_original_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_maintenanceLine_numbersLine_numbersLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_maintenanceLine_numbersLine_numbersLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_maintenanceLine_numbersLine_maintenanceLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_maintenanceLine_numbersLine_maintenanceLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_endorsementLine_numbersLine_numbersLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_endorsementLine_numbersLine_numbersLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_endorsementLine_numbersLine_endorsementLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_endorsementLine_numbersLine_endorsementLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_endorsementLine_maintenanceLine_maintenanceLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_endorsementLine_maintenanceLine_maintenanceLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_endorsementLine_maintenanceLine_endorsementLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_endorsementLine_maintenanceLine_endorsementLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeProfessional_numbersLine_numbersLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeProfessional_numbersLine_numbersLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeProfessional_numbersLine_makeProfessional_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeProfessional_numbersLine_makeProfessional_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeProfessional_maintenanceLine_maintenanceLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeProfessional_maintenanceLine_maintenanceLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeProfessional_maintenanceLine_makeProfessional_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeProfessional_maintenanceLine_makeProfessional_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeProfessional_endorsementLine_endorsementLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeProfessional_endorsementLine_endorsementLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeProfessional_endorsementLine_makeProfessional_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeProfessional_endorsementLine_makeProfessional_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeCasual_numbersLine_numbersLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeCasual_numbersLine_numbersLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeCasual_numbersLine_makeCasual_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeCasual_numbersLine_makeCasual_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeCasual_maintenanceLine_maintenanceLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeCasual_maintenanceLine_maintenanceLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeCasual_maintenanceLine_makeCasual_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeCasual_maintenanceLine_makeCasual_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeCasual_endorsementLine_endorsementLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeCasual_endorsementLine_endorsementLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeCasual_endorsementLine_makeCasual_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeCasual_endorsementLine_makeCasual_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeCasual_makeProfessional_makeProfessional_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeCasual_makeProfessional_makeProfessional_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_makeCasual_makeProfessional_makeCasual_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_makeCasual_makeProfessional_makeCasual_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_increaseLength_numbersLine_numbersLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_increaseLength_numbersLine_numbersLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_increaseLength_numbersLine_increaseLength_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_increaseLength_numbersLine_increaseLength_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_increaseLength_maintenanceLine_maintenanceLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_increaseLength_maintenanceLine_maintenanceLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_increaseLength_maintenanceLine_increaseLength_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_increaseLength_maintenanceLine_increaseLength_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_increaseLength_endorsementLine_endorsementLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_increaseLength_endorsementLine_endorsementLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_increaseLength_endorsementLine_increaseLength_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_increaseLength_endorsementLine_increaseLength_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_increaseLength_makeProfessional_makeProfessional_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_increaseLength_makeProfessional_makeProfessional_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_increaseLength_makeProfessional_increaseLength_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_increaseLength_makeProfessional_increaseLength_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_increaseLength_makeCasual_makeCasual_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_increaseLength_makeCasual_makeCasual_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_increaseLength_makeCasual_increaseLength_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_increaseLength_makeCasual_increaseLength_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_numbersLine_numbersLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_numbersLine_numbersLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_numbersLine_companyName_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_numbersLine_companyName_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_maintenanceLine_maintenanceLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_maintenanceLine_maintenanceLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_maintenanceLine_companyName_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_maintenanceLine_companyName_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_endorsementLine_endorsementLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_endorsementLine_endorsementLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_endorsementLine_companyName_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_endorsementLine_companyName_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_makeProfessional_makeProfessional_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_makeProfessional_makeProfessional_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_makeProfessional_companyName_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_makeProfessional_companyName_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_makeCasual_makeCasual_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_makeCasual_makeCasual_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_makeCasual_companyName_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_makeCasual_companyName_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_increaseLength_increaseLength_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_increaseLength_increaseLength_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_companyName_increaseLength_companyName_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_companyName_increaseLength_companyName_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_numbersLine_numbersLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_numbersLine_numbersLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_numbersLine_addExample_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_numbersLine_addExample_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_maintenanceLine_maintenanceLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_maintenanceLine_maintenanceLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_maintenanceLine_addExample_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_maintenanceLine_addExample_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_endorsementLine_endorsementLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_endorsementLine_endorsementLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_endorsementLine_addExample_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_endorsementLine_addExample_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_makeProfessional_makeProfessional_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_makeProfessional_makeProfessional_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_makeProfessional_addExample_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_makeProfessional_addExample_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_makeCasual_makeCasual_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_makeCasual_makeCasual_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_makeCasual_addExample_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_makeCasual_addExample_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_increaseLength_increaseLength_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_increaseLength_increaseLength_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_increaseLength_addExample_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_increaseLength_addExample_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_companyName_companyName_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_companyName_companyName_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_addExample_companyName_addExample_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_addExample_companyName_addExample_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_numbersLine_numbersLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_numbersLine_numbersLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_numbersLine_original_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_numbersLine_original_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_maintenanceLine_maintenanceLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_maintenanceLine_maintenanceLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_maintenanceLine_original_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_maintenanceLine_original_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_endorsementLine_endorsementLine_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_endorsementLine_endorsementLine_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_endorsementLine_original_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_endorsementLine_original_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_makeProfessional_makeProfessional_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_makeProfessional_makeProfessional_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_makeProfessional_original_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_makeProfessional_original_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_makeCasual_makeCasual_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_makeCasual_makeCasual_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_makeCasual_original_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_makeCasual_original_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_increaseLength_increaseLength_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_increaseLength_increaseLength_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_increaseLength_original_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_increaseLength_original_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_companyName_companyName_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_companyName_companyName_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_companyName_original_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_companyName_original_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_addExample_addExample_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_addExample_addExample_first.json"
TEST_FILE_MAPPING["combined_simple_live_simple_dup2_original_addExample_original_first"] = f"{VERSION_PREFIX}_combined_simple_live_simple_dup2_original_addExample_original_first.json"
TEST_FILE_MAPPING["live_simple_dup1_originalV2_duplicate_first"] = f"{VERSION_PREFIX}_live_simple_dup1_originalV2_duplicate_first.json"
TEST_FILE_MAPPING["live_simple_dup1_originalV2_original_first"] = f"{VERSION_PREFIX}_live_simple_dup1_originalV2_original_first.json"
TEST_FILE_MAPPING["live_simple_dup1_fusionV2_743892_duplicate_first"] = f"{VERSION_PREFIX}_live_simple_dup1_fusionV2_743892_duplicate_first.json"
TEST_FILE_MAPPING["live_simple_dup1_fusionV2_743892_original_first"] = f"{VERSION_PREFIX}_live_simple_dup1_fusionV2_743892_original_first.json"
TEST_FILE_MAPPING["live_simple_dup1_fusionV2_74389_duplicate_first"] = f"{VERSION_PREFIX}_live_simple_dup1_fusionV2_74389_duplicate_first.json"
TEST_FILE_MAPPING["live_simple_dup1_fusionV2_74389_original_first"] = f"{VERSION_PREFIX}_live_simple_dup1_fusionV2_74389_original_first.json"
TEST_FILE_MAPPING["live_simple_dup1_addEmojis_duplicate_first"] = f"{VERSION_PREFIX}_live_simple_dup1_addEmojis_duplicate_first.json"
TEST_FILE_MAPPING["live_simple_dup1_makeCasual_duplicate_first"] = f"{VERSION_PREFIX}_live_simple_dup1_makeCasual_duplicate_first.json"
TEST_FILE_MAPPING["live_simple_dup1_makeProfessional_duplicate_first"] = f"{VERSION_PREFIX}_live_simple_dup1_makeProfessional_duplicate_first.json"
TEST_FILE_MAPPING["live_simple_dup1_shortenLength_duplicate_first"] = f"{VERSION_PREFIX}_live_simple_dup1_shortenLength_duplicate_first.json"
TEST_FILE_MAPPING["live_simple_dup1_increaseLength_duplicate_first"] = f"{VERSION_PREFIX}_live_simple_dup1_increaseLength_duplicate_first.json"
TEST_FILE_MAPPING["live_simple_dup1_addEmojis_original_first"] = f"{VERSION_PREFIX}_live_simple_dup1_addEmojis_original_first.json"
TEST_FILE_MAPPING["live_simple_dup1_makeCasual_original_first"] = f"{VERSION_PREFIX}_live_simple_dup1_makeCasual_original_first.json"
TEST_FILE_MAPPING["live_simple_dup1_makeProfessional_original_first"] = f"{VERSION_PREFIX}_live_simple_dup1_makeProfessional_original_first.json"
TEST_FILE_MAPPING["live_simple_dup1_shortenLength_original_first"] = f"{VERSION_PREFIX}_live_simple_dup1_shortenLength_original_first.json"
TEST_FILE_MAPPING["live_simple_dup1_increaseLength_original_first"] = f"{VERSION_PREFIX}_live_simple_dup1_increaseLength_original_first.json"

TEST_FILE_MAPPING["live_simple_dup1_addExample_duplicate_first"] = f"{VERSION_PREFIX}_live_simple_dup1_addExample_duplicate_first.json"
TEST_FILE_MAPPING["live_simple_dup1_addExample_original_first"] = f"{VERSION_PREFIX}_live_simple_dup1_addExample_original_first.json"
TEST_FILE_MAPPING["simple_dup1_addExample_original_first"] = f"{VERSION_PREFIX}_simple_dup1_addExample_original_first.json"
TEST_FILE_MAPPING["simple_dup1_addExample_duplicate_first"] = f"{VERSION_PREFIX}_simple_dup1_addExample_duplicate_first.json"
TEST_FILE_MAPPING["simple_dup1_makeMultiLingual_duplicate_first"] = f"{VERSION_PREFIX}_simple_dup1_makeMultiLingual_duplicate_first.json"
TEST_FILE_MAPPING["simple_dup1_makeMultiLingual_original_first"] = f"{VERSION_PREFIX}_simple_dup1_makeMultiLingual_original_first.json"
TEST_FILE_MAPPING["live_simple_dup1_makeMultiLingual_duplicate_first"] = f"{VERSION_PREFIX}_live_simple_dup1_makeMultiLingual_duplicate_first.json"
TEST_FILE_MAPPING["live_simple_dup1_makeMultiLingual_original_first"] = f"{VERSION_PREFIX}_live_simple_dup1_makeMultiLingual_original_first.json"
TEST_FILE_MAPPING["live_simple_dup1_naive_duplicate_first"] = f"{VERSION_PREFIX}_live_simple_dup1_naive_duplicate_first.json"

TEST_COLLECTION_MAPPING = {
    "all": [
        "simple",
        "irrelevance",
        "parallel",
        "multiple",
        "parallel_multiple",
        "java",
        "javascript",
        "live_simple",
        "live_multiple",
        "live_parallel",
        "live_parallel_multiple",
        "live_irrelevance",
        "live_relevance",
        "multi_turn_base",
        "multi_turn_miss_func",
        "multi_turn_miss_param",
        "multi_turn_long_context",
    ],
    "multi_turn": [
        "multi_turn_base",
        "multi_turn_miss_func",
        "multi_turn_miss_param",
        "multi_turn_long_context",
    ],
    "single_turn": [
        "simple",
        "irrelevance",
        "parallel",
        "multiple",
        "parallel_multiple",
        "java",
        "javascript",
        "live_simple",
        "live_multiple",
        "live_parallel",
        "live_parallel_multiple",
        "live_irrelevance",
        "live_relevance",
    ],
    "live": [
        "live_simple",
        "live_multiple",
        "live_parallel",
        "live_parallel_multiple",
        "live_irrelevance",
        "live_relevance",
    ],
    "non_live": [
        "simple",
        "irrelevance",
        "parallel",
        "multiple",
        "parallel_multiple",
        "java",
        "javascript",
    ],
    "ast": [
        "simple",
        "irrelevance",
        "parallel",
        "multiple",
        "parallel_multiple",
        "java",
        "javascript",
        "live_simple",
        "live_multiple",
        "live_parallel",
        "live_parallel_multiple",
        "live_irrelevance",
        "live_relevance",
    ],
    "non_python": [
        "java",
        "javascript",
    ],
    "python": [
        "simple",
        "irrelevance",
        "parallel",
        "multiple",
        "parallel_multiple",
        "live_simple",
        "live_multiple",
        "live_parallel",
        "live_parallel_multiple",
        "live_irrelevance",
        "live_relevance",
    ],
}

MULTI_TURN_FUNC_DOC_FILE_MAPPING = {
    "GorillaFileSystem": "gorilla_file_system.json",
    "MathAPI": "math_api.json",
    "MessageAPI": "message_api.json",
    "TwitterAPI": "posting_api.json",
    "TicketAPI": "ticket_api.json",
    "TradingBot": "trading_bot.json",
    "TravelAPI": "travel_booking.json",
    "VehicleControlAPI": "vehicle_control.json",
}
