import analyzer as a
import argparse
import sys

def main():
    try :
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

        entries = a.read_log_file(args.file)

        level_counts = a.count_by_level(entries)
        top_messages = a.most_common_messages(entries, args.top)

        print("\nLog level counts:")
        for level, count in level_counts.items():
            print(f"{level}: {count}")

        print(f"\nTop {args.top} most common messages:")
        for message, count in top_messages:
            print(f"{message} ({count})")
        
        #Error handling
        if args.top <= 0:
            print("Error: --top must be a positive integer")
            sys.exit(1)

        if not entries:
            print("Error: Log file contains no valid log entries")
            sys.exit(1)

    except FileNotFoundError:
        print("Error: File does not exist or cannot be opened")
        sys.exit(1)

if __name__ == "__main__":
    main()
