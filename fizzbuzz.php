<?php
	function fizzBuzz(int $num){
		$returnVal = "";
		$fizzedOrBuzzed = false;


		if($num%3==0){
			$returnVal.="fizz";
			$fizzedOrBuzzed = true;
		}
		
		if ($num%5==0) {
			$returnVal.="buzz";
			$fizzedOrBuzzed = true;
		}

		if(fizzedOrBuzzed==false){
			$returnVal = $num;
		}
		
		return $returnVal;
	}

?>