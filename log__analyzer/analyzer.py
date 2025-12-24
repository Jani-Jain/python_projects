def parse_log_line(line):
    parts = line.split()

    if len(parts) < 4 :
        return None

    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = " ".join(parts[3:])

    return timestamp,level,message

#readlogfile
def read_log_file(filepath):
    entries = []

    with open(filepath, "r") as file:
        for line in file :
            parsed = parse_log_line(line.strip())
            if parsed is not None :
                entries.append(parsed)

    return entries

def count_by_level(entries):
    counts = {}

    for entry in entries:
        level = entry[1]

        if level not in counts:
            counts[level] = 0

        counts[level] += 1

    return counts

def most_common_messages(entries, top_n):
    messages = {}
    
    for timestamp,level,message in entries:
        if message in messages :
            messages[message] += 1
        else :
            messages[message] = 1
    
    tuple_of_counts = list(messages.items())
    tuple_of_counts.sort(key = lambda x:x[1],reverse = True)

    return tuple_of_counts[:top_n]   
