

document.getElementById('UpdateLandingPageButts').addEventListener("click", function (ev) {
            var vstrSelector = "LPBody";
            var vstrLPBody = document.getElementById('strLPBody').value;
            var dataString = '&vstrSelector=' + vstrSelector + '&vstrLPBody=' + vstrLPBody;
            $.ajax({
                type: "get",
                url: "/affiliates/landingpage",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#LPBodyINFDiv').html(html)
                }
            });
});
