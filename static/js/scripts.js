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

postRecord = (page) => {
    let post_url = window.location.origin + '/ui/post_record?save=' + page;
    fetch(post_url, {
        method: 'POST', 
        redirect: 'follow'
    }).then(response => {
        if (response.redirected) {
            window.location = response.url
        }
    })
}

editRecord = () => {
    let post_url = window.location.origin + '/ui/';
    fetch(post_url, {
        method: 'POST',
        redirect: 'follow'
    }).then(response => {
        if (response.redirected) {
            window.location = response.url
        }
    })
}

$(document).ready(()=>{
    $('#input__date').css('display','none')
    if (window.location.pathname.includes('update/p'))
        $('#national__identification__number').val(patientID).prop('disable',true);

    if (window.location.pathname.includes('/update/')) {
        if (!window.location.pathname.endsWith('update/')) {
            let patient = window.location.pathname.substring(11)
            console.log(patient)
            $('#patient_id').val(patient)
        }
    }
})