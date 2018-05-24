

document.getElementById('UpdateFooterINFDivButt').addEventListener("click", function (ev) {
            var vstrSelector = "LPFooter";
            var vstrLPFooter = document.getElementById('strLPFooter').value;
            var dataString = '&vstrSelector=' + vstrSelector + '&vstrLPFooter=' + vstrLPFooter;
            $.ajax({
                type: "get",
                url: "/affiliates/landingpage",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#UpdateFooterInformationDivision').html(html)
                }
            });

});
