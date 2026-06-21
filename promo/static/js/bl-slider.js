 const blSlides = document.querySelectorAll('.bl-slide');
const blSelectors = document.querySelector('.bl-slide-selectors');
let blCurrentSlideIndex = 0;
const blTotalSlides = blSlides.length;
let blIsAnimating = false; 

let blInterval;
let blIncomingAnimTimeout;
let blCleanupTimeout;
let blOverlayTimeout;

function blInit() {
    for(let i = 0; i < blSlides.length; i++) {
        const text = blSlides[i].dataset.selectorText; 
        const button = document.createElement('button');
        button.dataset.slideIndex = i;
        button.innerText = text;
        button.addEventListener('click', () => blUserSelect(i));
        const listItem = document.createElement('li');
        listItem.classList.add('bl-slide-selector');
        listItem.appendChild(button);
        blSelectors.appendChild(listItem);
    }
    
    blFillSlideData(blSlides[blCurrentSlideIndex]);
    blStartAutoCycle(); // Extracted into a reusable function
}
blInit();

// Helper to reliably start/restart the automated slide changes
function blStartAutoCycle() {
    clearInterval(blInterval);
    blInterval = setInterval(() => {
        blShowNextSlide();
    }, 10000);
}

function blShowNextSlide(indexRequested = null) {
    if (blIsAnimating) return;
    blIsAnimating = true;

    const currentSlide = blSlides[blCurrentSlideIndex];
    
    // FIX 1: Explicitly determine which slide is next and what its index actually is
    let nextSlideIndex;
    if (indexRequested !== null) {
        nextSlideIndex = indexRequested;
    } else {
        nextSlideIndex = (blCurrentSlideIndex + 1) % blTotalSlides;
    }
    const nextSlide = blSlides[nextSlideIndex];
    
    // Phase 1: Prep next slide
    nextSlide.classList.add('slide__incoming');
    
    // Phase 2: Trigger animation frame
    // FIX 3: Fixed typo (Timout -> Timeout)
    blIncomingAnimTimeout = setTimeout(() => {
        nextSlide.classList.add('is-active');
        blFillSlideData(nextSlide);
    }, 50); 
    
    // Phase 3: Clean up using precise timing calculation
    // FIX 3: Fixed typo (Timout -> Timeout)
    blCleanupTimeout = setTimeout(() => {
        // Promote incoming slide to current
        nextSlide.classList.add('slide__current');
        nextSlide.classList.remove('slide__incoming', 'is-active');
        
        // Demote old slide if it's different from the new slide
        if (currentSlide !== nextSlide) {
            currentSlide.classList.remove('slide__current');
        }
        
        // FIX 1: Correctly track our new position based on what was rendered
        blCurrentSlideIndex = nextSlideIndex;
        blIsAnimating = false;
    }, 900); 
}

function blFillSlideData(slideElem) {
    clearTimeout(blOverlayTimeout); // Clear old overlay timeouts to prevent erratic fading

    const title = slideElem.dataset.title;
    const subtitle = slideElem.dataset.subtitle;
    const paragraph = slideElem.dataset.text;
    const overlay = document.querySelector('.bl-slide-overlay');
    const titleElem = overlay.querySelector('h2');
    const subtElem = overlay.querySelector('span');
    const paraElem = overlay.querySelector('p');
    
    titleElem.innerText = title; 
    subtElem.innerText = subtitle; 
    paraElem.innerText = paragraph;
    
    const overlayContent = overlay.querySelector('.bl-slide-content');
    overlayContent.classList.add('is-active');
    
    blOverlayTimeout = setTimeout(() => {
        overlayContent.classList.remove('is-active');
    }, 9000);
}

function blUserSelect(slideIndex) {
    // If the user selects the slide they are already looking at, do nothing
    if (slideIndex === blCurrentSlideIndex) return;

    // Force unlock state if mid-animation to allow immediate click responsiveness
    blIsAnimating = false; 

    // Clear everything actively running
    clearInterval(blInterval);
    clearTimeout(blIncomingAnimTimeout);
    clearTimeout(blCleanupTimeout);
    clearTimeout(blOverlayTimeout);
    
    blIncomingAnimTimeout = null;
    blCleanupTimeout = null;
    blInterval = null;
    blOverlayTimeout = null;
    
    // Reset classes clean slate
    for(let i = 0; i < blSlides.length; i++) {
        blSlides[i].classList.remove('slide__incoming', 'is-active');
    }
    
    const overlay = document.querySelector('.bl-slide-overlay');
    const overlayContent = overlay.querySelector('.bl-slide-content');
    overlayContent.classList.remove('is-active');
    
    setTimeout(() => {
        blShowNextSlide(slideIndex);
        blStartAutoCycle(); // FIX 2: Restart the 7-second timer loop for uninterrupted auto-play
    }, 200);
}