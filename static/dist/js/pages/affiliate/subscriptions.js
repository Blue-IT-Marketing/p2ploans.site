


document.getElementById('AutoRenewAffiliateButt').addEventListener("click", function (ev) {
            var vstrAutoRenewDate = document.getElementById('strAutoRenewDate').value;

            var vstrChoice = "Affiliate";

            var dataString = '&vstrAutoRenewDate=' + vstrAutoRenewDate + '&vstrChoice=' + vstrChoice;
            $.ajax({
                type: "post",
                url: "/affiliates/subscriptions",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SubscriptionsINFDiv').html(html)
                }
            });
});
document.getElementById('AutoRenewPromosButt').addEventListener("click", function (ev) {
            var vstrAutoRenewDate = document.getElementById('strAutoRenewDate').value;

            var vstrChoice = "Promo";

            var dataString = '&vstrAutoRenewDate=' + vstrAutoRenewDate + '&vstrChoice=' + vstrChoice;
            $.ajax({
                type: "post",
                url: "/affiliates/subscriptions",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SubscriptionsINFDiv').html(html)
                }
            });
});