document.getElementById('SaveProfileButt').addEventListener("click", function (ev) {
            var vstrProfileName = document.getElementById('strProfileName').value;
            var vstrEmail = document.getElementById('strEmail').value;
            var vstrPayPalEmail = document.getElementById('strPayPalEmail').value;
            var vstrProfileIntroduction = document.getElementById('strProfileIntroduction').value;
            var vstrTermsCheck = document.getElementById('TermsCheck').value;

            var dataString = '&vstrProfileName=' + vstrProfileName + '&vstrEmail=' + vstrEmail + '&vstrPayPalEmail=' + vstrPayPalEmail +
                    '&vstrProfileIntroduction=' + vstrProfileIntroduction + '&vstrTermsCheck=' + vstrTermsCheck;

            $.ajax({
                type: "get",
                url: "/profiles/save",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SaveProfileINFDIV').html(html)
                }
            });
});

document.getElementById('LoadInboxButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/profiles/inbox",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#InboxDivInf').html(html)
                }
            });
});
document.getElementById('SaveSettingsButt').addEventListener("click", function (ev) {
            var vstrAutoTrade = document.getElementById('AutoTrade').value;
            var vstrAutoWithDraw = document.getElementById('AutoWithDraw').value;
            var vstrBussinessProfile = document.getElementById('BussinessProfile').value;

            var vstrSendNotifications = document.getElementById('SendNotifications').value;
            var vstrMakeProfilePrivate = document.getElementById('MakeProfilePrivate').value;
            var vstrMakeChatPrivate = document.getElementById('MakeChatPrivate').value;

            var dataString = '&vstrAutoTrade=' + vstrAutoTrade + '&vstrAutoWithDraw=' + vstrAutoWithDraw + '&vstrBussinessProfile=' +
                    vstrBussinessProfile + '&vstrSendNotifications=' + vstrSendNotifications +
                    '&vstrMakeProfilePrivate=' + vstrMakeProfilePrivate + '&vstrMakeChatPrivate=' + vstrMakeChatPrivate;
            $.ajax({
                type: "get",
                url: "/profiles/settings",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#SaveSettingsINFDIV').html(html)
                }
            });
});
document.getElementById('PeerToPeerLoansButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/p2ploans",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#PeerToPeerLoansDIVInf').html(html)
                }
            });
});
document.getElementById('LoadAffiliateButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/affiliates",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#AffiliateINFDiv').html(html)
                }
            });
});
document.getElementById('ShowWalletButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/wallet",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#WalletInfDIV').html(html)
                }
            });
});
document.getElementById('PublicProfilesButt').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "post",
                url: "/profiles",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#PublicProfilesINFDiv').html(html)
                }
            });
});
