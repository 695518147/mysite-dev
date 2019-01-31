var xiaobing = (function () {

    //缓冲对象容器
    var orders = {};

    /***
     * 显示右侧内容
     * @param dom
     */
    function showContent(dom) {
        var id = dom.id;
        var order;
        if ((id in orders) || (orders[id] && orders[id] != '')) {
            order = orders[id];
            if (order["isSplit"] == false) {
                $("#content2").empty().html(order.orderTypeDescription);
                $("#content1").hide();
                $("hr").hide();
            } else {
                $("#content1").show();
                $("hr").show();
                $("#content1").empty().html(order.orderTypeDescription);
                $("#content2").empty().html(order.orderDescription);
            }
        } else {
            $.ajax({
                type: "GET",
                url: "/xb/order/" + id,
            }).done(function (data) {
                order = data;
                orders[id] = order;
                if (order["isSplit"] == false) {
                    $("#content2").empty().html(order.orderTypeDescription);
                    $("#content1").hide();
                    $("hr").hide();
                } else {
                    $("#content1").show();
                    $("hr").show();
                    $("#content1").empty().html(order.orderTypeDescription);
                    $("#content2").empty().html(order.orderDescription);
                }
            }).fail(function (err) {

            });
        }
        $(dom).addClass("meun-item-active").siblings().removeClass("meun-item-active");
    }

    /**
     * 初始化头部tab
     */
    function initTopTab() {
        $.ajax({
            type: "GET",
            url: "/xb/orderType",
        }).done(function (data) {
            var json = data.results == undefined ? data : data.results;
            var arr = [];
            $.each(json, function (index, orderType) {
                var li = '<li role="presentation" class="' + (index == 0 ? "active" : "") + '" id="' + orderType.id + '"><a href="#">' + orderType.orderTypeName + '</a></li>';
                arr.push(li)
            });
            $("#tab_header").empty()
                .append(arr.join(" "))
                .find("li")
                .on("click", function () {
                    $(this).addClass("active").siblings().removeClass("active");
                    initLeftMeun(this.id);
                });
            $("#tab_header").find("li.active").trigger('click');
        });
    }

    /**
     * 初始化左侧菜单
     * @param typeId
     */
    function initLeftMeun(typeId) {
        $.ajax({
            type: "GET",
            url: "/xb/order",
            data: {'orderType': typeId}
        }).done(function (data) {
            if (!!data.length) {
                var json = data.results == undefined ? data : data.results;
                $("#leftMeun").empty();
                $.each(json, function (index, order) {
                    var item = '<div class="meun-item ' + (index == 0 ? " meun-item-active" : "") + '" ' +
                        'id="' + order.id + '" onclick="xiaobing.showContent(this)" href="#" name=' + order.orderType + ' role="tab" data-toggle="tab">' +
                        '<div id="lineHight">' + order.orderName + '</div> </div>';
                    if (index == 0) {
                        if (order["isSplit"] == false) {
                            $("#content2").empty().html(order.orderTypeDescription);
                            $("#content1").hide();
                            $("hr").hide();
                        } else {
                            $("#content1").show();
                            $("hr").show();
                            $("#content1").empty().html(order.orderTypeDescription);
                            $("#content2").empty().html(order.orderDescription);
                        }
                    }
                    $("#leftMeun").append(item)
                });
            } else {
                $("#leftMeun").empty();
                $("#content1").empty();
                $("#content2").empty();
            }


        });
    }

    return {
        showContent: function (dom) {
            showContent(dom)
        },
        initTopTab: function () {
            initTopTab()
        }
    }
})();