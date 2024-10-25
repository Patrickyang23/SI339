import csv
import os

def generate_homepage():
    # Initialize HTML content
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Skyline Cross Country</title>
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
        <img src="../images/skylineeagle.jpg" alt="Skyline Eagles Logo" class="nav-logo">
        
        <!-- Side menu for small screens (hidden by default) -->
        <div class="side-menu">
            <ul>
                <li><a href="index.html" tabindex="0">Home Page</a></li>
                <li><a href="#about" tabindex="0">Summary</a></li>
                <li><a href="#meets" tabindex="0">Team Results</a></li>
                <li><a href="#performance" tabindex="0">Individual Results</a></li>
                <li><a href="#gallery" tabindex="0">Photo Gallery</a></li>
            </ul>
        </div>
        <div class="overlay"></div> <!-- Background overlay -->
   </nav>
   
    <!-- JavaScript to handle the hamburger and overlay behavior -->
    <script>
        // Select the relevant elements
        const hamburger = document.querySelector(".hamburger");
        const sideMenu = document.querySelector(".side-menu");
        const overlay = document.querySelector(".overlay");
        const sideMenuLinks = document.querySelectorAll(".side-menu a");

        // Function to open the menu
        function openMenu() {
            sideMenu.classList.add("active");
            overlay.classList.add("active");
        }

        // Function to close the menu
        function closeMenu() {
            sideMenu.classList.remove("active");
            overlay.classList.remove("active");
        }
        
        // Function to toggle menu visibility
        function toggleMenu() {
            const isActive = sideMenu.classList.contains("active");
            if (isActive) {
                closeMenu();
            } else {
                openMenu();
            }
        }

        // Toggle menu when clicking the hamburger icon
        hamburger.addEventListener("click", function () {
            toggleMenu();
        });

        // Automatically open the menu when the hamburger icon is focused
        hamburger.addEventListener("focus", function () {
            openMenu();
        });

        // Add focus listeners to each link in the side menu
        sideMenuLinks.forEach(function (link) {
            link.addEventListener("focus", function () {
                openMenu();
            });
        });

        // Add focusout event listener to the side menu and hamburger icon to detect when focus leaves
        document.addEventListener("focusin", function (event) {
            // Check if the newly focused element is outside both the side menu and the hamburger icon
            if (
                !sideMenu.contains(event.target) &&
                !hamburger.contains(event.target)
            ) {
                closeMenu();
            }
        });
        
        // Add event listener to overlay to close the menu when clicked
        overlay.addEventListener("click", function () {
            closeMenu();
        });
    </script>
   
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
                <div class="summary-container">
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

        <!-- Meets Section -->
        <section id = "meets" tabindex="0">
            <div class="section-header">
                <h2><i class="fas fa-camera"></i> Our Meets</h2>
                <button class="toggle-button" aria-expanded="true" data-section="Meets">Hide Meets</button>
            </div>
            
            <div class="collapsible-content open">
                <div class="meets-container">
                </div>
            </div>
        </section>
        
        <!-- Gallery Section -->
        <section id = "gallery" tabindex="0">
            <div class="section-header">
                <h2><i class="fas fa-camera"></i> Photo Gallery</h2>
                <button class="toggle-button" aria-expanded="true" data-section="Gallery">Hide Gallery</button>
            </div>
            
            <div class="collapsible-content open">
                <div class="gallery-container">
                </div>
            </div>
        </section>
        """
    html_content += """
    <!-- JavaScript to toggle collapsible sections -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const toggleButtons = document.querySelectorAll('.toggle-button');

            toggleButtons.forEach(toggleButton => {
                const sectionName = toggleButton.getAttribute('data-section');
                const collapsibleContent = toggleButton.closest('.section-header').nextElementSibling;

                toggleButton.addEventListener('click', function() {
                    const isExpanded = toggleButton.getAttribute('aria-expanded') === 'true';
                    toggleButton.setAttribute('aria-expanded', !isExpanded);

                    // Update the button text based on the section
                    if (isExpanded) {
                        toggleButton.textContent = `Show ${sectionName}`;
                        collapsibleContent.classList.remove('open');
                    } else {
                        toggleButton.textContent = `Hide ${sectionName}`;
                        collapsibleContent.classList.add('open');
                    }
                });
            });
        });
    </script>
    """
    html_content += """   
    </main>
    </body>
    </html>
    """
    return html_content

def main():
    # Generate the full HTML content
    html_content = generate_homepage()
    
    # Write the HTML content to an output file
    with open("index.html", "w") as file:
        file.write(html_content)
    print("HTML file generated successfully!")

# Run the main function
if __name__ == "__main__":
    main()