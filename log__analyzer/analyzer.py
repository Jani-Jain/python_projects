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