import polars as pl
import numpy as np
import seaborn as sns
import matplotlib as plt
import keyword_reader
from StatisticsExtractor import StatisticsExtractor

PATH_KEYWORDS = "keywords/"

df_projects = pl.read_csv("result/tot_projects.csv")
file_to_kw = keyword_reader.read_json()

extractor = StatisticsExtractor(file_to_kw)

# TODO: What do do when keyword shows up in a string: for instance __builtins__ in: 
#/home/linus-brewitz/Code/thesis/scyros/tot_projects/0/322764981-73991d3b6174a29261cd6b86bc5f1c16a8b13021/star-eyes-student_edit-73991d3/成绩管理系统1/schema/pgsql/pgAdmin 4/venv/Lib/pydoc_data/topics.py

#TODO: min() is probably not very useful since it will always be 0

files_kw_percentage = extractor.kw_ratio_project(df_projects, "files_with_kw", "files")
loc_kw_percentage = extractor.kw_ratio_project(df_projects, "loc_with_kw", "loc")
words_kw_percentage = extractor.kw_ratio_project(df_projects, "words_with_kw", "words")
print(f"The percentage of files having at least one keyword: {files_kw_percentage}%")
print(f"The percentage of LOC having at least one keywords: {loc_kw_percentage}%")
print(f"The percentage of words having at least one keyword: {words_kw_percentage}%")
print()
print()

file_names = file_to_kw.keys()

for kw in file_names:
    files_kw_percentage = extractor.kw_ratio_project(df_projects, "files_with_" + PATH_KEYWORDS + kw, "files")
    loc_kw_percentage = extractor.kw_ratio_project(df_projects, "loc_of_files_with_" + PATH_KEYWORDS + kw, "loc")
    words_kw_percentage = extractor.kw_ratio_project(df_projects, "words_of_files_with_" + PATH_KEYWORDS + kw, "words")
    print(f"The percentage of files having {file_to_kw.get(kw)}: {files_kw_percentage}%")
    print(f"The percentage of LOC having {file_to_kw.get(kw)}: {loc_kw_percentage}%")
    print(f"The percentage of words having {file_to_kw.get(kw)}: {words_kw_percentage}%")

    kw_in_project = extractor.kw_in_project(df_projects, PATH_KEYWORDS + kw)
    print(f"The total number of occurrences in all projects for {file_to_kw.get(kw)}: {kw_in_project}")

    max_kw_project = extractor.max_keyword_project(df_projects, PATH_KEYWORDS + kw)
    print(f"The maximum number of occurrences for {file_to_kw.get(kw)} is: {max_kw_project}")

    min_kw_project = extractor.min_keyword_project(df_projects, PATH_KEYWORDS + kw)
    print(f"The minimum number of occurrences for {file_to_kw.get(kw)} is: {min_kw_project}")

    mean_kw_project = extractor.calculate_mean_attr(df_projects, PATH_KEYWORDS + kw)
    print(f"The mean of keywords is for {file_to_kw.get(kw)}: {mean_kw_project}")

    median_kw_project = extractor.calculate_median_attr(df_projects, PATH_KEYWORDS + kw)
    print(f"The median of keywords is for {file_to_kw.get(kw)}: {median_kw_project}")

    var_kw_project = extractor.calculate_variance_attr(df_projects, PATH_KEYWORDS + kw)
    print(f"The variance of keywords for {file_to_kw.get(kw)} is : {var_kw_project}")

    sigma_kw_project = extractor.calculate_sigma_attr(df_projects, PATH_KEYWORDS + kw)
    print(f"The standard deviation of keywords for {file_to_kw.get(kw)} is : {sigma_kw_project}")

    quantiles_kw_project = extractor.calculate_quant_attr(df_projects, PATH_KEYWORDS + kw)
    print(f"The quantiles of keywords for {file_to_kw.get(kw)} is : {quantiles_kw_project}")
    print()
    print()
