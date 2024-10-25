import os
import csv

def csv_to_skyline_results(meets_folder, output_file):
    # List to store all results
    skyline_results = [["Ann Arbor Skyline Team Results"], ["Date", "Meet", "Place", "Score", "URL"]]

    # Iterate over all CSV files in the 'meets' folder
    for csv_filename in os.listdir(meets_folder):
        if csv_filename.endswith(".csv"):
            csv_filepath = os.path.join(meets_folder, csv_filename)
            
            with open(csv_filepath, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)

                # Ensure there are at least 5 rows for valid processing
                if len(rows) < 5:
                    print(f"CSV file {csv_filename} must have at least 5 rows.")
                    continue

                # Extract date, meet name, and URL from the first three rows
                meet = rows[0][0]
                date = rows[1][0]
                link_url = rows[2][0]

                # Loop through the remaining rows and find Skyline results
                for row in rows[4:]:
                    if len(row) == 3 and row[1].strip().lower() == "ann arbor skyline":
                        place = row[0]
                        score = row[2]

                        # Append the result to the skyline_results list
                        skyline_results.append([date, meet, place, score, link_url])

    # Write the results to the output CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerows(skyline_results)

    print(f"Skyline team results written to {output_file}")

# Call the function and process all CSV files in the 'meets' folder
meets_folder = "meets"
output_file = "skyline_team_results.csv"
csv_to_skyline_results(meets_folder, output_file)
