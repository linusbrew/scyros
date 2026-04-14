import polars as pl
import numpy as np
import seaborn as sns
import matplotlib as plt
from StatisticsExtractor import StatisticsExtractor

PATH_KEYWORDS = "keywords/"

df_projects = pl.read_csv("result/tot_projects.csv")

extractor = StatisticsExtractor()

# TODO: What do do when keyword shows up in a string: for instance __builtins__ in: 
#/home/linus-brewitz/Code/thesis/scyros/tot_projects/0/322764981-73991d3b6174a29261cd6b86bc5f1c16a8b13021/star-eyes-student_edit-73991d3/成绩管理系统1/schema/pgsql/pgAdmin 4/venv/Lib/pydoc_data/topics.py

#TODO: min() is probably not very useful since it will always be 0

with open("stats_projects2.txt", "w") as f:
    files_kw_percentage = extractor.kw_ratio_project(df_projects, "files_with_kw", "files")
    loc_kw_percentage = extractor.kw_ratio_project(df_projects, "loc_with_kw", "loc")
    words_kw_percentage = extractor.kw_ratio_project(df_projects, "words_with_kw", "words")
    f.write(f"The percentage of files having at least one keyword: {files_kw_percentage}%\n")
    f.write(f"The percentage of LOC having at least one keyword: {loc_kw_percentage}%\n")
    f.write(f"The percentage of words having at least one keyword: {words_kw_percentage}%\n")
    f.write("\n")
    f.write("\n")

    file_names = extractor.file_to_kw.keys()

    for kw in file_names:
        path = PATH_KEYWORDS + kw
        files_kw_percentage = extractor.kw_ratio_project(df_projects, "files_with_" + path, "files")
        loc_kw_percentage = extractor.kw_ratio_project(df_projects, "loc_of_files_with_" + path, "loc")
        words_kw_percentage = extractor.kw_ratio_project(df_projects, "words_of_files_with_" + path, "words")
        f.write(f"The percentage of files having {extractor.file_to_kw.get(kw)}: {files_kw_percentage}%\n")
        f.write(f"The percentage of LOC having {extractor.file_to_kw.get(kw)}: {loc_kw_percentage}%\n")
        f.write(f"The percentage of words having {extractor.file_to_kw.get(kw)}: {words_kw_percentage}%\n")

        kw_in_project = extractor.kw_in_project(df_projects, path)
        f.write(f"The total number of occurrences in all projects for {extractor.file_to_kw.get(kw)}: {kw_in_project}\n")

        max_kw_project = extractor.max_keyword_project(df_projects, path)
        f.write(f"The maximum number of occurrences for {extractor.file_to_kw.get(kw)} is: {max_kw_project}\n")

        min_kw_project = extractor.min_keyword_project(df_projects, path)
        f.write(f"The minimum number of occurrences for {extractor.file_to_kw.get(kw)} is: {min_kw_project}\n")

        mean_kw_project = extractor.calculate_mean_attr(df_projects, path)
        f.write(f"The mean of keywords is for {extractor.file_to_kw.get(kw)}: {mean_kw_project}\n")

        median_kw_project = extractor.calculate_median_attr(df_projects, path)
        f.write(f"The median of keywords is for {extractor.file_to_kw.get(kw)}: {median_kw_project}\n")

        var_kw_project = extractor.calculate_variance_attr(df_projects, path)
        f.write(f"The variance of keywords for {extractor.file_to_kw.get(kw)} is : {var_kw_project}\n")

        sigma_kw_project = extractor.calculate_sigma_attr(df_projects, path)
        f.write(f"The standard deviation of keywords for {extractor.file_to_kw.get(kw)} is : {sigma_kw_project}\n")

        quantiles_kw_project = extractor.calculate_quant_attr(df_projects, path)
        f.write(f"The quantiles of keywords for {extractor.file_to_kw.get(kw)} is : {quantiles_kw_project}\n")
        f.write("\n")
        f.write("\n")
