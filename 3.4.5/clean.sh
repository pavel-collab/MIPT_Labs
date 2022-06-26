#!/bin/bash

aux=main.aux
fdb_latexmk=main.fdb_latexmk
fls=main.fls
out=main.out
gz=main.gz
synctex_gz=main.synctex.gz
log=main.log
bbl=main.bbl
blg=main.blg
toc=main.toc

arr1=($aux $fdb_latexmk $fls $out $gz $synctex_gz $log $bbl $blg $toc)

for i in ${!arr1[@]}; do
    if [ -f ${arr1[$i]} ]
    then
    echo "${arr1[$i]} exists"
    rm ${arr1[$i]}
    else
    echo "${arr1[$i]} doesn't exists"
    fi
done

vscode=.vscode
pycache=__pycache__

arr2=($vscode $pycache)

for i in ${!arr2[@]}; do
    if [ -e ${arr2[$i]} ]
    then
    echo "${arr2[$i]} exists"
    rm -r ${arr2[$i]}
    else
    echo "${arr2[$i]} doesn't exists"
    fi
done

echo "all technical files were removed"