const imageMapPoints = document.querySelectorAll('.mapped-circle');
const mapInfoCard = document.querySelector('.mapped-info');
const handleClick = (e) => {
    clearMappedInfo();
    setMappedInfo(e.target.dataset);

}

const clearMappedInfo = () => {
    const text = mapInfoCard.querySelector('h4');
    const subtext = mapInfoCard.querySelector('span');
    text.innerText = "";
    subtext.innerText = "";
}

const setMappedInfo = (dataset) => {
    const text = mapInfoCard.querySelector('h4');
    const subtext = mapInfoCard.querySelector('span');
    text.innerText = dataset.text; 
    subtext.innerText = dataset.subtext;

}
for (let i = 0; i < imageMapPoints.length; i++) {
    const mapPoint = imageMapPoints[i];
        mapPoint.addEventListener('click', handleClick);
    
}