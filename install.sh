InstallDir=/usr/local 
InstallInc=${InstallDir}/include/tadcc/
echo 'mkdir '$InstallInc
mkdir ${InstallInc} -p
cp ./include/* ${InstallInc}

