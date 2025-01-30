import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py databases/large.csv sequences/5.txt")

    # TODO: Read database file into a variable
    databaseList = []
    filename = sys.argv[1]
    with open(filename) as file:
        reader = csv.DictReader(file)
        for entry in reader:
            databaseList.append(entry)

    # for entry in databaseList:
    # print (entry)

    # TODO: Read DNA sequence file into a variable
    sequenceFileName = sys.argv[2]
    with open(sequenceFileName) as file:
        sequence = file.read()

    # print (sequence)

    # TODO: Find longest match of each STR in DNA sequence
    longestMatchDict = {}
    for i in databaseList[0]:
        if i != "name":
            # print (i, longest_match(sequence, i))
            longestMatchDict[i] = longest_match(sequence, i)

    # print(longestMatchDict)

    # TODO: Check database for matching profiles

    for person in databaseList:
        # Iterate through each person in the database
        matched = "No matched"
        for codeDNA in longestMatchDict:
            if int(person[codeDNA]) != longestMatchDict[codeDNA]:
                matched = False
                # print (person[codeDNA], longestMatchDict[codeDNA])

                break

        if matched:
            return print(person["name"])

    return print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
