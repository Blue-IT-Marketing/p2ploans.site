

document.getElementById('AllocateToLoanPocketButt').addEventListener("click", function (ev) {
            var vstrLoanPocket = document.getElementById('strLoanPocket').value;
            var vstrAllocate = "YES";

            var dataString = '&vstrLoanPocket=' + vstrLoanPocket + '&vstrAllocate=' + vstrAllocate;
            $.ajax({
                type: "post",
                url: "/p2ploans",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#P2PLoanYourMoneyDIVInf').html(html)
                }
            });
});

document.getElementById('WithdrawFromLoanPocketButt').addEventListener("click", function (ev) {
            var vstrLoanPocket = document.getElementById('strLoanPocket').value;
            var vstrAllocate = "NO";

            var dataString = '&vstrLoanPocket=' + vstrLoanPocket + '&vstrAllocate=' + vstrAllocate;
            $.ajax({
                type: "post",
                url: "/p2ploans",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#P2PLoanYourMoneyDIVInf').html(html)
                }
            });
});

document.getElementById('TransferAvailableToLoanPocket').addEventListener("click", function (ev) {
            var vstrLoanPocket = document.getElementById('strLoanPocket').value;


            var dataString = '&vstrLoanPocket=' + vstrLoanPocket;
            $.ajax({
                type: "get",
                url: "/p2ploans/transferavailloanpocket",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#P2PLoanYourMoneyDIVInf').html(html)
                }
            });
});

document.getElementById('LoanRequestsButt').addEventListener("click", function (ev) {


            var dataString = '1';
            $.ajax({
                type: "get",
                url: "/p2ploans/loanrequests",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#LoansInfoDIV').html(html)
                }
            });
});
document.getElementById('ActiveLoansButt').addEventListener("click", function (ev) {
            var dataString = '1';
            $.ajax({
                type: "get",
                url: "/p2ploans/activeloans",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#LoansInfoDIV').html(html)
                }
            });
});
document.getElementById('AvailableLoansButt').addEventListener("click", function (ev) {
            var dataString = '1';
            $.ajax({
                type: "get",
                url: "/p2ploans/availableloans",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#LoansInfoDIV').html(html)
                }
            });
});
document.getElementById('LoansTakenButt').addEventListener("click", function (ev) {
            var dataString = '1';
            $.ajax({
                type: "get",
                url: "/p2ploans/loanstaken",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#LoansInfoDIV').html(html)
                }
            });
});
document.getElementById('BestFinanciersButt').addEventListener("click", function (ev) {
            var dataString = '1';
            $.ajax({
                type: "get",
                url: "/p2ploans/financiers",
                data: dataString,
                cache: false,
                success: function (html) {
                    $('#LoansInfoDIV').html(html)
                }
            });
});