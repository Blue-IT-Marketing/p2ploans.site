document.getElementById(('SEODescriptionButts')).addEventListener("click", function (ev) {
            var vstrSelector = "SEODescription";
            var vstrSEODescription = document.getElementById('strSEODescription').value;
            var dataString = '&vstrSelector=' + vstrSelector + '&vstrSEODescription=' + vstrSEODescription;
            $.ajax({
                type: "get",
                url: "/affiliates/landingpage",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SEODescriptionINFDiv').html(html)
                }
            });
});