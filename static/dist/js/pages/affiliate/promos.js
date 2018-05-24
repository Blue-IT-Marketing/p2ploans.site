

document.getElementById('EnablePriorityButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/affiliates/enablepriority",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#PromotionsINFDiv').html(html)
                }
            });
});
document.getElementById('DisablePriorityListingButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "post",
                url: "/affiliates/enablepriority",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#PromotionsINFDiv').html(html)
                }
            });
});
document.getElementById('EnableAutoDownLineButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/affiliates/enableautodownline",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#PromotionsINFDiv').html(html)
                }
            });
});
document.getElementById('DisableAutoDownLineButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "post",
                url: "/affiliates/enableautodownline",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#PromotionsINFDiv').html(html)
                }
            });
});
document.getElementById('EnableSocialMediaButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/affiliates/enablesocialmedia",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#PromotionsINFDiv').html(html)
                }
            });
});

document.getElementById('DisableSocialMediaButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "post",
                url: "/affiliates/enablesocialmedia",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#PromotionsINFDiv').html(html)
                }
            });
});
document.getElementById('CreatePostButton').addEventListener("click", function (ev) {
            var vstrGraphApiKey = document.getElementById('strGraphApiKey').value;
            var vstrFacebookPost = document.getElementById('strFacebookPost').value;
            var vstrGroupIDs = document.getElementById('strGroupIDs').value;



            var dataString = '&vstrGraphApiKey=' + vstrGraphApiKey + '&vstrFacebookPost='+ vstrFacebookPost + '&vstrGroupIDs=' + vstrGroupIDs;
            $.ajax({
                type: "get",
                url: "/social/facebook/groups",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#FacebookPostINFDiv').html(html)
                }
            });

});
