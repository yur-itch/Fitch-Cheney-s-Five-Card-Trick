def parse_file(filename):
    decided4_count = None
    decided5_count = None

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line.startswith('decided4 = {'):
                # Extract dict part after `=`
                dict_str = line.split('=', 1)[1].strip()
                decided4_count = dict_str.count(':')

            elif line.startswith('decided5 = {'):
                dict_str = line.split('=', 1)[1].strip()
                decided5_count = dict_str.count(':')

    print(f"decided4 has {decided4_count} items")
    print(f"decided5 has {decided5_count} items")


# Run it
parse_file("complex_cases_result.py")