

document.getElementById('ComposeResponseButt').addEventListener("click", function (ev) {
            var sendToURL = "/admin/messaging";
            var dataString = "1";
            $.ajax({
                type: "post",
                url: sendToURL,
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#AdminINFDIV').html(html)
                }
            });
});
