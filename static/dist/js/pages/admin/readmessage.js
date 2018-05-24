

document.getElementById('SendButton').addEventListener("click", function (ev) {
            var vstrToEmail = document.getElementById('strToEmail').value;
            var vstrSubject = document.getElementById('strSubject').value;
            var vstrcomposetextarea = document.getElementById('composetextarea').value;
            var vstrMessageIndex = document.getElementById('strMessageIndex').value;


            var dataString = '&vstrToEmail=' + vstrToEmail + '&vstrSubject=' + vstrSubject +
                '&vstrcomposetextarea=' + vstrcomposetextarea + '&vstrMessageIndex=' + vstrMessageIndex;
            $.ajax({
                type: "post",
                url: "/admin/messaging",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#MessagingINFDiv').html(html)
                }
            });
});