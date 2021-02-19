<?php

$str = "";
//$str = "Va beqre gb trarengr gur vaivgr pbqr, znxr n CBFG erdhrfg gb /ncv/vaivgr/trarengr";

//print_r(str_rot13($str)."\n");
print_r(base64_decode($str)."\n");



Va beqre gb trarengr gur vaivgr pbqr, znxr n CBFG erdhrfg gb /ncv/vaivgr/trarengr

In order to generate the invite code, make a POST request to /api/invite/generate



function doMakeInviteCode() {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: '/api/invite/generate',
        success: function(a) {
            console.log(a)
        },
        error: function(a) {
            console.log(a)
        }
    })
}

?>