import polars as pl
import numpy as np
import seaborn as sns
import matplotlib as plt
from scripts.StatisticsExtractor import StatisticsExtractor

PATH_GLOBALS = "keywords/globals.json"

df_projects = pl.read_csv("result/gl_projects.csv")
df_files = pl.read_csv("result/gl_files.csv")
# df_files = pl.read_csv("result/gl_dedup_files.csv")

extractor = StatisticsExtractor()

files_kw_percentage = extractor.kw_ratio_project(df_projects, "files_with_kw", "files")
loc_kw_percentage = extractor.kw_ratio_project(df_projects, "loc_with_kw", "loc")
words_kw_percentage = extractor.kw_ratio_project(df_projects, "words_with_kw", "words")
print(f"The percentage of files having kw: {files_kw_percentage}%")
print(f"The percentage of LOC having kw: {loc_kw_percentage}%")
print(f"The percentage of words having kw: {words_kw_percentage}%")


kw_in_project = extractor.kw_in_project(df_projects, PATH_GLOBALS)
print(f"The total number of occurrences in all projects: {kw_in_project}")

max_kw_project = extractor.max_keyword_project(df_projects, PATH_GLOBALS)
print(f"The maximum number of occurrences is: {max_kw_project}")

min_kw_project = extractor.min_keyword_project(df_projects, PATH_GLOBALS)
print(f"The minimum number of occurrences is: {min_kw_project}")

mean_kw_project = extractor.calculate_mean_attr(df_projects, PATH_GLOBALS)
print(f"The mean of keywords is : {mean_kw_project}")

median_kw_project = extractor.calculate_median_attr(df_projects, PATH_GLOBALS)
print(f"The median of keywords is : {median_kw_project}")

var_kw_project = extractor.calculate_variance_attr(df_projects, PATH_GLOBALS)
print(f"The variance of keywords is : {var_kw_project}")

sigma_kw_project = extractor.calculate_sigma_attr(df_projects, PATH_GLOBALS)
print(f"The standard deviation of keywords is : {sigma_kw_project}")

quantiles_kw_project = extractor.calculate_quant_attr(df_projects, PATH_GLOBALS)
print(f"The quantiles of keywords is : {quantiles_kw_project}")


# print(extr.max_keyword_project(df_projects, PATH_GLOBALS))
###################################################################
## IGONORE THE CODE BENEATH THIS COMMENT ##########################
###################################################################



###### MEAN OF FILES ######
# mean_of_files = df_files.mean()

# avg_loc_files = mean_of_files.select(pl.col("loc"))
# avg_words_files = mean_of_files.select(pl.col("words")) 
# avg_keywords_files = mean_of_files.select(pl.col(PATH_GLOBALS))

# print(f"The mean of LOC in files is: {avg_loc_files.item()}")
# print(f"The mean of words in files is: {avg_words_files.item()}")
# print(f"The mean of keywords in files is: {avg_keywords_files.item()}")

# ###### MEAN OF FILES ######
# median_of_files = df_files.median()

# median_loc_files = median_of_files.select(pl.col("loc"))
# median_words_files = median_of_files.select(pl.col("words")) 
# median_keywords_files = median_of_files.select(pl.col(PATH_GLOBALS))

# print(f"The median of LOC in files is: {median_loc_files.item()}")
# print(f"The median of words in files is: {median_words_files.item()}")
# print(f"The median of keywords in files is: {median_keywords_files.item()}")

# ###### STANDARD DEVIATION OF FILES ######
# sigma_of_files = df_files.std()

# sigma_loc_files = sigma_of_files.select(pl.col("loc"))
# sigma_words_files = sigma_of_files.select(pl.col("words")) 
# sigma_keywords_files = sigma_of_files.select(pl.col(PATH_GLOBALS))

# print(f"The std deviation of LOC in files is: {sigma_loc_files.item()}")
# print(f"The std deviation of words in files is: {sigma_words_files.item()}")
# print(f"The std deviation of keywords in files is: {sigma_keywords_files.item()}")

# ###### VARIANCE OF FILES ######
# var_of_files = df_files.var()

# var_loc_files = var_of_files.select(pl.col("loc"))
# var_words_files = var_of_files.select(pl.col("words")) 
# var_keywords_files = var_of_files.select(pl.col(PATH_GLOBALS))

# print(f"The variance of LOC in files is: {var_loc_files.item()}")
# print(f"The variance of words in files is: {var_words_files.item()}")
# print(f"The variance of keywords in files is: {var_keywords_files.item()}")

# ###### QUANTILES OF FILES ######
# def calculate_all_quantiles(df: pl.DataFrame) -> None:
#     quantiles: list[float] = [0.25, 0.50, 0.75]
#     result = list()
#     for quantile in quantiles:
#         foo = df.quantile(quantile=quantile).item()
#         result.append(foo)
#     for i in result:
#         print(f"The quantile for UPDATE THIS {i}")


# quant_loc_files = df_files.select(pl.col("loc"))
# quant_words_files = df_files.select(pl.col("words")) 
# quant_keywords_files = df_files.select(pl.col(PATH_GLOBALS))

# calculate_all_quantiles(quant_loc_files)
# calculate_all_quantiles(quant_words_files)
# calculate_all_quantiles(quant_keywords_files)

# print("Number of unique occurrences files: ", quant_keywords_files.n_unique())

# #######################################################################
# ############################Cutoff point###############################
# #######################################################################
# print("")
# ###### MEAN OF PROJECTS ######
# mean_of_projects = df_projects.mean()

# avg_loc_projects = mean_of_projects.select(pl.col("loc"))
# avg_words_projects = mean_of_projects.select(pl.col("words")) 
# avg_total_keywords_projects = mean_of_projects.select(pl.col(PATH_GLOBALS)) 

# print(f"The mean of LOC in projects is: {avg_loc_projects.item()}")
# print(f"The mean of words in projects is: {avg_words_projects.item()}")
# print(f"The mean of total keywords in projects is: {avg_total_keywords_projects.item()}")

# ###### MEDIAN OF PROJECTS ######
# median_of_projects = df_projects.median()

# median_loc_projects = median_of_projects.select(pl.col("loc"))
# median_words_projects = median_of_projects.select(pl.col("words")) 
# median_total_keywords_projects = median_of_projects.select(pl.col(PATH_GLOBALS)) 

# print(f"The median of LOC in projects is: {median_loc_projects.item()}")
# print(f"The median of words in projects is: {median_words_projects.item()}")
# print(f"The median of total keywords in projects is: {median_total_keywords_projects.item()}")

# ###### STANDARD DEVIATION OF PROJECTS ######
# sigma_of_projects = df_projects.std()

# sigma_loc_projects = sigma_of_projects.select(pl.col("loc"))
# sigma_words_projects = sigma_of_projects.select(pl.col("words")) 
# sigma_keywords_projects = sigma_of_projects.select(pl.col(PATH_GLOBALS))

# print(f"The std deviation of LOC in projects is: {sigma_loc_projects.item()}")
# print(f"The std deviation of words in projects is: {sigma_words_projects.item()}")
# print(f"The std deviation of keywords in projects is: {sigma_keywords_projects.item()}")

# ###### VARIANCE OF PROJECTS ######
# var_of_projects = df_projects.std()

# var_loc_projects = var_of_projects.select(pl.col("loc"))
# var_words_projects = var_of_projects.select(pl.col("words")) 
# var_keywords_projects = var_of_projects.select(pl.col(PATH_GLOBALS))

# print(f"The variance of LOC in projects is: {var_loc_projects.item()}")
# print(f"The variance of words in projects is: {var_words_projects.item()}")
# print(f"The variance of keywords in projects is: {var_keywords_projects.item()}")

# ###### VARIANCE OF PROJECTS ######
# quant_loc_projects = df_projects.select(pl.col("loc"))
# quant_words_projects = df_projects.select(pl.col("words")) 
# quant_keywords_projects = df_projects.select(pl.col(PATH_GLOBALS))

# calculate_all_quantiles(quant_loc_projects)
# calculate_all_quantiles(quant_words_projects)
# calculate_all_quantiles(quant_keywords_projects)

# print("Number of unique occurrences projects: ", quant_keywords_projects.n_unique())
