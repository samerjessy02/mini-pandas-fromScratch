from functools import reduce
import numpy as np
import pandas as pd
import pandas as pd
import json 
import csv



def read_dtype(file_path:str = "titanic_dtype.csv"):
    dtype_dict = {}
    try:
        with open(file=file_path, mode="r", newline="") as file:
            rows = csv.reader(file)
            header = next(file)
            for row in rows:
                dtype_dict[row[0]] = row[1]
            return dtype_dict
    except FileNotFoundError as e:
        print(f"{file_path} not found!")
    except Exception:
        print("Something went wrong")

# print(read_dtype())

def read_csv_file(file_path:str="titanic.csv", dtypes:dict=None):

    if dtypes is None:
        dtypes = read_dtype()

    data_dict = {}

    data_type_map = {"int": int,
                     "string": str,
                     "float" : float}
    try:
        with open(file=file_path, mode="r", newline="") as file:
            rows = csv.reader(file)
            header = next(file)
            header = [x.strip() for x in header.split(",")]
            for col_name in header:
                data_dict[col_name] = []
            for row in rows:
                for row_idx, row_val in enumerate(row):
                    # print(dtypes[header[row_idx]], row_val)
                    if row_val == "":
                        data_dict[header[row_idx]].append(None)
                    else:
                        data_dict[header[row_idx]].append(data_type_map[(dtypes[header[row_idx]])](row_val))
            return data_dict
    except FileNotFoundError as e:
        print(f"{file_path} not found")
    except Exception:
        print("Something went wrong")

# print(read_csv_file())


def write_file(file_path:str="out.csv", data:dict=None):
    if data is None:
        data = read_csv_file()
    col_names = list(data.keys())
    
    with open(file=file_path, mode="w", newline="") as file:
        write = csv.writer(file)
        write.writerow(col_names)
        write.writerows(zip(*data.values()))
        
write_file()

    