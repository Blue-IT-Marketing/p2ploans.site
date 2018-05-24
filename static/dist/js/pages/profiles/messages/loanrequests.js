


document.getElementById('SendButt').addEventListener("click", function (ev) {
            var vstrReference = document.getElementById('vstrReference').value;

            var vstrSubject = document.getElementById('strSubject').value;
            var vcomposetextarea = document.getElementById('composetextarea').value;



            var sendToURL = "/p2ploans/financiers/messages";
            var dataString = '&vstrSubject=' + vstrSubject + '&vcomposetextarea=' + vcomposetextarea + '&vstrReference=' + vstrReference;

            $.ajax({
                type: "post",
                url: sendToURL,
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#MessagingINFDIV').html(html)
                }
            });
});

document.getElementById('DiscardButt').addEventListener("click", function (ev) {
            document.getElementById('composetextarea').value = "";
            document.getElementById('strSubject').value = "";

            var thisHtml = "Message Discarded";
            $('#MessagingINFDIV').html(thisHtml);
});