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
        try:
            if isinstance(val, dict):
                print_depth_object(val) 
                depth -= 1
            elif isinstance(val.__dict__, dict):
                print_depth_object(val.__dict__)
                depth -= 1
        except AttributeError:
            pass
        if key in cache:
            cache[key+'@'+str(depth)] = depth
        else:
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
        out_val = str(item[1])
        repeat_key = '@'+out_val in item[0]
        if repeat_key:
            out_key = item[0].split('@')[0]
        else:
            out_key = item[0] 
        output_str += f"{out_key} {out_val}\n"
    return output_str

if __name__ == "__main__":
    try:
        with open(sys.argv[1]) as f:
            data = json.loads(f.read())
        print(print_depth_object(data))
    except IndexError:
        pass




    


