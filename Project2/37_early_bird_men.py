import csv
import html

# Set the path to the CSV file
csv_file = 'Client-Data-Files/meets/37th_Early_Bird_Open_Mens_5000_Meters_HS_Open_5K_24.csv'

# Open the CSV file and extract the data
with open(csv_file, newline='', encoding='utf-8') as file:
   reader = csv.reader(file)
   data = list(reader)

# Extract meet information based on provided indices
meet_name = data[0][0]  # Cell A1 - Meet Name
meet_date = data[1][0]  # Cell A2 - Meet Date
team_results_link = data[2][0]  # Cell A3 - hyperlink for the team-results section
race_comments = " ".join(data[3][0:9])   # Row 4 - race-comments section
race_comments = html.escape(race_comments)  # Escape any special HTML characters

# Extract team results starting from row 8 (index 7) assuming columns A, B, and C
team_results = []
for row in data[7:12]:  # Selecting first 5 rows of team results as requested
   if len(row) >= 3:
      place, team, score = row[0], row[1], row[2]
      team_results.append({
         'place': place,
         'team': team,
         'score': score
      })

# Extract athlete details
athlete_results = []
indices = [54, 66, 73, 84, 100]  # The indices of the sample rows
for i in indices:  # Selecting rows
   row = data[i] # Selecting athlete results as requested
   if len(row) >= 8:
      place = row[0]
      grade = row[1]
      name = row[2]
      athlete_link = row[3]
      time = row[4]
      team = row[5]
      team_link = row[6]
      profile_pic = row[7]
      
      athlete_results.append({
         'place': place,
         'grade': grade,
         'name': name,
         'athlete_link': athlete_link,
         'time': time,
         'team': team,
         'team_link': team_link,
         'profile_pic': profile_pic
      })

# Build the HTML content using the extracted data
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel="stylesheet" href="css/reset.css">
   <link rel="stylesheet" href="css/style.css">
   <title>{meet_name} Country Meet</title>
</head>
<body>

<header>
   <nav>
      <ul>
         <li><a href="index.html">Home</a></li>
         <li><a href="#athlete-results">Athlete Results</a></li>
         <li><a href="#team-results">Team Results</a></li>
         <li><a href="#overall-comments">Overall Comments</a></li>
         <li><a href="#photo-gallery">Photo Gallery</a></li>
      </ul>
   </nav>
   
   <h1>{meet_name}</h1>
   <h2>{meet_date}</h2>
</header>

<section id="athlete-results">
   <h2>Athlete Results</h2>
   <table>
      <tr>
         <th>Name</th>
         <th>Grade</th>
         <th>Time</th>
         <th>Place</th>
         <th>Team</th>
         <th>Profile Picture</th>
      </tr>'''

# Populate athlete results into the HTML table
for athlete in athlete_results:
    html_content += f'''
      <tr>
         <td><a href="{athlete['athlete_link']}">{athlete['name']}</a></td>
         <td>{athlete['grade']}</td>
         <td>{athlete['time']}</td>
         <td>{athlete['place']}</td>
         <td><a href="{athlete['team_link']}">{athlete['team']}</a></td>
         <td><img src="Client-Data-Files/images/AthleteImages/{athlete['profile_pic']}" alt="{athlete['name']}'s picture" width="60" height="80"></td>
      </tr>'''

html_content += f'''
   </table>
</section>

<section id="team-results">
   <h2>Team Results</h2>
   <a href="{team_results_link}">View Full Team Results</a>
   <table>
      <tr>
         <th>Place</th>
         <th>Team</th>
         <th>Score</th>
      </tr>'''

# Populate team results into the HTML table 
for result in team_results:
    html_content += f'''
      <tr>
         <td>{result['place']}</td>
         <td>{result['team']}</td>
         <td>{result['score']}</td>
      </tr>'''

html_content += f'''
   </table>
</section>

<section id="overall-comments">
   <h2>Overall Comments</h2>
   <p>{race_comments}</p>
</section>'''

html_content += '''
<section id="photo-gallery">
   <h2>Photo Gallery</h2>
'''

# Add images from IMG_9022 to IMG_9026
html_content += '<div>'
for i in range(9022, 9027):
    html_content += f'''
      <img src="Client-Data-Files/images/earlybird/IMG_{i}.jpg" alt="IMG_{i}" width="150" height="150" />
    '''
html_content += '</div>'
      
# Add images from IMG_9030 to IMG_9034
html_content += '<div>'
for i in range(9030, 9035):
    html_content += f'''
      <img src="Client-Data-Files/images/earlybird/IMG_{i}.jpg" alt="IMG_{i}" width="150" height="150" />
    '''
html_content += '</div>'

html_content += f'''
</section>

<!-- Footer Section -->
<footer>
   <p>&copy; {meet_name}. All Rights Reserved.</p>
</footer>

</body>
</html>'''

# Save the updated HTML content to a file
output_html_file_path = 'meet_results_website_men.html'
with open(output_html_file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

output_html_file_path
