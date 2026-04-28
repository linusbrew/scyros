from StatisticsExtractor import StatisticsExtractor
import polars as pl
import os


PATH_KEYWORDS = "keywords/"

df_files = pl.read_csv("result/imp_dedup_files4.csv")
df_logs = pl.read_csv("result/imp_function_logs.csv")

file_name = "stats/stats_imports.txt"
os.makedirs(os.path.dirname(file_name), exist_ok=True) 

extractor = StatisticsExtractor()

file_names = extractor.file_to_kw.keys()
for kw in file_names:
    path = PATH_KEYWORDS + kw
    kw_in_function = extractor.kw_in_project(df_logs, path)
    kw_in_files = extractor.kw_in_project(df_files, path)
    kw_in_module = kw_in_files - kw_in_function
    print(f"The amount of {extractor.file_to_kw.get(kw)} at function level: {kw_in_function}")
    print(f"The amount of {extractor.file_to_kw.get(kw)} at module level: {kw_in_module}")
    print()
    print()

#TODO: at home look at these files to see how nonlocal is used:
# GOOD EXAMPLE: tot_projects/0/322764981-73991d3b6174a29261cd6b86bc5f1c16a8b13021/star-eyes-student_edit-73991d3/成绩管理系统1/schema/pgsql/pgAdmin 4/venv/Lib/site-packages/pygments/lexers/python.py,1
""" 
name,keywords/nonlocal.json
tot_projects/0/322764981-73991d3b6174a29261cd6b86bc5f1c16a8b13021/star-eyes-student_edit-73991d3/成绩管理系统1/schema/pgsql/pgAdmin 4/venv/Lib/asyncio/tasks.py,2
tot_projects/0/33257894-88424361ede6d9215835cd839cc51b02e5771ff7/BrainTech-pisak-8842436/pisak/scanning.py,1
tot_projects/0/322764981-73991d3b6174a29261cd6b86bc5f1c16a8b13021/star-eyes-student_edit-73991d3/成绩管理系统1/schema/pgsql/pgAdmin 4/venv/Lib/asyncio/staggered.py,1
tot_projects/0/322764981-73991d3b6174a29261cd6b86bc5f1c16a8b13021/star-eyes-student_edit-73991d3/成绩管理系统1/schema/pgsql/pgAdmin 4/venv/Lib/types.py,1
tot_projects/0/322764981-73991d3b6174a29261cd6b86bc5f1c16a8b13021/star-eyes-student_edit-73991d3/成绩管理系统1/schema/pgsql/pgAdmin 4/venv/Lib/sre_compile.py,1
tot_projects/0/322764981-73991d3b6174a29261cd6b86bc5f1c16a8b13021/star-eyes-student_edit-73991d3/成绩管理系统1/schema/pgsql/pgAdmin 4/venv/Lib/zipfile.py,1
tot_projects/0/322764981-73991d3b6174a29261cd6b86bc5f1c16a8b13021/star-eyes-student_edit-73991d3/成绩管理系统1/schema/pgsql/pgAdmin 4/venv/Lib/idlelib/idle_test/htest.py,1
tot_projects/0/322764981-73991d3b6174a29261cd6b86bc5f1c16a8b13021/star-eyes-student_edit-73991d3/成绩管理系统1/schema/pgsql/pgAdmin 4/venv/Lib/functools.py,2
tot_projects/0/770928505-9b13aa338b619080c86e23e0492a5a82deecfa1c/epfl-cs358-2024sp-exoskeleton-9b13aa3/pvenv/Lib/site-packages/pip/_vendor/rich/traceback.py,1
tot_projects/0/770928505-9b13aa338b619080c86e23e0492a5a82deecfa1c/epfl-cs358-2024sp-exoskeleton-9b13aa3/pvenv/Lib/site-packages/pkg_resources/_vendor/pyparsing/core.py,1
tot_projects/0/322764981-73991d3b6174a29261cd6b86bc5f1c16a8b13021/star-eyes-student_edit-73991d3/成绩管理系统1/schema/pgsql/pgAdmin 4/venv/Lib/idlelib/sidebar.py,1
tot_projects/0/770928505-9b13aa338b619080c86e23e0492a5a82deecfa1c/epfl-cs358-2024sp-exoskeleton-9b13aa3/pvenv/Lib/site-packages/pkg_resources/_vendor/pyparsing/helpers.py,1
tot_projects/0/322764981-73991d3b6174a29261cd6b86bc5f1c16a8b13021/star-eyes-student_edit-73991d3/成绩管理系统1/schema/pgsql/pgAdmin 4/venv/Lib/statistics.py,1
tot_projects/0/770928505-9b13aa338b619080c86e23e0492a5a82deecfa1c/epfl-cs358-2024sp-exoskeleton-9b13aa3/pvenv/Lib/site-packages/pip/_vendor/pyparsing/core.py,1"""

