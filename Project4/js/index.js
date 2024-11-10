// JavaScript to handle the moon icon behavior
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

// JavaScript to handle the hamburger and overlay behavior
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

lightbox.option({
    'resizeDuration': 200,
    'wrapAround': true
  })