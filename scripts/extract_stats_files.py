import polars as pl
import numpy as np
import seaborn as sns
import matplotlib as plt
import os
from scripts.StatisticsExtractor import StatisticsExtractor

PATH_KEYWORDS = "keywords/"

df_files = pl.read_csv("result/tot_dedup_files.csv")

file_name = "stats/stats_files.txt"
os.makedirs(os.path.dirname(file_name), exist_ok=True) 

extractor = StatisticsExtractor()

#TODO: min() is probably not very useful since it will always be 0

file_names = extractor.file_to_kw.keys()
with open(file_name, "w") as f:
    for kw in file_names:
        path = PATH_KEYWORDS + kw
        f.write(f"----------{extractor.file_to_kw.get(kw)}----------\n")
        avg_loc = extractor.avg_length(df_files, "loc", path)
        avg_words = extractor.avg_length(df_files, "words", path)
        f.write(f"On average when {extractor.file_to_kw.get(kw)} appears the file has: {avg_loc} LOC\n")
        f.write(f"On average when {extractor.file_to_kw.get(kw)} appears the file has: {avg_words} words\n")

        kw_in_project = extractor.kw_in_project(df_files, path)
        f.write(f"The total number of occurrences in all projects for {extractor.file_to_kw.get(kw)}: {kw_in_project}\n")

        max_kw_project = extractor.max_keyword_project(df_files, path)
        f.write(f"The maximum number of occurrences for {extractor.file_to_kw.get(kw)} is: {max_kw_project}\n")

        min_kw_project = extractor.min_keyword_project(df_files, path)
        f.write(f"The minimum number of occurrences for {extractor.file_to_kw.get(kw)} is: {min_kw_project}\n")

        mean_kw_project = extractor.calculate_mean_attr(df_files, path)
        f.write(f"The mean of keywords is for {extractor.file_to_kw.get(kw)}: {mean_kw_project}\n")

        median_kw_project = extractor.calculate_median_attr(df_files, path)
        f.write(f"The median of keywords is for {extractor.file_to_kw.get(kw)}: {median_kw_project}\n")

        var_kw_project = extractor.calculate_variance_attr(df_files, path)
        f.write(f"The variance of keywords for {extractor.file_to_kw.get(kw)} is : {var_kw_project}\n")

        sigma_kw_project = extractor.calculate_sigma_attr(df_files, path)
        f.write(f"The standard deviation of keywords for {extractor.file_to_kw.get(kw)} is : {sigma_kw_project}\n")

        quantiles_kw_project = extractor.calculate_quant_attr(df_files, path)
        f.write(f"The quantiles of keywords for {extractor.file_to_kw.get(kw)} is : {quantiles_kw_project}\n")
        f.write("\n")
        f.write("\n")

