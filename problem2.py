import sys
import json

cache = {}
depth = 0
def print_depth_object(data):

    global cache
    global depth

    if not(data) or not isinstance(data,dict):
        return ""

    depth += 1
    for key,val in data.items():
        print(val)
        if isinstance(val, dict):
            print_depth_object(val) 
            depth -= 1
        elif isinstance(val, object):
            print_depth_object(val.__dict__)
            depth -= 1
        cache[key] = depth

    if depth==1:
        return sort_output(cache)
    else:
        return "Error"


    depth += 1
    for key,val in data.items():
        print(type(val))

def sort_output(output):
    global cache
    global depth

    output_str = ""
    sorted_output = sorted(output.items(), key=lambda x:(x[1],x[0]))
    cache = {}
    depth = 0
    for item in sorted_output:
        output_str += f"{item[0]} {item[1]}\n"
    return output_str






    


