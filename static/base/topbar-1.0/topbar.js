/*!
 * topBar v1.0
 * Copyright (c) 2012-2017 Tencent BlueKing. All Rights Reserved.
 * author : 钃濋哺鏅轰簯
 */

$(function() {
    var topBarTimline = 0;
    $topBar = function(options) {
        $div = $("<div class='magic-topbar-container'></div>");
        if ((typeof options == 'object') && options.constructor == Object) {
            // 璁剧疆榛樿鍊�
            var defaults = {
                    setClass: 'bg-primary',
                    close: function() {},
                    timeOut: 0,
                }
                // 浼犲弬璁剧疆
            var options = $.extend(defaults, options);

            // 鍒ゆ柇椤甸潰鏄惁鏈夋彁绀烘潯
            if ($('.magic-topbar-container').length>0) {
                $('.magic-topbar-container').remove();
                clearTimeout(topBarTimline);
            };
            if ($('.' + options.setClass).length == 0 ) {
                // 鐢熸垚鎻愮ず鏉�
                $div.addClass(options.setClass).appendTo('body').html('<span>' + options.text + '</span>');
                // 娣诲姞鍏抽棴鎸夐挳
                $div.append('<div class="magic-topbar-close" style="font-size:20px; float:right;margin:-5px -15px 0 0;cursor:pointer;">&times;</div>');
                // 闃绘鍐掓场鍜岄粯璁よ涓�
                $div.on('click', function() {
                        return false;
                    });
                // 鍏抽棴鎸夐挳浜嬩欢
                $('.magic-topbar-close').on('click', function() {
                        $(this).parent().remove();
                        options.close();
                        return false;
                    });
                // 璁剧疆榛樿鍏抽棴鏃堕棿
                function closeFn() {
                    $('.magic-topbar-close').trigger('click');
                    clearTimeout(topBarTimline);
                }
                if (!options.timeOut == 0 && options.timeOut > 0) {
                    topBarTimline = setTimeout(closeFn, options.timeOut);
                };
                // 榧犳爣绉诲叆绉诲嚭
                $div.mouseenter(function() {
                    clearTimeout(topBarTimline);
                });
                $div.mouseleave(function() {
                    if (!options.timeOut == 0 && options.timeOut > 0) {
                        topBarTimline = setTimeout(closeFn, options.timeOut);
                    };
                })
            };
        };

    }

});
