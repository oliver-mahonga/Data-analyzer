# Excel & CSV Auto Data Analyzer

This is a Python-based command-line tool that automates the analysis of structured data from CSV or Excel files. It performs automated data cleaning, statistical summarization, outlier detection, and visualization using Pandas, NumPy, Matplotlib, Seaborn, and Rich.

## Features

- Load and analyze CSV files from any specified directory
- Automatic data cleaning summary
- Statistical insights: mean, median, mode, std, etc.
- Outlier detection using both Z-Score and IQR methods
- Auto-generated visualizations: histograms, box plots, heatmaps, and pair plots
- Beautiful command-line output using the Rich library

## Project Structure

excel_analyzer/
├── analyzer.py # Main entry point (CLI)
├── utils/
│ ├── visualizer.py # All Matplotlib/Seaborn plots
│ └── outlier.py # Outlier and stats analyzer
├── data/
│ └── data.csv # Sample dataset (you provide your own)
├── graphs/ # Auto-generated plots saved here
└── README.md


## Installation

1. Clone this repository:

```bash
git clone https://github.com/oliver-mahonga/Data-analyzer
cd excel-analyzer

    Create a virtual environment (optional):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

    Install required packages:

pip install -r requirements.txt

Or install manually:

pip install pandas numpy matplotlib seaborn random rich

How to Use

Place your data.csv file inside the data/ directory, then run:


## you can run this command immediatly to test


python analyzer.py --path data --summery True --plot True

    --path: Folder containing the data.csv file

    --summery: Set to True to view a summary of the dataset

    --plot: Set to True to generate plots from the analysis

The CLI will:

    Load your dataset

    Display structural and statistical summaries

    Detect outliers

    Generate visualizations saved in graphs/

Output Includes

    CLI-based summary (table of info)

    Full statistical breakdown of numeric columns

    Z-Score and IQR-based outlier detection counts

    Plots:

        Histograms

        Boxplots

        Correlation heatmap

        Pairplot (if few columns)

Dependencies

    Python 3.8+

    pandas

    numpy

    matplotlib

    seaborn

    scipy

    rich
