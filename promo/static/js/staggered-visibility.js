const visElements = document.querySelectorAll('.clip-item, .fade-up-item, .fade-left-item, .progress-progress');
const visibleClass = 'is-visible';
const stagger = 175;
const visProcessable = [];
let visIsProcessing = false;
const visIntercept = (entries, observer) => {
    entries.forEach( (entry) =>  {
        if(entry.isIntersecting) {
            const elem = entry.target;
            visProcessable.push(elem);
        }
    });
    if(visIsProcessing || visProcessable.length === 0 ) return;
    processBatch();
    
}

const processBatch = () => {
    visIsProcessing = true;

    for(let i = 0; i < visProcessable.length; i++) {
        const pr = visProcessable[i];
        let itemStagger = 0 + (stagger * i) ;
        setTimeout(() => {
            visProcessElem(pr, observer);
            
        } ,itemStagger)
    }
    visIsProcessing = false;
}
const visProcessElem = (elem, observer) => {
    
    observer.unobserve(elem);
    elem.classList.add(visibleClass);
    visProcessable.splice(visProcessable.indexOf(elem), 1);
}
visOptions = {
    root: null,
    rootMargin: "0px 0px -100px 0px",
    scrollMargin: "",
    threshold: .15,
};

const observer = new IntersectionObserver(visIntercept, visOptions);
console.log(visElements);
visElements.forEach(elem => {
    observer.observe(elem);
})