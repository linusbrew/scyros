import polars as pl

class StatisticsExtractor:
    quantiles = [0.25, 0.50, 0.75]

    # NOTE: just in case I need to clean the data because of the errors
    def clean_projects(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.remove(pl.col("path") == "error")

    # TODO: fix so the column does not have to be mentioned, i.e., it will just automatically
    # work. to do this the program needs to know how many keywords I'm looking for
    def kw_in_project(self, df: pl.DataFrame, column: str) -> int:
        kw_count = df.select(pl.col(column) == 0).sum().item()
        return kw_count
    
    # To see how the ratio between the total LOC and the LOC that contain 
    # the keyword. This is only intended if we have one keyword, must
    # be updated when doing this with multiple keywords
    # NOTE: this actually works for words as well since we specify
    # the columns before the call
    def kw_ratio_project(self, df: pl.DataFrame, c1: str, c2: str) -> float:
        return df.select((pl.col(c2).sum() / pl.col(c1).sum()) * 100).item()

    #TODO: fix so I do not have so many seperate methods when they essentially
    # do the same thing. globals() might be useful
    def calculate_mean_all(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.mean()

    def calculate_mean_attr(self, df: pl.DataFrame, column: str) -> int:
        df_mean = df.mean()
        return df_mean.select(pl.col(column)).item()
    
    def calculate_median_all(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.median()
    
    def calculate_median_attr(self, df: pl.DataFrame, column:str) -> int:
        df_median = df.median()
        return df_median.select(pl.col(column)).item()

    def calculate_variance_all(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.var()

    def calculate_variance_attr(self, df: pl.DataFrame, column:str) -> int:
        df_var = df.var()
        return df_var.select(pl.col(column))

    def calculate_sigma_all(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.std()

    def calculate_sigma_attr(self, df: pl.DataFrame, column:str) -> int:
        df_sigma = df.std()
        return df_sigma.select(pl.col(column)).item()
    
    def calculate_quant_all(self, df: pl.DataFrame) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
        result = list()
        for quantile in self.quantiles:
            result.append(df.quantile(quantile=quantile))
        return tuple(result)

    def calculate_quant_attr(self, df: pl.DataFrame, column:str) -> tuple[int, int, int]:
        result = list()
        foo = df.select(pl.col(column))
        for quantile in self.quantiles:
            result.append(foo.quantile(quantile=quantile))
        return tuple(result)
    