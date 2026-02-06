from functools import reduce
from file_handler import read_csv_file , write_file , read_dtype

def get_col_max(col:list):
    if col and isinstance(col[0], (int, float)):
        clean_col = [num for num in col if not num is None]
        return reduce(lambda num1, num2 : num1 if num1 > num2 else num2 ,clean_col)
    else:
        return None
    
# col = []
# print(get_col_max(col))


def get_col_min(col:list):
    if col and isinstance(col[0], (int, float)):
        clean_col = [num for num in col if not num is None]
        return reduce(lambda num1, num2 : num1 if num1 < num2 else num2 ,clean_col)
    else:
        return None
    
# col = [12, 33,4455 , 3, 455, 6777, 885]
# print(get_col_min(col))


def get_col_mean(col:list):
    if col and isinstance(col[0], (int, float)):
        clean_col = [num for num in col if not num is None]
        return reduce(lambda num1, num2 : num1 + num2 ,clean_col)/len(clean_col)
    else:
        return None

# col = [3,5,2,4,6, None]
# print(get_col_mean(col))
    


def get_col_median(col:list):
    if col and isinstance(col[0], (int, float)):
        clean_col = [num for num in col if not num is None]
        print(clean_col)
        sorted_col = sorted(clean_col)
        print(sorted_col)
        size = len(sorted_col)
        if (len(clean_col)) % 2 == 0:
            return (sorted_col[size//2] + sorted_col[(size//2) - 1])/2
        else:
            return sorted_col[size//2]
    else:
        return None

# col = [4, 2, 1, 3,5, None]
# print(get_col_median(col))



def get_col_mode(col:list):
    clean_col = [elem for elem in col if not elem is None]
    freq_dict = {}
    if col:
        for elem in clean_col:
            freq_dict[elem]  = freq_dict.get(elem , 0) + 1
        return sorted(freq_dict.items(), key=lambda item : item[1], reverse=True)[0][0]
    else:
        return None
    
col = ["1", "3", None, "3", "3", "3"]
print(get_col_mode(col))


def get_stat(data:dict, dtypes:dict, function= get_col_mode):
    stats_dict = {}
    for col_name , col_lst in data.items():
        if dtypes[col_name] in ("int", "float"):
            stats_dict[col_name] = function(col_lst)
        else:
            stats_dict[col_name] = function(col_lst)

    return stats_dict


dtypes = read_dtype()
data = read_csv_file()

print(get_stat(data=data, dtypes=dtypes,function=get_col_mode))