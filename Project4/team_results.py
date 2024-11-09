import os
import csv
from datetime import datetime

def csv_to_skyline_results(meets_folder, output_file):
    # List to store all results
    skyline_results = [["Ann Arbor Skyline Team Results"], ["Date", "Meet", "Category", "Place", "Score", "URL", "HTML"]]

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
                date_str = rows[1][0]
                link_url = rows[2][0]

                # Determine the category (Mens or Womens) based on the meet name
                if "Mens" in meet:
                    category = "Mens"
                elif "Womens" in meet:
                    category = "Womens"
                else:
                    category = "Unknown"  # Fallback if neither is found

                # Convert CSV filename to HTML filename
                html_filename = os.path.splitext(csv_filename)[0] + '.html'

                # Try parsing the date (assuming the format "Sat Sep 14 2024")
                try:
                    meet_date = datetime.strptime(date_str, '%a %b %d %Y')
                except ValueError:
                    print(f"Invalid date format in file {csv_filename}. Skipping this file.")
                    continue

                # Loop through the remaining rows and find Skyline results
                for row in rows[4:]:
                    if len(row) == 3 and row[1].strip().lower() == "ann arbor skyline":
                        place = row[0]
                        score = row[2]

                        # Append the result to the skyline_results list
                        skyline_results.append([
                            meet_date.strftime('%a %b %d %Y'), 
                            meet, 
                            category, 
                            place, 
                            score, 
                            link_url, 
                            html_filename  # Add HTML column
                        ])

    # Sort the results by date
    skyline_results_sorted = sorted(skyline_results[2:], key=lambda x: datetime.strptime(x[0], '%a %b %d %Y'))

    # Write sorted results to the output CSV file
    write_csv(output_file, skyline_results[:2] + skyline_results_sorted)

    print(f"Skyline team results written to {output_file}")


def write_csv(output_file, data):
    with open(output_file, mode='w', newline='', encoding='utf-8') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerows(data)


# Call the function and process all CSV files in the 'meets' folder
meets_folder = "meets"
output_file = "skyline_team_results.csv"
csv_to_skyline_results(meets_folder, output_file)
