import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import polars as pl

import scripts.extract_stats_projects as extract_stats_projects
import scripts.extract_stats_files as extract_stats_files
# import scripts.extract_stats_functions as extract_stats_functions

# print(globals())

if __name__ == "__main__":
    extract_stats_projects
    extract_stats_files
    # extract_stats_functions

# def globals():
#     foo = 1
#     bar = "bar"
#     print("Hello world!")
#     print(locals())

# # globals()
# # print(locals())
# # print(__builtins__)
# # print(globals())

# df_projects = pd.read_csv("fp_dataset/data/fp_projects.csv")
# df_files = pd.read_csv("fp_dataset/data/fp_projects.csv")

# foo = df_projects[df_projects["path"] != "error"]

# print(foo.info())

# # df_projects = pd.read_csv("result/gl_projects.csv")
# # df_files = pd.read_csv("result/gl_files.csv")

# # # print(df_projects.info())
# # # print(df_files.head())

# # # to remove projects with error, do something like this:
# # foo = df_projects[["id", "path"]]
# # rows = foo[foo["path"] != "error"].index
# # foo.drop(rows, inplace=True)
# # # TODO: write script to make sure that the ids of projects with error do not show up in files. extract column, convert
# # # to set maybe and then compare for both cases

# # id_project = foo["id"]
# # id_project = set(id_project)

# # id_file = df_files["id"]
# # id_file = set(id_file)

# # ids_in_both = id_project.isdisjoint(id_file)
# # if ids_in_both:
# #     print("The ID:s do not appear in both files, we are good! :D")
# # else:
# #     print("ERROR: The ID:s appear in both files, we are not good :(")

# # most_keywords = df_projects["keywords/globals.json"]
# # print(most_keywords.max())