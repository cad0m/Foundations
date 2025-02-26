import csv
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    with open(sys.argv[2], "r") as DNAtext:
        sequence = DNAtext.read()

    with open(sys.argv[1]) as file:
        database_reader = csv.DictReader(file)
        header = database_reader.fieldnames[1:]

        # Find the longest match of each STR in the DNA sequence and store it in LongSTRs
        LongSTRs = {}
        for str in header:
            count = longest_match(sequence, str)
            LongSTRs[str] = count

        # Check the database for matching profiles
        for row in database_reader:
            itis = True
            for str in header:
                profile = int(row[str])
                if profile != LongSTRs[str]:
                    itis = False
                    break
            if itis:
                print(row["name"])
                sys.exit(0)

    print("No match")
    return
def longest_match(sequence, subsequence):
    """Returns the length of the longest run of subsequence in the sequence."""
    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in the sequence for the longest consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize the count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within the sequence
        # If a match, move the substring to the next potential match in the sequence
        # Continue moving the substring and checking for matches until out of consecutive matches
        while True:
            # Adjust the substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            # If there is no match in the substring
            else:
                break

        # Update the longest consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in the sequence, return the longest run found
    return longest_run


if __name__ == "__main__":
    main()
