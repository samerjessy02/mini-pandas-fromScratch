from file_handler import read_csv_file, read_dtype, write_file
from stats import *
import csv

class DataFrame:
    def __init__(self, data:dict, dtype:dict):
        self.data = data
        self.dtype = dtype
    

    @classmethod
    def read_csv(cls, data_path="titanic.csv", dtype_path="titanic_dtype.csv"):
        data_dict = read_csv_file(data_path)
        dtype_dict = read_dtype(dtype_path)
        return cls(data_dict, dtype_dict)
    

    def count_nulls(self):
        nulls_dict = {}

        for col_name , col_lst in self.data.items():
            nulls_dict[col_name] = len([elem for elem in col_lst if elem is None])
        
        return nulls_dict
    

    def describe(self, path:str="describe.csv"):
        columns = ["column", "nulls", "max", "min", "mean", "median", "mode"]
        with open(file=path, mode="w", newline="") as file:
            write = csv.writer(file)
            write.writerow(columns)

            for col_name, col_lst in self.data.items():
                write.writerow([col_name, self.count_nulls()[col_name],  get_col_max(col_lst), get_col_min(col_lst), get_col_median(col_lst), get_col_mode(col_lst)])
    


    def fillna(self, num_strategy=get_col_mean, cat_strategy=get_col_mode):
        for col_name , col_lst in self.data.items():
            for elem_idx , elem in enumerate(col_lst):
                if elem is None:
                    if self.dtype[col_name] in ("int", "float"):
                        self.data[col_name][elem_idx] = num_strategy(col_lst)
                    else:
                        self.data[col_name][elem_idx] = cat_strategy(col_lst)
                else:
                    self.data[col_name][elem_idx] = elem
    


    def to_csv(self, path:str="out.csv"):
        write_file(path, self.data)


                


    







df = DataFrame.read_csv()
# print(df.data)
# print(df.dtype)
print(df.count_nulls())
df.describe()
df.to_csv()
df.fillna()
df.to_csv("fillna_df.csv")
df.describe("post_fill_desc.csv")


