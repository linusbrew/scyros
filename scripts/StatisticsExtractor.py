import polars as pl
import os
import json 

paths = "/home/linus-brewitz/Code/thesis/scyros/keywords"

class StatisticsExtractor:
    quantiles = [0.25, 0.50, 0.75]
    file_to_kw = dict()

    # NOTE: this is assuming there is only ONE keyword per file
    def __init__(self):
        for e in os.scandir(paths):
            if e.is_file():
                with open(e.path, "r") as f:
                    data = json.load(f)
                    new_string = data["keywords"][0].replace("\\", "")
                    self.file_to_kw[e.name] = new_string

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
    