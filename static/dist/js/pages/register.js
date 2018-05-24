


document.getElementById('ActivateButt').addEventListener("click", function (ev) {

            var vstrFirstName = document.getElementById('strFirstName').value;
            var vstrSurname = document.getElementById('strSurname').value;
            var vstrCellNumber = document.getElementById('strCellNumber').value;
            var vstrEmail = document.getElementById('strEmail').value;




            var dataString = '&vstrFirstName=' + vstrFirstName + '&vstrSurname=' + vstrSurname + '&vstrCellNumber=' + vstrCellNumber +
                '&vstrEmail=' + vstrEmail;
            $.ajax({
                type: "get",
                url: "/activate",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#ActivationDIVInf').html(html)
                }
            });
});

document.getElementById('ActivationCodeButt').addEventListener("click", function (ev) {
            var vstrActivationCode = document.getElementById('strActivationCode').value;
            var dataString = '&vstrActivationCode=' + vstrActivationCode;
            $.ajax({
                type: "post",
                url: "/activate/code",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#ActivationCodeINFDIV').html(html)
                }
            });
});