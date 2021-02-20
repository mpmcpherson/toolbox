<?php


$fixedCost = 1930;
print_r("\n");
print_r("\n");
print_r("\n");

print_r("Perfect Bound B&W \n");
print_r("--------------------------------------------------------------------------------\n");
$costPerItem = 2.4;

$salePrice = 8;
print_r("at sale price \$$salePrice, CPI \$$costPerItem: ".round(BESFunc($salePrice, $costPerItem, $fixedCost),0)." copies \n");

$salePrice = 10;
print_r("at sale price \$$salePrice, CPI \$$costPerItem: ".round(BESFunc($salePrice, $costPerItem, $fixedCost),0)." copies \n");

$salePrice = 12;
print_r("at sale price \$$salePrice, CPI \$$costPerItem: ".round(BESFunc($salePrice, $costPerItem, $fixedCost),0)." copies \n");

$salePrice = 15;
print_r("at sale price \$$salePrice, CPI \$$costPerItem: ".round(BESFunc($salePrice, $costPerItem, $fixedCost),0)." copies \n");

print_r("\n");
print_r("\n");
print_r("\n");
print_r("Case Bound B&W \n");
print_r("--------------------------------------------------------------------------------\n");
$costPerItem = 8;

$salePrice = 9;
print_r("at sale price \$$salePrice, CPI \$$costPerItem: ".round(BESFunc($salePrice, $costPerItem, $fixedCost),0)." copies \n");

$salePrice = 10;
print_r("at sale price \$$salePrice, CPI \$$costPerItem: ".round(BESFunc($salePrice, $costPerItem, $fixedCost),0)." copies \n");

$salePrice = 12;
print_r("at sale price \$$salePrice, CPI \$$costPerItem: ".round(BESFunc($salePrice, $costPerItem, $fixedCost),0)." copies \n");

$salePrice = 15;
print_r("at sale price \$$salePrice, CPI \$$costPerItem: ".round(BESFunc($salePrice, $costPerItem, $fixedCost),0)." copies \n");

print_r("\n");
print_r("\n");
print_r("\n");

function BESFunc(int $price, int $cpi, int $fc){
	$ttlCopies = ($fc/$price);
	$newCost = $ttlCopies*$cpi;
	if($newCost<$cpi){
		return 1;
	}else{
		return $ttlCopies + BESFunc($price, $cpi, $newCost);
	}
}

?>