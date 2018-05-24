

document.getElementById('MaxLoanButt').addEventListener("click", function (ev) {

            var vstrMyLoanLimit = document.getElementById('strMyLoanLimit').value;
            var vstrLoanReference = document.getElementById('strLoanReference').value;

            var dataString = '&vstrMyLoanLimit=' + vstrMyLoanLimit + '&vstrLoanReference=' + vstrLoanReference;

            var sendToURL = "/p2ploans/availableloans/" + vstrLoanReference;

            $.ajax({
                type: "post",
                url: sendToURL,
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#MaxLoanDIVInf').html(html)
                }
            });
});

document.getElementById('RequestLoanLimitIncreaseButt').addEventListener("click", function (ev) {

            var dataString = "1";

            var sendToURL = "/p2ploans/loanlimit";

            $.ajax({
                type: "get",
                url: sendToURL,
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#MaxLoanDIVInf').html(html)
                }
            });
});