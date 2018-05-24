

document.getElementById('UpdateSEOTitleButt').addEventListener("click", function (ev) {
            var vstrSelector = "SEOTitle";
            var vstrSEOTitle = document.getElementById('strSEOTitle').value;
            var dataString = '&vstrSelector=' + vstrSelector + '&vstrSEOTitle=' + vstrSEOTitle;
            $.ajax({
                type: "get",
                url: "/affiliates/landingpage",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SEOTitleINFDIv').html(html)
                }
            });
});