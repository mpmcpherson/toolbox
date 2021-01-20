!#/bin/bash

grep -oP '<.*>:' libExporter.asm >> libExporterFunctions.txt

objdump -M intel -d libExporter.so >> libExporter.asm

ls | wc -l (get non-hidden entries --files and folders alike)

candidate = ls;

for i in $candidate
do

done

for i in *; do echo "$i" done

for f in *; do echo "File -> $f" done

for file in *; do type=$(file $file); if [[$type=="*executable"]] echo $file; elif [[]] echo $file; else echo $file; fi done



for file in *; do file $file; done
for file in *; do cat $file; done

