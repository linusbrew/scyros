import polars as pl
import os
import json 
import re
import numpy as np
import matplotlib.pyplot as plt

paths = "/home/linus-brewitz/Code/thesis/scyros/keywords"

class StatisticsExtractor:
    quantiles = [0.25, 0.50, 0.75]
    file_to_kw = dict()
    PATH_KEYWORDS = "keywords/"
    PATH_FIGURES = "figures/"

    # NOTE: this is assuming there is only ONE keyword per file
    def __init__(self):
        for e in os.scandir(paths):
            if e.is_file():
                with open(e.path, "r") as f:
                    data = json.load(f)
                    new_string = data["keywords"][0].replace("\\t", "")
                    new_string = new_string.replace("\\r", "")
                    new_string = new_string.replace("\\v", "")
                    new_string = new_string.replace("\\S", "")
                    new_string = new_string.replace("\\s", "")
                    new_string = new_string.replace("\\b", "")
                    new_string = new_string.replace("\\f", "")
                    new_string = new_string.replace("\\n", "")
                    new_string = re.sub(r'[^A-Za-z\.]', '', new_string)
                    if new_string[0] == "m":
                        new_string = new_string.replace("m", "", 1)
                    self.file_to_kw[e.name] = new_string

    #TODO: this method is supposed to sum over all occurrences of a keyword
    # in a dataframe (files/functions_logs). this is supposed to be used when
    # deciding wether the import are used in module vs function. the thinking is that
    # we know how many times the keyword shows up in a file from the file.csv file, 
    # we also know how many times it shows up in functions. to get how many times they
    # show up in module based we need to subtract the total of file with the total in function
    # i.e., kw_in_module = kw_in_files - kw_in_functions 
    # NOTE: this is the same as kw_in_project(), need to fix that by removing one of them
    def find_kw_in_df(self, df: pl.DataFrame, kw: str) -> int:
        df.select(pl.col(kw).sum()).item()

    def plot_lorenz(self, arr, kw: str) -> None:
        gini_coeff = self.gini(arr)
        lorenz_curve = self.lorenz(arr)
        # we need the X values to be between 0.0 to 1.0
        plt.cla()
        plt.clf()
        plt.plot(np.linspace(0.0, 1.0, lorenz_curve.size), lorenz_curve, label="Lorenz curve for " + kw)
        # plot the straight line perfect equality curve
        plt.plot([0,1], [0,1], label="Equality line")

        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        plt.text(-0.025, 0.83, "Gini = " + str(gini_coeff), bbox=props)
        plt.xlabel("Xes man")
        plt.gca().yaxis.set_label_position("right")
        plt.gca().yaxis.tick_right()
        plt.ylabel("Yes man")
        plt.legend()
        plt.savefig("figures/" + kw + ".png")

    def gini(self, g_arr) -> float:
        # This method was originally posted on GitHubGist by CMCDragonkai 
        # Link: https://gist.github.com/CMCDragonkai/c79b9a0883e31b327c88bfadb8b06fc4
        count = g_arr.size
        coefficient = 2 / count
        indexes = np.arange(1, count + 1)
        weighted_sum = (indexes * g_arr).sum()
        total = g_arr.sum()
        constant = (count + 1) / count
        return round(coefficient * weighted_sum / total - constant, 4)

    def lorenz(self, l_arr):
        # This method was originally posted on GitHubGist by CMCDragonkai 
        # Link: https://gist.github.com/CMCDragonkai/c79b9a0883e31b327c88bfadb8b06fc4

        # this divides the prefix sum by the total sum
        # this ensures all the values are between 0 and 1.0
        scaled_prefix_sum = l_arr.cumsum() / l_arr.sum()
        # this prepends the 0 value (because 0% of all people have 0% of all wealth)
        return np.insert(scaled_prefix_sum, 0, 0)

    def column_as_numpy(self, df: pl.DataFrame, column: str) -> np.array:
        sorted = df.sort(column)
        selected_col = sorted.select(pl.col(column))
        result = selected_col.to_numpy()
        return np.ravel(result)

    def count_rows(self, df: pl.DataFrame) -> int:
        return df.select(pl.count()).item()

    def num_after_cleanup(self, df_before: pl.DataFrame, df_after: pl.DataFrame) -> int:
        return self.count_rows(df_before) - self.count_rows(df_after)

    def percentage_after_cleanup(self, df_before: pl.DataFrame, df_after: pl.DataFrame) -> float:
        return round((self.count_rows(df_after) / self.count_rows(df_before)) * 100, 2)

    def percentage_imports(self, df: pl.DataFrame, numerator: str, deno: str) -> float:
        numerator_num = df.select(pl.col(numerator).sum().round(2)).item()
        deno_num = df.select(pl.col(deno).sum().round(2)).item()
        percentage = numerator_num / (numerator_num + deno_num)
        return round(percentage, 2)

    def functions_with_kw(self, df_files: pl.DataFrame) -> int:
        return df_files.select(((pl.col("functions_with_kw").sum() / 
                        pl.col("functions").sum()) * 100).round(2)).item()
    
    # Function that calculates the share of a certain keyword
    # compared to all functions 
    def calculate_share_functions_with_keyword(self, df: pl.DataFrame, kw: str,
                                                column: str) -> float:
        return df.select(((pl.col(kw).sum() / pl.col(column).sum()) * 100).round(2)).item()
        
    # Column can be either LOC or words, check how on avg how large a file is if
    # it contains a keyword
    #TODO: larger files will probably be more likely to contain keywords,
    # so might need to use weighted somehow
    def avg_length(self, df: pl.DataFrame, length: str, keyword: str) -> float:
        non_zero = df.remove(pl.col(keyword) == 0)
        return non_zero.select(pl.col(length).mean().round(2)).item()
    
    def median_length(self, df: pl.DataFrame, length: str, keyword: str) -> int:
        non_zero = df.remove(pl.col(keyword) == 0)
        return non_zero.select(pl.col(length).median().round(2)).item()

    # NOTE: just in case I need to clean the data because of the errors
    def clean_projects(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.remove(pl.col("path") == "error")

    # TODO: fix so the column does not have to be mentioned, i.e., it will just automatically
    # work. to do this the program needs to know how and many and what keywords I'm looking for
    def kw_in_project(self, df: pl.DataFrame, column: str) -> int:
        kw_count = df.select(pl.col(column)).sum().item()
        return kw_count
    
    # To see how the ratio between the total LOC and the LOC that contain 
    # the keyword. This is only intended if we have one keyword, must
    # be updated when doing this with multiple keywords
    # NOTE: this actually works for words as well since we specify
    # the columns before the call
    def kw_ratio_project(self, df: pl.DataFrame, part: str, total: str) -> float:
        return df.select(((pl.col(part).sum() / pl.col(total).sum()) * 100).round(2)).item()

    def max_keyword_project(self, df: pl.DataFrame, column: str) -> int:
        return df.select(pl.col(column).max()).item()
    
    def min_keyword_project(self, df: pl.DataFrame, column: str) -> int:
        return df.select(pl.col(column).min()).item()

    def calculate_mean(self, df: pl.DataFrame, column: str) -> int:
        df_mean = df.mean()
        return df_mean.select(pl.col(column).round(2)).item()
    
    def calculate_median(self, df: pl.DataFrame, column:str) -> int:
        df_median = df.median()
        return df_median.select(pl.col(column)).item()

    def calculate_variance(self, df: pl.DataFrame, column:str) -> int:
        df_var = df.var()
        return round(df_var.select(pl.col(column)).item(), 2)

    def calculate_sigma(self, df: pl.DataFrame, column:str) -> int:
        df_sigma = df.std()
        return round(df_sigma.select(pl.col(column)).item(), 2)

    def calculate_quant(self, df: pl.DataFrame, column:str) -> tuple[int, int, int]:
        result = list()
        foo = df.select(pl.col(column))
        for quantile in self.quantiles:
            result.append(foo.quantile(quantile=quantile).item())
        return tuple(result)
    