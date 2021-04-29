<?php

$min = 8;
$max = 64;
$out = "";
$ascMin = 32;
$ascMax = 126;

for($i = $min; $i<=$max; $i++)
{
	$writeStr = "";
	$workingAry = array_fill(0,$i,$ascMin);
	do{
		for($strLen = $i-1; $strLen>=0;$strLen--){
			if($workingAry[$strLen]===$ascMax && ($strLen)>0){
				$workingAry[$strLen] = $ascMin;
				$workingAry[$strLen-1]++;
				writeOut($workingAry);
				break;
			}

			if($workingAry[$strLen]<$ascMax){
				$workingAry[$strLen]++;
				writeOut($workingAry);
				break;
			}

			
		}
	}while(substr_count($writeStr, chr($ascMax)) <= $i);
}

function writeOut($ary){

}
?>