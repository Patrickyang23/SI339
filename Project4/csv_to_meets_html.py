import csv
import os
import random
import html  # To safely escape filenames in HTML

def csv_to_html(csv_filename, output_folder):
    # Derive the HTML filename by replacing the CSV extension with '.html' in the meets folder
    html_filename = os.path.join(output_folder, os.path.splitext(os.path.basename(csv_filename))[0] + '.html')

    # try:
    with open(csv_filename, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        # Ensure there are at least 5 rows for valid HTML generation
        if len(rows) < 5:
            print("CSV file must have at least 5 rows.")
            return

        # Extract values from the first five rows
        link_text = rows[0][0]
        h2_text = rows[1][0]
        link_url = rows[2][0]
        summary_text = rows[3][0]

        # Initialize HTML content
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{link_text}</title>
<link rel="stylesheet" href="../css/reset.css">
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
    <body>
    <a class="skip" href = "#main">Skip to Main Content</a>
    <nav>
        <div class="nav-left">
            <div class="hamburger" tabindex="0">&#9776;</div>  <!-- Hamburger icon (three lines) -->
            <div>Skyline Cross Country 2024</div>
        </div>
        
        <div class="nav-right">
            <button id="dark-mode-toggle" onclick="toggleDarkMode()" aria-label="Toggle Dark Mode">
                <i class="fas fa-moon"></i>
            </button>
            <img src="../images/skylineeagle.jpg" alt="Skyline Eagles Logo" class="nav-logo">
        </div>
    """
    
        html_content += """
        
        <!-- Side menu for small screens (hidden by default) -->
        <div class="side-menu">
            <ul>
                <li><a href="../index.html" tabindex="0">Home Page</a></li>
                <li><a href="#summary" tabindex="0">Summary</a></li>
                <li><a href="#team-results" tabindex="0">Team Results</a></li>
                <li><a href="#individual-results" tabindex="0">Individual Results</a></li>
                <li><a href="#gallery" tabindex="0">Photo Gallery</a></li>
            </ul>
        </div>
        <div class="overlay"></div> <!-- Background overlay -->
    </nav>
    """
    
        html_content += f"""
    <header class="meets" tabindex="0">
        <h1><a href="{link_url}">{link_text}</a></h1>
        <h2>{h2_text}</h2>
    </header>
    
    <main id = "main">


    <section class="summary" id="summary" tabindex="0">
        <div class="section-header">
            <h2><i class="fas fa-sticky-note"></i> Race Summary</h2>
            <button class="toggle-button" aria-expanded="true" data-section="Summary">Hide Summary</button>
        </div>
        <div class="collapsible-content open">
            <div class="summary-container" tabindex="0">
                {summary_text}
            </div>
        </div>
    </section>
    """
    
        # Start container for individual results
        html_content += """<section id="team-results" tabindex="0">\n
        <div class="section-header">
            <h2><i class="fas fa-medal"></i> Team Results</h2>
            <button class="toggle-button" aria-expanded="true" data-section="Results">Hide Results</button>
        </div>\n
        """
        
        # Add a collapsible div container to enable scrolling
        html_content += """
        <div class="collapsible-content open">\n
            <div class="table-container">\n"""
        
        # Process the remaining rows (after the first five)
        html_content += """<table>\n"""
        table_start = True

        for row in rows[4:]:
            # For rows that are 3 columns wide, add to the team places list
            if len(row) == 3:
                if row[0] == "Place":
                    html_content += f"<tr><th>{row[0]}</th><th>{row[1]}</th><th>{row[2]}</th></tr>\n"

                else:
                    html_content += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td> {row[2]}</td></tr>\n"

            # For rows that are 8 columns wide and contain 'Ann Arbor Skyline' in column 6
            elif len(row) == 8 and row[5].strip().lower() == 'ann arbor skyline':
                if table_start == True:
                    table_start = False
                    html_content += """</table>\n
            </div>\n
        </div>\n"""
                    html_content += """
    </section>\n
    <section id="individual-results" tabindex="0">\n
        <div class="section-header">
            <h2><i class="fas fa-running"></i> Individual Results</h2>              
            <button class="toggle-button" aria-expanded="true" data-section="Results">Hide Results</button>
        </div>
        
        <div class="collapsible-content open">
        <div class="individual-results-container">
            <div class="athlete-cards-container">
            
            <!-- No results message (hidden by default) -->
            <p id="no-results-message" >No results matched your criteria.</p>
            """

                place = row[0]
                grade = row[1]
                name = row[2]
                time = row[4]
                profile_pic = row[7]

                # Add the athlete div
                html_content += f"""
            <div class="athlete-card" data-grade="{grade}" data-name="{name.lower()}">
                <figure class="athlete-figure"> 
                    <img src="../images/profiles/{profile_pic}" width="200" alt="Profile picture of {name}"> 
                    <figcaption>{name}</figcaption>
                </figure>
                
                <div class="athlete-info">
                    <dl>
                        <dt>Place</dt><dd>{place}</dd>
                        <dt>Time</dt><dd>{time}</dd>
                        <dt>Grade</dt><dd>{grade}</dd>
                    </dl>
                </div>
            </div>
            """

        html_content += """
        </div>\n
                
        <!-- Floating Action Buttons (FABs) -->
        <div class="fab-container">
            <button class="fab" id="fab-filter" aria-label="Filter by Grade">
                <i class="fas fa-filter"></i>
            </button>
            <button class="fab" id="fab-search" aria-label="Search by Name">
                <i class="fas fa-search"></i>
            </button>
        </div>
        
        </div>\n
        
        <!-- Modal for searching by name -->
        <div id="search-modal" class="modal">
            <div class="modal-content">
                <h3>Search by Name</h3>
                <label for="name-search" class="sr-only">Enter Athlete Name</label>
                <input type="text" id="name-search" placeholder="Enter Athlete Name" aria-label="Enter Athlete Name">
                <button id="apply-search">Search</button>
            </div>
        </div>
        
        <!-- Modal for filtering by grade -->
        <div id="filter-modal" class="modal">
            <div class="modal-content">
                <h3>Filter by Grade</h3>
                <label for="grade-filter" class="sr-only">Select Grade</label> 
                <select id="grade-filter" class="filter-select" aria-label="Select Grade">
                    <option value="all">All Grades</option>
                    <option value="9">Grade 9</option>
                    <option value="10">Grade 10</option>
                    <option value="11">Grade 11</option>
                    <option value="12">Grade 12</option>
                </select>
                <button id="apply-filter">Apply</button>
            </div>
        </div>
        </div>\n
        </section>\n
        
        """
        meet_id = extract_meet_id(link_url)
        # Get the list of images from the folder
        image_list = create_meet_image_gallery(link_url)

        html_content += """
        <section id = "gallery" tabindex="0">
            <div class="section-header">
                <h2><i class="fas fa-camera"></i> Photo Gallery</h2>
                <button class="toggle-button" aria-expanded="true" data-section="Gallery">Hide Gallery</button>
            </div>
            
            <div class="collapsible-content open">
                <div class="gallery-container">
                    """
        if isinstance(image_list, list) and image_list:  # Check if image_list is a non-empty list
            html_content += """
                    <div class="gallery-slide">
            """
            html_content += f"""
                    <button class="arrow left-arrow" onclick="prevImage()">&#10094;</button> <!-- Left arrow -->
                    <img id="gallery-image" src="../images/meets/{meet_id}/{image_list[0]}" alt="Skyline Gallery Images">
                    <button class="arrow right-arrow" onclick="nextImage()">&#10095;</button> <!-- Right arrow -->
            """
            
        else:  # If image_list is a message string
            # Display a "Waiting for update" message if no images are found
            html_content += """
                <p>Wait for updating photo gallery for this meet.</p>
            """

        html_content += """
                </div>
            </div>
        </section>
        """
    
        # Close the HTML document
        html_content += """
            </div>
            </div>
        </section>
        """    

        # Add any necessary JavaScript for the gallery only if images exist
        if isinstance(image_list, list) and image_list:
            # Convert Python list of images to a JavaScript array format
            js_image_array = f"const images = {image_list};"
            html_content += f"""
            <script>
                const meet_id = "{meet_id}";  // Pass meet_id as a JavaScript variable
                {js_image_array}  // JavaScript array of images generated from Python
            </script>
            """
        
    html_content += """
    </main>   
    <footer>
        <div class="footer-container">
            <p>
                Skyline High School<br>
                <address>
                    2552 North Maple Road<br>
                    Ann Arbor, MI 48103<br>
                </address>
            </p>
        
            <p>
                <a href = "https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home">XC Skyline Page</a><br>
                Follow us on Instagram
                <a href = "https://www.instagram.com/a2skylinexc/" aria-label="Instagram"><i class="fa-brands fa-instagram"></i>
                </a> 
            </p>

            <p>&copy 2024 Skyline High School. All rights reserved.</p>
        </div>
    </footer>
    
    <script src="../js/meet.js"></script>
    
    </body>
</html>
"""
    import re
    html_content = re.sub(r'<time>', '<span class="time">', html_content)
    html_content = re.sub(r'</time>', '</span>', html_content)

    # Save HTML content to a file in the meets folder
    with open(html_filename, 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(html_content)

    print(f"HTML file '{html_filename}' created successfully.")

    # except Exception as e:
    #     print(f"Error processing file: {e}")

def process_meet_files():
    # Set the meets folder path
    meets_folder = os.path.join(os.getcwd(), "meets")
    
    # Search for all CSV files in the meets folder
    csv_files = [f for f in os.listdir(meets_folder) if f.endswith('.csv')]
    
    if not csv_files:
        print(f"No CSV files found in folder: {meets_folder}")
        return

    # Process each CSV file in the meets folder
    for csv_file in csv_files:
        csv_file_path = os.path.join(meets_folder, csv_file)
        csv_to_html(csv_file_path, meets_folder)




import re
import os
import random

# Step 1: Extract the meet ID from the URL
def extract_meet_id(url):
    # Regex to extract the meet ID, which is the number right after '/meet/'
    match = re.search(r"/meet/(\d+)", url)
    print(f"The meet id is {match}")
    if match:
        print(f"REturning {match.group(1)}")
        return match.group(1)
    else:
        raise ValueError("Meet ID not found in URL.")

# Step 2: Select 10 random photos from the folder
def select_random_photos(folder_path, num_photos=10):
     # List all image files in the folder
    print(f"Checking {folder_path}")
    all_files = os.listdir(folder_path)
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Ensure we have enough images to select
    if len(image_files) < num_photos:
        return []
        raise ValueError(f"Not enough images in the folder. Found {len(image_files)} images.")
    
    # Select 10 random images
    return random.sample(image_files, num_photos)

# Step 3: Generate HTML image tags
def generate_image_tags(image_files):
    img_tags = []
    for img in image_files:
        # Use html.escape to handle special characters, including spaces
        img_path_escaped = html.escape(img)
        img_tags.append(f'{img_path_escaped}')
    return img_tags

# Putting it all together
def create_meet_image_gallery(url):
    meet_id = extract_meet_id(url)
    # Define the folder path for images based on the meet ID
    folder_path = f'images/meets/{meet_id}/'

    # print(f"The folder path is {folder_path}")
    
    if not os.path.exists(folder_path):
        return "Waiting for updating photo gallery for this meet."
        raise FileNotFoundError(f"The folder {folder_path} does not exist.")
    
    # Select 15 random photos
    selected_photos = select_random_photos(folder_path)
    
    # Generate image tags
    html_image_tags = generate_image_tags(selected_photos)
    
    print("List of images:", html_image_tags)  # Print the sorted list of images
    
    return html_image_tags

# Example usage
# url = "https://www.athletic.net/CrossCountry/meet/235827/results/943367"
# html_gallery = create_meet_image_gallery(url)
# print(html_gallery)


if __name__ == "__main__":
    # Check if meets folder exists
    meets_folder = os.path.join(os.getcwd(), "meets")
    if not os.path.exists(meets_folder):
        print(f"Folder '{meets_folder}' does not exist.")
    else:
        process_meet_files()
