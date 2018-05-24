


document.getElementById('CancelWithDrawButton').addEventListener("click", function (ev) {
            var dataString = 1;
            $.ajax({
                type: "get",
                url: "/wallet/cancelwithdrawal",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#WithdrawalINFDIV').html(html)
                }
            });
});

document.getElementById('WithdrawButt').addEventListener("click", function (ev) {
          var vstrWithDrawalAmount = document.getElementById('strWithDrawalAmount').value;
          var vstrWithdrawalMethod = document.getElementById('strWithdrawalMethod').value;

            var dataString = '&vstrWithDrawalAmount=' + vstrWithDrawalAmount + '&vstrWithdrawalMethod=' + vstrWithdrawalMethod;
            $.ajax({
                type: "get",
                url: "/wallet/withdraw",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#WithdrawalINFDIV').html(html)
                }
            });
});
document.getElementById('SaveLinkedAccountsButt').addEventListener("click", function (ev) {
          var vstrAccountHolder = document.getElementById('strAccountHolder').value;
          var vstrBankName = document.getElementById('strBankName').value;
          var vstrBranchCode = document.getElementById('strBranchCode').value;
          var vstrAccountNumber = document.getElementById('strAccountNumber').value;
          var vstrAccountType = document.getElementById('strAccountType').value;
          var vstrPayPalEmail = document.getElementById('strPayPalEmail').value;


            var dataString = '&vstrAccountHolder=' + vstrAccountHolder + '&vstrBankName=' + vstrBankName +
                '&vstrBranchCode=' + vstrBranchCode + '&vstrAccountNumber=' + vstrAccountNumber + '&vstrAccountType='+vstrAccountType +
                '&vstrPayPalEmail=' + vstrPayPalEmail;
            $.ajax({
                type: "post",
                url: "/wallet",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#LinkedAccountsINFDiv').html(html)
                }
            });
});