<?php

$newAry = array();
$len = rand(1,2000);

for($i=0;$i<$len;$i++){
    array_push($newAry,rand(0,3000-$len));
}

print_r("sum ".getMinimumUniqueSum($newAry));
print_r("\n");

function getMinimumUniqueSum(array $ary){
    $array = $ary;
    
    while(count(array_unique($array))<count($array)){
        $dupes = 0;
        foreach($array as $key=>$value){
            if(array_count_values($array)[$value]>1){
                $dupes++;
                $array[$key] = $value+1;
                print("[".$key."] => ".$value." DUPLICATE\n");
            }else{
                //print("[".$key."] => ".$value."\n");
            }
        }
        print_r("duplicate counts: ".$dupes);
        sleep(2);
    }
    print_r($array);
    return array_sum($array);
}
function array_count_values_of($value, $array) {
    $counts = array_count_values($array);
    return $counts[$value];
}

?>