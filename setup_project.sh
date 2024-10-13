#!/bin/bash

mkdir -p data/raw
mkdir -p data/processed/dataset
mkdir -p data/processed/labels
mkdir -p data/processed/other
mkdir -p data/external

mkdir -p notebooks

mkdir -p src/data_processing/classes
mkdir -p src/analysis
mkdir -p src/visualization
mkdir -p src/common
mkdir -p src/utils

mkdir -p tests

mkdir -p results/figures
mkdir -p results/tables

mkdir -p scripts

mkdir -p configs

mkdir -p docs

# 空のファイルを作成
# data/raw 内の *.dat と *.zip はテンプレートとして作成しません

# src/data_processing
touch src/data_processing/__init__.py
touch src/data_processing/pr7_25.py
touch src/data_processing/makeimage.py
touch src/data_processing/makehysteresis.py

# src/data_processing/classes
touch src/data_processing/classes/__init__.py
touch src/data_processing/classes/CalcMPEXP.py
touch src/data_processing/classes/GetFiles.py

# src/analysis
touch src/analysis/__init__.py
touch src/analysis/svm_result_analysis_and_plot.py
touch src/analysis/pr8.py
touch src/analysis/pr9_5.py
touch src/analysis/pr9_5original.py
touch src/analysis/change_detection.py
touch src/analysis/F1score.py
touch src/analysis/ES_SVM.py

# src/visualization
touch src/visualization/__init__.py
touch src/visualization/makeimage.py
touch src/visualization/makehysteresis.py
touch src/visualization/make_isat_graph.py

# src/common
touch src/common/__init__.py
touch src/common/names_dict.py

# src/utils
touch src/utils/__init__.py

# tests
touch tests/__init__.py
touch tests/test_example.py  # test_*.py の例としてtest_example.pyを作成

# scripts
touch scripts/run_data_processing.sh
touch scripts/run_analysis.sh

# configs
touch configs/config.json

# docs
touch docs/README.md

# ルートディレクトリのファイル
touch requirements.txt

echo "プロジェクトのディレクトリ構成とファイルの作成が完了しました。"