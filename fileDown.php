<?php
  

$userAgent = 'Googlebot/2.1 (http://www.googlebot.com/bot.html)';
curl_setopt($ch, CURLOPT_USERAGENT, $userAgent);

 $ch = curl_init();
 curl_setopt($ch, CURLOPT_USERAGENT, $userAgent);
 curl_setopt($ch, CURLOPT_URL,$target_url);
 curl_setopt($ch, CURLOPT_FAILONERROR, true);
 curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
 curl_setopt($ch, CURLOPT_AUTOREFERER, true);
 curl_setopt($ch, CURLOPT_RETURNTRANSFER,true);
 curl_setopt($ch, CURLOPT_TIMEOUT, 10);
 $html = curl_exec($ch);

 if (!$html) {
        echo "<br />cURL error number:" .curl_errno($ch);
        echo "<br />cURL error:" . curl_error($ch);
}else{
    echo $html;
}


function mydl($file){
    // Initialize a file URL to the variable
    $url = $file;
      
    // Use basename() function to return the base name of file
    $file_name = basename($url);
      
    // Use file_get_contents() function to get the file
    // from url and use file_put_contents() function to
    // save the file by using base name
    if (file_put_contents($file_name, file_get_contents($url)))
    {
        echo "File downloaded successfully";
    }
    else
    {
        echo "File downloading failed.";
    }
}
?>