


document.getElementById('AffiliateLinkButt').addEventListener("click", function (ev) {
            var strSelector = "Link";
            var dataString = '&vstrSelector=' + strSelector;
            $.ajax({
                type: "post",
                url: "/affiliates/settings",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SettingsINFDiv').html(html)
                }
            });
});
document.getElementById('SEOTitleButt').addEventListener("click", function (ev) {
            var strSelector = "SEOTitle";
            var dataString = '&vstrSelector=' + strSelector;
            $.ajax({
                type: "post",
                url: "/affiliates/settings",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SettingsINFDiv').html(html)
                }
            });
});
document.getElementById('SEODescriptionButt').addEventListener("click", function (ev) {
            var strSelector = "SEODescription";
            var dataString = '&vstrSelector=' + strSelector;
            $.ajax({
                type: "post",
                url: "/affiliates/settings",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SettingsINFDiv').html(html)
                }
            });
});
document.getElementById('LPHeadingButt').addEventListener("click", function (ev) {
            var strSelector = "LPHeading";
            var dataString = '&vstrSelector=' + strSelector;
            $.ajax({
                type: "post",
                url: "/affiliates/settings",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SettingsINFDiv').html(html)
                }
            });
});
document.getElementById('LPIntroButt').addEventListener("click", function (ev) {
            var strSelector = "LPIntro";
            var dataString = '&vstrSelector=' + strSelector;
            $.ajax({
                type: "post",
                url: "/affiliates/settings",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SettingsINFDiv').html(html)
                }
            });
});
document.getElementById('LPBodyButt').addEventListener("click", function (ev) {

            var strSelector = "LPBody";
            var dataString = '&vstrSelector=' + strSelector;
            $.ajax({
                type: "post",
                url: "/affiliates/settings",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SettingsINFDiv').html(html)
                }
            });
});
document.getElementById('LPFooterButt').addEventListener("click", function (ev) {
            var strSelector = "LPFooter";
            var dataString = '&vstrSelector=' + strSelector;
            $.ajax({
                type: "post",
                url: "/affiliates/settings",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SettingsINFDiv').html(html)
                }
            });
});
document.getElementById('CreateDefaultLandingPageButt').addEventListener("click", function (ev) {
            var dataString = '1';
            $.ajax({
                type: "post",
                url: "/affiliates/landingpage",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SettingsINFDiv').html(html)
                }
            });
});