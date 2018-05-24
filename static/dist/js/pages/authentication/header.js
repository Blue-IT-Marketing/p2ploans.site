
  // Initialize Firebase
var config = {
    apiKey: "AIzaSyBhNkqMr7zXi4r_bToSFiqPQ8BQLja47_g",
    authDomain: "sa-sms-b.firebaseapp.com",
    databaseURL: "https://sa-sms-b.firebaseio.com",
    projectId: "sa-sms-b",
    storageBucket: "sa-sms-b.appspot.com",
    messagingSenderId: "3221236137"
  };
if (!firebase.apps.length) {
    firebase.initializeApp(config);
}else {
}

function sendEmailVerification() {
  // [START sendemailverification]
  firebase.auth().currentUser.sendEmailVerification().then(function() {
    // Email Verification sent!
    // [START_EXCLUDE]
    alert('Email Verification Sent!');
    // [END_EXCLUDE]
  });
  // [END sendemailverification]
}





initApp = function() {
    firebase.auth().onAuthStateChanged(function(user) {
          if (user) {
            // User is signed in.
            var displayName = user.displayName;
            var email = user.email;
            var emailVerified = user.emailVerified;
            var photoURL = user.photoURL;
            var uid = user.uid;

            var phoneNumber = user.phoneNumber;
            var providerData = user.providerData;
            user.getIdToken().then(function(accessToken) {
              //document.getElementById('SingInButton').textContent = 'Signed in';
              document.getElementById('SingInButton').textContent = 'Sign out';
              document.getElementById('SingInButton').setAttribute('href','/logout');
              document.getElementById('strUserNameID').textContent = displayName;
              document.getElementById('strUserImageID').src =photoURL;
              document.getElementById('strMainUserImageID').src = photoURL;
              document.getElementById('strAccountDetails').textContent = JSON.stringify({
                displayName: displayName,
                email: email,
                emailVerified: emailVerified,
                phoneNumber: phoneNumber,
                photoURL: photoURL,
                uid: uid,

                accessToken: accessToken,
                providerData: providerData
              }, null, '  ');
              //Send the User Token to the backend with ajax at this point with a sign in instruction
                var vstrChoice = 2;
                if (emailVerified === true){
                    emailVerified = "YES"
                }else{
                    emailVerified = "NO"
                }
                var dataString ='&vstrChoice=' + vstrChoice + '&vstrDisplayName=' + displayName + '&vstrEmail=' + email +
                        '&vstremailVerified=' + emailVerified + '&vstrUserID=' + uid + '&vstrPhoneNumber=' + phoneNumber +
                        '&vstrProviderData=' + providerData + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/login",
                    data: dataString,
                    cache: false,
                    success: function(data){
                        $('#loginINFDIV').html(data)
                    }});
            });
          } else {
            // User is signed out.
            //document.getElementById('sign-in-status').textContent = 'Signed out';
            document.getElementById('SingInButton').textContent = 'Sign in';
            document.getElementById('strAccountDetails').textContent = 'null';
            //Send the User Token to the backend at this stage using ajax with instructions to logout the user
            var dataString = document.getElementById('account-details').value;
            $.ajax({
                type: "post",
                url: "/logout",
                data: dataString,
                cache: false,
                success: function(data){
                    $('#logoutinfDIV').html(data)
                }});
          }
        }, function(error) {
          console.log(error);
        });
      };
initApp();




