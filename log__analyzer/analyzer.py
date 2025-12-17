def parse_log_line(line):
    parts = line.split()

    if len(parts) < 4 :
        return None
#Variables 
    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = " ".join(parts[3:])

    return timestamp,level,message