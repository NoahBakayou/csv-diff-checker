import pandas as pd

def compare_csv(file1, file2):
    # Determine maximum number of columns expected based on the header of the files
    def get_max_columns(*files):
        max_cols = 0
        for file in files:
            with open(file, 'r') as f:
                line = f.readline()
                max_cols = max(max_cols, line.count(',') + 1)  # Adding 1 because count(',') gives one less than number of fields
        return max_cols

    max_columns = get_max_columns(file1, file2)

    # Define a function to handle bad lines by padding shorter lines
    def on_bad_line(line):
        if len(line) < max_columns:
            return line + [None] * (max_columns - len(line))
        return line

    # Read the CSV files, handling bad lines with the custom function
    df1 = pd.read_csv(file1, on_bad_lines=on_bad_line, engine='python')
    df2 = pd.read_csv(file2, on_bad_lines=on_bad_line, engine='python')

    # Perform an outer join to find rows that are different
    diff = pd.concat([df1, df2]).drop_duplicates(keep=False)

    # Output the differences
    if diff.empty:
        print("No differences found.")
    else:
        print("Differences found:")
        print(diff)

if __name__ == "__main__":
    # File paths (you can change these as needed)
    file1 = 'Test1.csv'
    file2 = 'Test2.csv'

    # Compare the CSV files
    compare_csv(file1, file2)
