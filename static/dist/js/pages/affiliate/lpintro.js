

document.getElementById('LPIntroButton').addEventListener("click", function (ev) {
            var vstrSelector = "LPIntro";
            var vstrLPIntro = document.getElementById('strLPIntro').value;
            var dataString = '&vstrSelector=' + vstrSelector + '&vstrLPIntro=' + vstrLPIntro;
            $.ajax({
                type: "get",
                url: "/affiliates/landingpage",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#LPIntroINFDivision').html(html)
                }
            });
});