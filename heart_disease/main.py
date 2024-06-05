"""
Main module for the projet
"""
import argparse
import os
from src.plotting import *
from src.load import *
from src.process import *
from src.clean import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Heart Disease project')
    parser.add_argument('--process', action='store_true', help='Process the dataset')
    parser.add_argument("--plot", action='store_true', help='Generate plots')
    parser.add_argument('--clean', action='store_true', help='Cleans duplicates and NaNs')
    parser.add_argument('--all', action='store_true', help='Run all blocks')
    
    args = parser.parse_args()
    
    if args.process:
        df = process_all('data/raw_data/processed.cleveland.data')
        print(df.head())
        
    if args.plot:
        plot_all(path='data/processed_data/processed_data')
        
    if args.clean:
        clean_all
        
    # if args.all:
        # Runs all blocks
        