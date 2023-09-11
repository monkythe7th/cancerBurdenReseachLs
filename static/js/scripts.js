function toggleDisabled(flag) {
    let cls = document.getElementsByClassName('previous__screening');
    if (flag) Array.prototype.forEach.call(cls, (item) => item.style.display = 'inline-block' );
    else Array.prototype.forEach.call(cls, (item) => item.style.display = 'None');
}

calcAge = (dob) => {
    let age = 0;
    let today = new Date();
    // ToDo: calculate the age or date of birth.
    age = (today.getFullYear() - new Date(dob).getFullYear());
    return age.toFixed(0);
}

calcDob = (age) => {
    let dob = "";
    let year = new Date().getFullYear() - age;
    let date = new Date(year,0)
    console.log(date)
    dob = `${date.getFullYear()}-0${date.getMonth()+1}-0${date.getDate()}`
    return dob
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
    if (window.location.pathname.includes('update/p')) {
        $('#input__date').css('display','none')
        $('#national__identification__number').val(patientID).prop('disable',true);
    }

    if (window.location.pathname.includes('/update/')) {
        if (!window.location.pathname.endsWith('update/')) {
            let patient = window.location.pathname.substring(11)
            console.log(patient)
            $('#patient_id').val(patient)
        }
    }

    $('#dob').change(()=>{
        let dob = $('#dob').val();
        $('#age').val(calcAge(dob))
    });
    $('#age').change(()=>{
        let age = $('#age').val()
        if (age>0) {
            $('#dob').val(calcDob(age))
        }
    });

    $('#eye').hover(() => {
        $(this).toggleClass('showen').attr('src',eye)
        let type = $('#password').attr('type') === 'password' ? 'text' : 'password';
        $('#password').attr('type', type)
    })


})