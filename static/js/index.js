function showLogin(){
    document.querySelector('.login-wrapper').style.display = "flex"
    document.querySelector('.signup-wrapper').style.display = "none"
    document.querySelector('.shop-wrapper').style.display = "none"
}

function closeLogin(){
    document.querySelector('.login-wrapper').style.display = "none"
}


function showSignup(){
    document.querySelector('.login-wrapper').style.display = "none"
    document.querySelector('.signup-wrapper').style.display = "flex"
    document.querySelector('.shop-wrapper').style.display = "none"
}

function closeSignupShop(){
    document.querySelector('.login-wrapper').style.display = "none"
    document.querySelector('.signup-wrapper').style.display = "none"
    document.querySelector('.shop-wrapper').style.display = "none"
}

function closeSignup(){
    document.querySelector('.signup-wrapper').style.display = "none"
}

function showSignupShopkeeper(){
    document.querySelector('.login-wrapper').style.display = "none"
    document.querySelector('.signup-wrapper').style.display = "none"
    document.querySelector('.shop-wrapper').style.display = "flex"
}

function setProfilePic(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            // document.querySelector('.profile-pic').style.display = "flex"
            // document.querySelector('.profile-pic-name').textContent = input.value.replace("C:\\fakepath\\","")
            $('.imageMed')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }

    
}