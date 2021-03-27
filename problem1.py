import sys
import json

cache = {}
depth = 0
def print_depth(data):

    global cache
    global depth

    if not(data) or type(data)!=dict:
        return ""

    depth += 1
    for key,val in data.items():
        if type(val)==dict:
            print_depth(val) 
            depth -= 1
        
        cache[key] = depth
    if depth==1:
        return sort_output(cache)
    else:
        return "Error"

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



if __name__ == "__main__":
    try:
        with open(sys.argv[1]) as f:
            data = json.loads(f.read())
        print(print_depth(data))
    except IndexError:
        pass

    


