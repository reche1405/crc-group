const quicktab = document.querySelector('.quicktabs-wrapper');
const qtabs = quicktab.querySelectorAll('.tab-selector'); 
const qtabDetails = quicktab.querySelector('.tab-detail-wrapper');
console.log('Hi from the quicktabs');


const qtabHandlePress = (e) => {
    target = e.target;
    if(typeof(e.target) != 'BUTTON') {
        target = e.target.closest('button');
    }
    
    const data = quickTabExtract(target.closest('.tab-selector'));
    const para = qtabDetails.querySelector('p');
    const list = qtabDetails.querySelector('ul');
    const spans = list.querySelectorAll('span');
    para.innerText = data.text;
    for (let i = 0; i < spans.length; i++) {
        spans[i].innerText = data.reasons[i];
    }
    setActive(target.closest('.tab-selector'));

}

const quickTabExtract = (selector) => {
    const data = {};
    console.log(selector.dataset.text);
    data.text = selector.dataset.text;
    data.reasons = selector.dataset.reasons.split('|');
    console.log(data);
    return data; 
}

const setActive = (button) => {
    for (let i = 0; i < qtabs.length; i++) {
        qtabs[i].classList.remove('is-active');
    }
    button.closest('.tab-selector').classList.add('is-active');

}


for (let i = 0; i < qtabs.length; i++) {
    const button = qtabs[i].querySelector('button');
    console.log(button);
    button.addEventListener('click', qtabHandlePress);
    
}
