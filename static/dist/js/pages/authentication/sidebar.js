
  // Initialize Firebase
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

function initApp() {
  // Listening for auth state changes.
  // [START authstatelistener]
  firebase.auth().onAuthStateChanged(function(user) {
    // [START_EXCLUDE silent]

    // [END_EXCLUDE]
    if (user) {
      // User is signed in.
      var displayName = user.displayName;
      var email = user.email;
      var emailVerified = user.emailVerified;
      var photoURL = user.photoURL;
      var isAnonymous = user.isAnonymous;
      var uid = user.uid;
      var providerData = user.providerData;
      // [START_EXCLUDE]
      document.getElementById('strSideUserImageID').src =photoURL;
      document.getElementById('strSideUserNameID').textContent =displayName;

      if (!emailVerified) {
          var vstrChoice = 0;
          var dataString = "&vstrChoice=" + vstrChoice;
          $.ajax({
              type:"post",
              url: "/login",
              data: dataString,
              cache: false,
              success: function (SideBar) {
                  $('#SideBarMenu').html(SideBar);
              }
          })
      }else
          {
          var vstrChoice = 0;
          var dataString = "&vstrChoice=" + vstrChoice;
          $.ajax({
              type:"post",
              url: "/login",
              data: dataString,
              cache: false,
              success: function (SideBar) {
                  $('#SideBarMenu').html(SideBar);
              }
          })
          }
      // [END_EXCLUDE]
    } else
        {
      // User is signed out.
          var vstrChoice = 1;
          var dataString = "&vstrChoice=" + vstrChoice;
          $.ajax({
              type:"post",
              url: "/login",
              data: dataString,
              cache: false,
              success: function (SideBar) {
                  $('#SideBarMenu').html(SideBar);
              }
          })
    }
  });
}

initApp();

