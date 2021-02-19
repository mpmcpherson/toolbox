<?php

$newAry = array();
$max = 10000;
$len = $max;

for($i=0;$i<$len;$i++){
    array_push($newAry,rand(0,$max));
}
print_r("rands generated\n");

print_r("sum ".getMinimumUniqueSum($newAry));
print_r("\n");

function getMinimumUniqueSum(array $array){    
    while(count(array_unique($array))<count($array)){
        $dupes = 0;
        foreach($array as $key=>$value){
            if(array_count_values($array)[$value]>1){
                $dupes++;
                $array[$key] = $value+1;
                //print("[".$key."] => ".$value." DUPLICATE\n");
            }
            /*
            if($key%1000===0){
                echo "logpoint\n";
            }
            */
        }
        $outHash = "";
        for($i=0;$i<$dupes;$i=$i+10){
            $outHash = $outHash."|";
        }
        print_r($outHash." - ".$dupes."\n");
        //print_r("duplicate counts: ".$dupes);
        //sleep(2);
    }
    //print_r($array);
    return array_sum($array);
}
function array_count_values_of($value, $array) {
    $counts = array_count_values($array);
    return $counts[$value];
}

?>