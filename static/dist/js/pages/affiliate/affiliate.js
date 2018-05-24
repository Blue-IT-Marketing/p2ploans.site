

document.getElementById('FullStatsButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/affiliates/fullstats",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#AffiliateDIVInf').html(html)
                }
            });
});


document.getElementById('MyAffiliatesButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/affiliates/myaffiliates",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#AffiliateDIVInf').html(html)
                }
            });
});

document.getElementById('RunPromotionsButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/affiliates/promos",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#AffiliateDIVInf').html(html)
                }
            });
});

document.getElementById('SubscriptionsButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/affiliates/subscriptions",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#AffiliateDIVInf').html(html)
                }
            });
});
document.getElementById('SettingsButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/affiliates/settings",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#AffiliateDIVInf').html(html)
                }
            });
});
document.getElementById('TransferFundToWalletButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/affiliates/transfertowallet",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#AffiliateDIVInf').html(html)
                }
            });
});
