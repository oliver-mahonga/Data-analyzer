import argparse
import time 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from rich import print 
from rich.console import Console
from rich.align import Align
from rich.table import Table 
from rich import box
from utils.visualizer import generate_all_plots
import random
console = Console ()

def main():
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "bright_white"]
    color= random.choice(colors)
    heading= "Welcome to my excel analyzer project upload a file in the data directory and i will do all the analysis for you"
    for x in heading:
        console.print (x, style=color, highlight=False, end='')
        time.sleep(0.05)

    parser = argparse.ArgumentParser(description="Analyze files in a directory.")
    parser.add_argument('--path', type=str, required=True, help='Path to the directory to analyze')
    parser.add_argument('--summery',default=False, help='Generate a summary of the analysis')
    parser.add_argument('--plot', default=False, help='Generate plots from the analysis')
    args = parser.parse_args()
    

    if os.path.exists(args.path):
        df = pd.read_csv(os.path.join(args.path, 'data.csv'))
        print(Align.center(f"Analyzing files in directory: {args.path}"))
        time.sleep(2)
        print(Align.center(f"Summary requested: {args.summery}"))
        time.sleep(2)
        print(Align.center(f"Plot requested: {args.plot}"))
        time.sleep(2)
        print (Align.center(f"data loaded with {len(df)} rows and {len(df.columns)} columns"))
        time.sleep(3)
        console.print(Align.center("[purple]this is the basic info about your dataset[/purple] "))
        description = {'first 5 rows': df.head, 'summery of the data frame': df.info, 'dimensions of the dataframe': df.shape, 'column names':df.columns, 'statistical summeries of the dataset':df.describe}
        for key, command in description.items():
            table = Table(title=str(key), box=box.SQUARE)
            table.add_column(key, style="cyan")
            if isinstance(command, list):
                for item in command:
                    table.add_row(str(item))
            else:
                table.add_row(str(command))
            time.sleep(3)

            console.print(table)
        if args.plot == "True":
            generate = "generating plots for your data \n"
            for p in generate:
                console.print (p, style=color, highlight=False, end='')
                time.sleep(0.05)
            generate_all_plots(df)
    
            
    else:
        print(f"Error: The path {args.path} does not exist.")
        return
        

    



if __name__ == "__main__":
    main()
      


