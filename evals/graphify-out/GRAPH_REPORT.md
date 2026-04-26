# Graph Report - .  (2026-04-26)

## Corpus Check
- 40 files · ~69,690 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 362 nodes · 555 edges · 31 communities detected
- Extraction: 74% EXTRACTED · 26% INFERRED · 0% AMBIGUOUS · INFERRED: 143 edges (avg confidence: 0.6)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_QA Benchmark Base Framework|QA Benchmark Base Framework]]
- [[_COMMUNITY_Benchmark Summary Statistics|Benchmark Summary Statistics]]
- [[_COMMUNITY_Cross-System Score Comparison|Cross-System Score Comparison]]
- [[_COMMUNITY_Results Analysis Pipeline|Results Analysis Pipeline]]
- [[_COMMUNITY_Modal QA Evaluation|Modal QA Evaluation]]
- [[_COMMUNITY_Cross-Benchmark Analysis|Cross-Benchmark Analysis]]
- [[_COMMUNITY_Cognee Benchmark Runner|Cognee Benchmark Runner]]
- [[_COMMUNITY_Benchmark RAG Utilities|Benchmark RAG Utilities]]
- [[_COMMUNITY_GraphRAG Falkor Integration|GraphRAG Falkor Integration]]
- [[_COMMUNITY_Graphiti QA Integration|Graphiti QA Integration]]
- [[_COMMUNITY_Results Retrieval Helpers|Results Retrieval Helpers]]
- [[_COMMUNITY_Mem0 Benchmark Runner|Mem0 Benchmark Runner]]
- [[_COMMUNITY_Mem0 QA Integration|Mem0 QA Integration]]
- [[_COMMUNITY_Metrics Conversion Utilities|Metrics Conversion Utilities]]
- [[_COMMUNITY_Metrics Plotting|Metrics Plotting]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]

## God Nodes (most connected - your core abstractions)
1. `QABenchmarkRAG` - 43 edges
2. `QABenchmarkConfig` - 36 edges
3. `QABenchmarkGraphiti` - 16 edges
4. `QABenchmarkCognee` - 14 edges
5. `QA Evaluation Benchmark Suite` - 14 edges
6. `QABenchmarkLightRAG` - 13 edges
7. `QABenchmarkMem0` - 13 edges
8. `GraphitiConfig` - 12 edges
9. `CogneeConfig` - 10 edges
10. `LightRAGConfig` - 10 edges

## Surprising Connections (you probably didn't know these)
- `Memo Scores (Metrics: HLC=0.62, DE-C=0.42, F1=0.10, EM=0)` --rationale_for--> `Mem0`  [INFERRED]
  metrics_comparison.png → README.md
- `Comparative QA Benchmarks Suite` --semantically_similar_to--> `QA Evaluation Benchmark Suite`  [INFERRED] [semantically similar]
  old/comparative_eval/README.md → README.md
- `HotpotQA Dataset (50-item subset)` --semantically_similar_to--> `HotpotQA Dataset (24-item subset)`  [INFERRED] [semantically similar]
  old/comparative_eval/README.md → README.md
- `Mem0 Scores (Comprehensive: HLC=0.72, DE-C=0.54, F1=0.12)` --rationale_for--> `Mem0`  [EXTRACTED]
  comprehensive_metrics_comparison.png → README.md
- `Graphiti Previous Scores (Comprehensive: HLC=0.88, DE-C=0.74, F1=0.69, EM=0.46)` --rationale_for--> `Graphiti`  [EXTRACTED]
  comprehensive_metrics_comparison.png → README.md

## Hyperedges (group relationships)
- **hyperedge_evaluated_systems** — readme_cognee, readme_mem0, readme_graphiti, readme_lightrag [EXTRACTED 1.00]
- **hyperedge_cognee_configs** — readme_graph_completion, readme_graph_completion_cot, readme_graph_completion_context_extension [EXTRACTED 1.00]
- **hyperedge_evaluation_metrics** — readme_em_metric, readme_f1_metric, readme_deepeval_correctness, readme_humanlike_correctness [EXTRACTED 1.00]

## Communities

### Community 0 - "QA Benchmark Base Framework"
Cohesion: 0.07
Nodes (32): QABenchmarkConfig, QABenchmarkRAG, Base configuration for QA benchmark pipelines., Abstract base class for QA benchmarking with different RAG systems., Initialize the benchmark with corpus and QA data., QABenchmarkCognee, Insert document into Cognee via corpus builder., Load corpus data into Cognee using eval framework's corpus builder. (+24 more)

### Community 1 - "Benchmark Summary Statistics"
Cohesion: 0.07
Nodes (44): bootstrap_confidence_interval(), create_metric_entry(), create_output_directory(), extract_confidence_intervals(), format_benchmark_entry(), format_json_output(), get_benchmark_analysis_path(), handle_processing_errors() (+36 more)

### Community 2 - "Cross-System Score Comparison"
Cohesion: 0.09
Nodes (37): Cognee Scores (Comprehensive: HLC=0.93, DE-C=0.85, F1=0.84, EM=0.69), Graphiti Previous Scores (Comprehensive: HLC=0.88, DE-C=0.74, F1=0.69, EM=0.46), LightRAG Scores (Comprehensive: HLC=0.95, DE-C=0.67, F1=0.09), Mem0 Scores (Comprehensive: HLC=0.72, DE-C=0.54, F1=0.12), Comprehensive Metrics Comparison Chart, Cognee Scores (Metrics: HLC=0.84, DE-C=0.57, F1=0.20, EM=0.04), AI Memory Benchmark Results Chart, Graphiti Scores (Metrics: HLC=0.73, DE-C=0.59, F1=0.61, EM=0.44) (+29 more)

### Community 3 - "Results Analysis Pipeline"
Cohesion: 0.09
Nodes (26): create_aggregate_metrics_df(), cumulative_all_metrics_analysis(), cumulative_single_metric_analysis(), Create cumulative analysis for a single metric, ordered by best results first., Create cumulative analysis for all metrics, ordered by best results first., Create aggregate dataframe with mean and std for each metric across files., analyze_single_benchmark_folder(), create_all_dataframes() (+18 more)

### Community 4 - "Modal QA Evaluation"
Cohesion: 0.09
Nodes (23): calculate_qa_metrics(), get_answers_files(), main(), Entry point that triggers evaluation for a specific benchmark folder., Get list of JSON files from the answers folder in a benchmark directory., Calculate QA metrics for a JSON file using cognee evaluation framework., _create_benchmark_folder(), launch_neo4j_and_run_benchmark() (+15 more)

### Community 5 - "Cross-Benchmark Analysis"
Cohesion: 0.12
Nodes (22): check_analysis_files_exist(), check_evaluated_folder_exists(), create_analysis_folder(), create_cross_benchmark_summary(), download_modal_volume(), get_benchmark_folders(), main(), print_progress_update() (+14 more)

### Community 6 - "Cognee Benchmark Runner"
Cohesion: 0.14
Nodes (18): _create_benchmark_folder(), main(), Create benchmark folder structure and return the answers folder path., Run the Cognee QA benchmark on Modal., Trigger Cognee QA benchmark runs on Modal., run_cognee_benchmark(), _create_benchmark_folder(), main() (+10 more)

### Community 7 - "Benchmark RAG Utilities"
Cohesion: 0.12
Nodes (9): ABC, cleanup_rag(), initialize_rag(), insert_document(), query_rag(), Save results to JSON file., Run the complete benchmark pipeline., Load corpus data into the RAG system. (+1 more)

### Community 8 - "GraphRAG Falkor Integration"
Cohesion: 0.22
Nodes (12): answer_questions(), create_knowledge_graph(), create_ontology(), _get_sources_from_corpus_json(), HotpotQAConfig, main(), Query knowledge graph with questions from qa pairs file., Returns STRING sources from corpus JSON file. (+4 more)

### Community 9 - "Graphiti QA Integration"
Cohesion: 0.21
Nodes (12): answer_questions(), HotpotQAGraphitiConfig, load_corpus_to_graphiti(), main(), main_async(), Main async function for HotpotQA graphiti pipeline., Wrapper for async main function., Configuration for HotpotQA graphiti pipeline. (+4 more)

### Community 10 - "Results Retrieval Helpers"
Cohesion: 0.24
Nodes (10): Validate that all files have same length and all dictionaries contain same keys., Validate that a single file's data has correct structure and keys., Validate that metrics have correct structure and expected keys., Read all JSON files from the specified directory path., read_results(), validate_file_results(), validate_folder_results(), validate_metrics() (+2 more)

### Community 11 - "Mem0 Benchmark Runner"
Cohesion: 0.27
Nodes (8): _create_benchmark_folder(), main(), Create benchmark folder structure and return the answers folder path., Run the Mem0 QA benchmark on Modal., Trigger Mem0 QA benchmark runs on Modal., run_mem0_benchmark(), Mem0Config, Configuration for Mem0 QA benchmark.

### Community 12 - "Mem0 QA Integration"
Cohesion: 0.28
Nodes (8): answer_questions(), HotpotQAMemoryConfig, load_corpus_to_memory(), main(), Main function for HotpotQA memory pipeline., Configuration for HotpotQA memory pipeline., Loads corpus data into memory., Answer questions using memory retrieval.

### Community 13 - "Metrics Conversion Utilities"
Cohesion: 0.39
Nodes (6): convert_metrics_file(), convert_to_dataframe(), process_multiple_files(), Convert results list to DataFrame with expanded error columns., Process multiple JSON files and save concatenated results., Convert a single metrics JSON file to the desired format.

### Community 14 - "Metrics Plotting"
Cohesion: 0.43
Nodes (6): _extract_matrix(), _load(), main(), _plot_grouped_bar(), Read JSON file that may be either a list or dict{'data': …}., Return:         systems         -> list[str]         means           -> dict[m

### Community 15 - "Community 15"
Cohesion: 0.4
Nodes (4): main(), modal_evaluate_answers(), Main entry point that evaluates multiple JSON answer files in parallel., Evaluates answers from JSON content and returns metrics results.

### Community 16 - "Community 16"
Cohesion: 0.5
Nodes (4): load_benchmark_data(), Visualize benchmark results with error bars., Load benchmark data from JSON file., visualize_benchmarks()

### Community 17 - "Community 17"
Cohesion: 0.5
Nodes (2): calculate_aggregates_for_files(), Calculate aggregate metrics for a list of JSON files.

### Community 18 - "Community 18"
Cohesion: 0.67
Nodes (3): matplotlib, numpy, seaborn

### Community 19 - "Community 19"
Cohesion: 1.0
Nodes (0): 

### Community 20 - "Community 20"
Cohesion: 1.0
Nodes (0): 

### Community 21 - "Community 21"
Cohesion: 1.0
Nodes (0): 

### Community 22 - "Community 22"
Cohesion: 1.0
Nodes (1): Create benchmark instance by loading data from JSON files.

### Community 23 - "Community 23"
Cohesion: 1.0
Nodes (1): Initialize the RAG system. Returns the RAG client.

### Community 24 - "Community 24"
Cohesion: 1.0
Nodes (1): Clean up RAG system resources.

### Community 25 - "Community 25"
Cohesion: 1.0
Nodes (1): Insert a single document into the RAG system.

### Community 26 - "Community 26"
Cohesion: 1.0
Nodes (1): Query the RAG system and return the answer.

### Community 27 - "Community 27"
Cohesion: 1.0
Nodes (1): Return the name of the RAG system for logging.

### Community 28 - "Community 28"
Cohesion: 1.0
Nodes (0): 

### Community 29 - "Community 29"
Cohesion: 1.0
Nodes (1): scipy

### Community 30 - "Community 30"
Cohesion: 1.0
Nodes (1): pathlib

## Knowledge Gaps
- **106 isolated node(s):** `Read JSON file that may be either a list or dict{'data': …}.`, `Return:         systems         -> list[str]         means           -> dict[m`, `Calculate aggregate metrics for a list of JSON files.`, `Convert a single metrics JSON file to the desired format.`, `Convert results list to DataFrame with expanded error columns.` (+101 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 19`** (2 nodes): `main()`, `hotpotqa_instances.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (1 nodes): `modal_image.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (1 nodes): `Create benchmark instance by loading data from JSON files.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (1 nodes): `Initialize the RAG system. Returns the RAG client.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (1 nodes): `Clean up RAG system resources.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (1 nodes): `Insert a single document into the RAG system.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (1 nodes): `Query the RAG system and return the answer.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (1 nodes): `Return the name of the RAG system for logging.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (1 nodes): `scipy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (1 nodes): `pathlib`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `QABenchmarkRAG` connect `QA Benchmark Base Framework` to `Mem0 Benchmark Runner`, `Modal QA Evaluation`, `Cognee Benchmark Runner`, `Benchmark RAG Utilities`?**
  _High betweenness centrality (0.161) - this node is a cross-community bridge._
- **Why does `download_modal_volume()` connect `Cross-Benchmark Analysis` to `Modal QA Evaluation`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Why does `process_single_benchmark()` connect `Cross-Benchmark Analysis` to `Results Analysis Pipeline`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **Are the 34 inferred relationships involving `QABenchmarkRAG` (e.g. with `CogneeConfig` and `QABenchmarkCognee`) actually correct?**
  _`QABenchmarkRAG` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Are the 34 inferred relationships involving `QABenchmarkConfig` (e.g. with `CogneeConfig` and `QABenchmarkCognee`) actually correct?**
  _`QABenchmarkConfig` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `QABenchmarkGraphiti` (e.g. with `Create benchmark folder structure and return the answers folder path.` and `Run the Graphiti QA benchmark on Modal.`) actually correct?**
  _`QABenchmarkGraphiti` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `QABenchmarkCognee` (e.g. with `Create benchmark folder structure and return the answers folder path.` and `Run the Cognee QA benchmark on Modal.`) actually correct?**
  _`QABenchmarkCognee` has 5 INFERRED edges - model-reasoned connections that need verification._