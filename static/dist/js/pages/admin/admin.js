

document.getElementById('ProfilesButt').addEventListener("click", function (ev) {
            var sendToURL = "/admin/profiles";
            var dataString = "1";
            $.ajax({
                type: "get",
                url: sendToURL,
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#AdminINFDIV').html(html)
                }
            });
});

document.getElementById('WithdrawalsButt').addEventListener("click", function (ev) {
            var sendToURL = "/admin/withdrawals";
            var dataString = "1";
            $.ajax({
                type: "get",
                url: sendToURL,
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#AdminINFDIV').html(html)
                }
            });
});

document.getElementById('MessagingButt').addEventListener("click", function (ev) {
            var sendToURL = "/admin/messaging";
            var dataString = "1";
            $.ajax({
                type: "get",
                url: sendToURL,
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#AdminINFDIV').html(html)
                }
            });
});