# Excel & CSV Auto Data Analyzer

This is a Python-based command-line tool that automates the analysis of structured data from CSV or Excel files. It performs automated data cleaning, statistical summarization, outlier detection, and visualization using Pandas, NumPy, Matplotlib, Seaborn, and Rich.

## Features

- Load Excel or CSV files
- Clean data: remove nulls, fill missing values
- Analyze: get mean, median, mode, std deviation
- Outlier detection using Z-Score and IQR
- Save cleaned file and visual graphs

---

## 🛠Technologies

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- argparse
- openpyxl (for Excel support)

  ## Run the analyzer

- pip install -r requirements.txt
- python3 analyzer.py --path data/sales_data.xlsx --summery True --plot True



