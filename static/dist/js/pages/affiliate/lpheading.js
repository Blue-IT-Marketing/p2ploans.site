

document.getElementById('LPHeadingButts').addEventListener("click", function (ev) {
            var vstrSelector = "LPHeading";
            var vstrLPHeading = document.getElementById('strLPHeading').value;
            var dataString = '&vstrSelector=' + vstrSelector + '&vstrLPHeading=' + vstrLPHeading;
            $.ajax({
                type: "get",
                url: "/affiliates/landingpage",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#LPHeadingINFDivision').html(html)
                }
            });
});