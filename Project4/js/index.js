// JavaScript to handle the moon icon behavior
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");

    // Log a message to the console
    if (document.body.classList.contains("dark-mode")) {
        console.log("Dark mode is now enabled.");
    } else {
        console.log("Dark mode is now disabled.");
    }
}

// JavaScript to handle the hamburger and overlay behavior
// Select the relevant elements
const hamburger = document.querySelector(".hamburger");
const sideMenu = document.querySelector(".side-menu");
const overlay = document.querySelector(".overlay");
// const sideMenuLinks = document.querySelectorAll(".side-menu a");

// Function to open the menu
function openMenu() {
    sideMenu.classList.add("active");
    overlay.classList.add("active");
    console.log("Opening menu.");
}

// Function to close the menu
function closeMenu() {
    sideMenu.classList.remove("active");
    overlay.classList.remove("active");
    console.log("Closing menu.");
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


// Add event listener to overlay to close the menu when clicked
overlay.addEventListener("click", function () {
    closeMenu();
});

// Toggle menu when the hamburger icon is clicked or focused
hamburger.addEventListener("keydown", function(event) {
    if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        toggleMenu();
    }
});

// Manage focus events to automatically close menu if focus leaves both menu and hamburger
document.addEventListener("focusin", function(event) {
    const focusedOutsideMenu = !sideMenu.contains(event.target) && !hamburger.contains(event.target);
    if (focusedOutsideMenu && sideMenu.classList.contains("active")) {
        closeMenu();
    }
});

// JavaScript to toggle collapsible sections
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

let currentImageIndex = 0;
const galleryImage = document.getElementById("gallery-image");
const lightBoxImage = document.getElementById("lightbox-image");

// Function to show the next image
function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    showImage("right");
}

// Function to show the previous image
function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    showImage("left");
}

// Function to display the image with sliding animation
function showImage(direction) {
    galleryImage.classList.remove("active-slide", "slide-in-left", "slide-in-right");
    
    // Trigger a reflow to restart animation
    void galleryImage.offsetWidth;

    // Set the new image source
    galleryImage.src = `images/team/${images[currentImageIndex]}`;
    lightBoxImage.href = `images/team/${images[currentImageIndex]}`;

    // Add animation class based on direction
    galleryImage.classList.add(direction === "left" ? "slide-in-left" : "slide-in-right");

    // After animation, set it back to active position
    setTimeout(() => {
        galleryImage.classList.remove("slide-in-left", "slide-in-right");
        galleryImage.classList.add("active-slide");
    }, 500); // Duration should match CSS transition time
}

// Select all images on the page
document.querySelectorAll('img').forEach(img => {
    img.onerror = function() {
    this.onerror = null; // Prevents infinite loop if default image missing
    this.src = 'images/default_image.jpg';
    this.alt = "Default images"
    };
});

// lightbox.option({
//     'resizeDuration': 200,
//     'wrapAround': true
//   })