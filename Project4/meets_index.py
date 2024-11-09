import csv
import os
import urllib.parse

def generate_homepage(csv_filename, folder_path, html_filename):
    # Initialize HTML content
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Skyline Cross Country</title>
<link rel="stylesheet" href="css/reset.css">
<link rel="stylesheet" href="css/style.css">
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
            <img src="images/skylineeagle.jpg" alt="Skyline Eagles Logo" class="nav-logo">
        </div>
        
        <!-- Side menu for small screens (hidden by default) -->
        <div class="side-menu">
            <ul>
                <li><a href="index.html" tabindex="0">Home Page</a></li>
                <li><a href="#about" tabindex="0">About Us</a></li>
                <li><a href="#meets" tabindex="0">Our Meets</a></li>
                <li><a href="#gallery" tabindex="0">Photo Gallery</a></li>
            </ul>
        </div>
        <div class="overlay"></div> <!-- Background overlay -->
    </nav>
   
    <header class="index" tabindex="0">
        <h1>Skyline Cross Country</h1>
        <h2>Striving for Excellence, Race by Race</h2>
    </header>
    
    <main id = "main">
        <!-- About Section -->
        <section id="about" tabindex="0">
            <div class="section-header">
                <h2><i class="fas fa-sticky-note"></i> About Us</h2>
                <button class="toggle-button" aria-expanded="true" data-section="Summary">Hide Summary</button>
            </div>
            <div class="collapsible-content open">
                <div class="summary-container" tabindex="0"> 
                    <p>
                        <b>Welcome to the website of the Ann Arbor Skyline Cross Country team!</b> 
                    </p>
                    
                    <p>
                        Our team is built on a tradition of <b>dedication</b>, <b>perseverance</b>, and <b>sportsmanship</b>. Whether you're a current <b>athlete</b>, an <b>alumni</b>, or a <b>fan of cross country</b>, Skyline Cross Country has a proud history of <b>competitive success</b> and <b>personal growth</b>. We aim to foster a <b>supportive environment</b> where every athlete can strive for their <b>personal best</b>, while contributing to the <b>success of the team</b>.
                    </p>
                    
                    <p>
                        This website is your go-to resource for <b>all things Skyline Cross Country</b>. Here, you can explore the <b>meets Skyline attends</b>, check out <b>detailed team and individual results</b> from past competitions, and relive key moments through our <b>photo gallery</b>. Whether you're following a specific meet or looking for <b>past performances</b>, we've made it easy to navigate through the rich history of </b>Skyline's cross country achievements</b>. Stay updated with the <b>latest team news</b>, explore <b>athlete spotlights</b>, and celebrate the journey of <b>Skyline Cross Country</b>.          
                    </p>
                </div> 
            </div>
        </section>
        """
        
    html_content += """

        <!-- Meets Section -->
        <section id = "meets" tabindex="0">
            <div class="section-header">
                <h2><i class="fas fa-running"></i> Our Meets</h2>
                <button class="toggle-button" aria-expanded="true" data-section="Meets">Hide Meets</button>
            </div>
            
            <div class="collapsible-content open">
                <div class="table-container">
                    <table>
                        <tr>
                            <th>Date</th>
                            <th>Meet</th>
                            <th>Place</th>
                            <th>Score</th>
                        </tr>
    """
                        
    # Open the CSV file and read the data
    with open(csv_filename, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        # Loop through the rows of the CSV (starting from the third row to skip headers)
        for row in rows[2:]:
            date = row[0]
            meet_name = row[1]
            category = row[2]
            place = row[3]
            score = row[4]
            html_file = row[6]  # The HTML file for the meet link

            # Add a table row for each entry in the CSV, with the meet name as a clickable link
            html_content += f"""
                    <tr>
                        <td>{date}</td>
                        <td><a href="meets/{encode_filename(html_file)}">{meet_name}</a></td>
                        <td>{place}</td>
                        <td>{score}</td>
                    </tr>
            """
        # Close the HTML structure
       
    html_content += """
                    </table>
                </div>
            </div>
        </section>
    """
    # Convert Python list of images to a JavaScript array format
    js_image_array = f"const images = {image_list};"
    
    # Get the list of images from the folder
    image_list = generate_image_list(folder_path)
    
    html_content +="""
        <!-- Gallery Section -->
        <section id = "gallery" tabindex="0">
            <div class="section-header">
                <h2><i class="fas fa-camera"></i> Photo Gallery</h2>
                <button class="toggle-button" aria-expanded="true" data-section="Photos">Hide Photos</button>
            </div>
            
            <div class="collapsible-content open">
                <div class="gallery-container">
                    <div class="gallery-slide">
                    """
    html_content += f"""
                            <img id="gallery-image" src="images/team/{image_list[0]}" alt="Gallery Image">
                    """
    html_content += """
                    </div>
                    <button class="arrow left-arrow" onclick="prevImage()">&#10094;</button> <!-- Left arrow -->
                    <button class="arrow right-arrow" onclick="nextImage()">&#10095;</button> <!-- Right arrow -->
                </div>
            </div>
        </section>
        
        <script>
            {js_image_array}
        </script>
        """
        
    html_content += """   
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
    </main>
    
    <script src="js/meet.js"></script>
    
    </body>
    </html>
    """
    # Write the HTML content to the output file
    with open(html_filename, mode='w', encoding='utf-8') as htmlfile:
        htmlfile.write(html_content)

    print(f"HTML file generated: {html_filename}")

def generate_image_list(folder_path):
    images = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith((".jpg", ".jpeg", ".png")):
            images.append(file_name)
    images.sort()
    print("List of images:", images)  # Print the sorted list of images
    return images

def encode_filename(filename):
    return urllib.parse.quote(filename)

csv_filename = "skyline_team_results.csv"  # The CSV file containing the team results
html_filename = "index1.html"  # The output HTML file
folder_path = "images/team"
generate_homepage(csv_filename, folder_path, html_filename)