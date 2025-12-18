import analyzer as a
def main():
    filepath = input("Paste your log file path: ")
    top_n = int(input("How many top messages do you want to see? "))

    entries = a.read_log_file(filepath)

    level_counts = a.count_by_level(entries)
    top_messages = a.most_common_messages(entries, top_n)

    print("\nLog level counts:")
    for level, count in level_counts.items():
        print(f"{level}: {count}")

    print(f"\nTop {top_n} most common messages:")
    for message, count in top_messages:
        print(f"{message} ({count})")


if __name__ == "__main__":
    main()
