try{
var config =
{
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
}catch (err){

}

var thisLogOutButton = document.getElementById("LogOutButton");
thisLogOutButton.addEventListener("click", signOut);
  function signOut()
  {
        firebase.auth().signOut().then(function() {
          console.log('Signed Out');
          alert("Successfully signed out");
          thisLogOutButton.disabled = true;
        }, function(error) {
          console.error('Sign Out Error', error);
        });
  }