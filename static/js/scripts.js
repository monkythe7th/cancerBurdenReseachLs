function toggleDisabled(flag) {
    let cls = document.getElementsByClassName('previous__screening');
    if(flag) Array.prototype.forEach.call(cls, (item) => item.removeAttribute('disabled') );
    else Array.prototype.forEach.call(cls, (item) => item.setAttribute('disabled',true));
}