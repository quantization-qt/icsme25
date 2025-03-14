Replication Package: Investigating the Impact of Quantization on Large Code Models

This repository contains the replication package for our study on the impact of quantization on Large Code Models (LCMs), focusing on code quality and static properties beyond functional correctness. Our investigation examines whether reducing model precision via Activation-Aware Weight Quantization (AWQ) affects key software engineering attributes such as maintainability, security, and structural complexity.
We evaluated quantized and full-precision LCMs using state-of-the-art static analysis tools, including SonarCloud, PMD, Pylint, and Flake8, across two programming languages (Python and Java) and two benchmarks (MultipLE and McEval). The replication package includes all relevant scripts, datasets, and documentation necessary to reproduce our experiments and extend our analysis.

Repository Structure

├── data/
│   ├── multiple-java/
│   ├── multiple-python/
│   ├── mceval-java/
│   ├── mceval-python/
│   ├── manual-analysis/
│   ├── conflicts-analysis/
│   └── summary_statistics.csv
│
├── models/
│   ├── codellama-7b-awq/
│   ├── codellama-13b-awq/
│   ├── codellama-34b-awq/
│   ├── deepseekcoder-1.3b-awq/
│   ├── deepseekcoder-6.7b-awq/
│   ├── deepseekcoder-33b-awq/
│   ├── codellama-7b-fp/
│   ├── codellama-13b-fp/
│   ├── codellama-34b-fp/
│   ├── deepseekcoder-1.3b-fp/
│   ├── deepseekcoder-6.7b-fp/
│   ├── deepseekcoder-33b-fp/
│   └── model_configs/
│
├── scripts/
│   ├── run_static_analysis.py
│   ├── process_sonarcloud.py
│   ├── process_pylint_flake8.py
│   ├── compute_conflicts.py
│   ├── extract_quality_metrics.py
│   ├── statistical_tests.py
│   ├── manual_analysis_pipeline.py
│   ├── generate_plots.py
│   ├── utils/
│   └── README.md
│
├── results/
│   ├── summary_results.csv
│   ├── conflicts_matrix.csv
│   ├── quality_metrics_python.csv
│   ├── quality_metrics_java.csv
│   ├── statistical_tests_output.txt
│   ├── plots/
│   ├── raw_predictions/
│   └── README.md
│
├── docs/
│   ├── replication_instructions.pdf
│   ├── methodology.md
│   ├── experiment_setup.md
│   ├── license.txt
│   ├── acknowledgments.md
│   ├── references.bib
│   └── README.md
│
