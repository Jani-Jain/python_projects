import analyzer as a
import argparse
def main():
    parser = argparse.ArgumentParser(
        description="Analyze log files and summarize log levels and frequent messages."
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path to the log file"
    )

    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Number of most common messages to display"
    )  

    args = parser.parse_args()    

    if args.top <= 0:
        raise argparse.ArgumentTypeError(f"Please specify a positive number , not {args.top}")


    entries = a.read_log_file(args.file)

    level_counts = a.count_by_level(entries)
    top_messages = a.most_common_messages(entries, args.top)

    print("\nLog level counts:")
    for level, count in level_counts.items():
        print(f"{level}: {count}")

    print(f"\nTop {args.top} most common messages:")
    for message, count in top_messages:
        print(f"{message} ({count})")


if __name__ == "__main__":
    main()
