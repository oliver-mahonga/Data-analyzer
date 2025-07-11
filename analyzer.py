import argparse
import pandas as pd
import os
from utils.cleaner import Data

def main():
    parser = argparse.ArgumentParser(description="Analyze files in a directory.")
    parser.add_argument('--path', type=str, required=True, help='Path to the directory to analyze')
    parser.add_argument('--summery',default=False, help='Generate a summary of the analysis')
    parser.add_argument('--plot', default=False, help='Generate plots from the analysis')
    args = parser.parse_args()

    if os.path.exists(args.path):
        df = pd.read_csv(os.path.join(args.path, 'data.csv'))
        Data()

    else:
        print(f"Error: The path {args.path} does not exist.")
        return
        
    print(f"Analyzing files in directory: {args.path}")
    print(f"Summary requested it will be saved int the summery folder: {args.summery}")
    print(f"Plot requested: {args.plot}")
    print (f"data loaded with {len(df)} rows and {len(df.columns)} columns")



if __name__ == "__main__":
    main()
      


