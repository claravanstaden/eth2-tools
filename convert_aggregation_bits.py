file1 = open('in/input_agg_bits.txt', 'r')
Lines = file1.readlines()

count = 0

for line in Lines:
    if "aggregation_bits" in line:
        start = line.rindex("[")
        end = line.rindex("]")
        agg_bits = line[start+1:end].replace(" ", "")
        items_strings = agg_bits.split(",")
        hex_string = '0x'
        for item_string in items_strings:
            hex_string += hex(int(item_string)).split('x')[-1]
        print(str(count) + ":" + hex_string)
        count = count + 1
    else:
        print(line)
