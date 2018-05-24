

var thisSendMessageButt = document.getElementById('SendMessageButt');
thisSendMessageButt.addEventListener("click", function () {
          var vstrNames = document.getElementById('strNames').value;
          var vstrEmail = document.getElementById('strEmail').value;
          var vstrCell = document.getElementById('strCell').value;
          var vstrSubject = document.getElementById('strSubject').value;
          var vstrMessage = document.getElementById('strMessage').value;


            var dataString  = '&vstrNames=' + vstrNames +  '&vstrEmail=' + vstrEmail + '&vstrCell='+ vstrCell + '&vstrSubject=' + vstrSubject +
                    '&vstrMessage=' + vstrMessage;
              $.ajax({
                    type: "post",
                    url: "/contact",
                    data: dataString,
                    cache: false,
                  success: function(html){
                    $('#MessageDivINF').html(html)

                  }
              });
});