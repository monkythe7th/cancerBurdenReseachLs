function toggleDisabled(flag) {
    let cls = document.getElementsByClassName('previous__screening');
    if (flag) Array.prototype.forEach.call(cls, (item) => item.style.display = 'inline-block' );
    else Array.prototype.forEach.call(cls, (item) => item.style.display = 'None');
}

function calcAge(params) {
    let dob = document.getElementById('dob');
    let age = document.getElementById('age');
    // ToDo: calculate the age or date of birth.
}