function showLogin(){
    document.querySelector('.login-wrapper').style.display = "flex"
    document.querySelector('.signup-wrapper').style.display = "none"
    document.querySelector('.shop-wrapper').style.display = "none"
}


function closeLogin(){
    document.querySelector('.login-wrapper').style.display = "none"
}

function closeProfile(){
    document.querySelector('.profile-wrapper').style.display = "none"
}

function showProfile(){
    document.querySelector('.profile-wrapper').style.display = "flex"
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

function changeTab(num,element){
    if (num == 1){
        element.style.backgroundColor = "#07a44b"
        element.style.color = "white"
        element.style.border = "2px solid white"

        document.querySelector('.fr').style.backgroundColor = "white"
        document.querySelector('.fr').style.border = "2px solid rgba(230, 230, 230,0.5)"
        document.querySelector('.fr').style.color = "black"

        document.querySelector('.ve').style.backgroundColor = "white"
        document.querySelector('.ve').style.border = "2px solid rgba(230, 230, 230,0.5)"
        document.querySelector('.ve').style.color = "black"


        document.querySelector('.herb').style.display = "flex"
        document.querySelector('.fruit').style.display = "none"
        document.querySelector('.veg').style.display = "none"

    }
    else if(num == 2){
        element.style.backgroundColor = "#07a44b"
        element.style.color = "white"
        element.style.border = "2px solid white"

        document.querySelector('.he').style.backgroundColor = "white"
        document.querySelector('.he').style.border = "2px solid rgba(230, 230, 230,0.5)"
        document.querySelector('.he').style.color = "black"

        document.querySelector('.ve').style.backgroundColor = "white"
        document.querySelector('.ve').style.border = "2px solid rgba(230, 230, 230,0.5)"
        document.querySelector('.ve').style.color = "black"

        document.querySelector('.fruit').style.display = "flex"
        document.querySelector('.herb').style.display = "none"
        document.querySelector('.veg').style.display = "none"
    }
    else{
        element.style.backgroundColor = "#07a44b"
        element.style.color = "white"
        element.style.border = "2px solid white"

        document.querySelector('.fr').style.backgroundColor = "white"
        document.querySelector('.fr').style.border = "2px solid rgba(230, 230, 230,0.5)"
        document.querySelector('.fr').style.color = "black"

        document.querySelector('.he').style.backgroundColor = "white"
        document.querySelector('.he').style.border = "2px solid rgba(230, 230, 230,0.5)"
        document.querySelector('.he').style.color = "black"

        document.querySelector('.veg').style.display = "flex"
        document.querySelector('.fruit').style.display = "none"
        document.querySelector('.herb').style.display = "none"
    }
}

function changeTabPayment(num,element){
    if (num == 1){
        element.style.backgroundColor = "#07a44b"
        element.style.color = "white"
        element.style.border = "2px solid white"

        document.querySelector('.fr').style.backgroundColor = "white"
        document.querySelector('.fr').style.border = "2px solid rgba(230, 230, 230,0.5)"
        document.querySelector('.fr').style.color = "black"

        document.querySelector('.ve').style.backgroundColor = "white"
        document.querySelector('.ve').style.border = "2px solid rgba(230, 230, 230,0.5)"
        document.querySelector('.ve').style.color = "black"


        document.querySelector('.upi-pay').style.display = "flex"
        document.querySelector('.address').style.display = "none"
        document.querySelector('.debit').style.display = "none"

    }
    else if(num == 2){
        element.style.backgroundColor = "#07a44b"
        element.style.color = "white"
        element.style.border = "2px solid white"

        document.querySelector('.he').style.backgroundColor = "white"
        document.querySelector('.he').style.border = "2px solid rgba(230, 230, 230,0.5)"
        document.querySelector('.he').style.color = "black"

        document.querySelector('.ve').style.backgroundColor = "white"
        document.querySelector('.ve').style.border = "2px solid rgba(230, 230, 230,0.5)"
        document.querySelector('.ve').style.color = "black"

        document.querySelector('.address').style.display = "flex"
        document.querySelector('.upi-pay').style.display = "none"
        document.querySelector('.debit').style.display = "none"
    }
    else{
        element.style.backgroundColor = "#07a44b"
        element.style.color = "white"
        element.style.border = "2px solid white"

        document.querySelector('.fr').style.backgroundColor = "white"
        document.querySelector('.fr').style.border = "2px solid rgba(230, 230, 230,0.5)"
        document.querySelector('.fr').style.color = "black"

        document.querySelector('.he').style.backgroundColor = "white"
        document.querySelector('.he').style.border = "2px solid rgba(230, 230, 230,0.5)"
        document.querySelector('.he').style.color = "black"

        document.querySelector('.debit').style.display = "flex"
        document.querySelector('.upi-pay').style.display = "none"
        document.querySelector('.address').style.display = "none"
    }
}



function showNotifications(){
    document.querySelector('.notifications').style.display = "block"
}
function closeNotifications(){
    document.querySelector('.notifications').style.display = "none"
}

function showUpload(){
    document.querySelector('.upload-bill').style.display = "flex"
    document.getElementById('#style-2').overflowY = "hidden"
}

function closeUpload(){
    document.querySelector('.upload-bill').style.display = "none"
    document.getElementById('#style-2').overflowY = "scroll"
}

