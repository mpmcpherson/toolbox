<?php
	$draculaText=file_get_contents('dracula.txt');
	$pattern = "[\n[0-9]?+\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).+]";
	$matches = [];
	$trims = preg_match_all($pattern, $draculaText, $matches);
	
	print_r("\n".$matches[0][0]);

	// foreach ($trims as $key => $value) {
	// 	print_r("Key ".$key."\n");
	// 	print_r("Value ".$value."\n");
	// 	print_r("\n");
	// }
	//var_dump($matches);

?>