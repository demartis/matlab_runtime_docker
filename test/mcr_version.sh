# ------------------------------------------------------------------------
# Copyright (c) 2020-2023 Riccardo De Martis. MIT License.
# All Trademarks referred to are the property of their respective owners.
# ------------------------------------------------------------------------


XMLTAG=release
result=`sed -n "/$XMLTAG/{s/.*<$XMLTAG>//;s/<\/$XMLTAG.*//;p;}" $MCR_MASTER_PATH/VersionInfo.xml`

echo "======================================================="
echo "Script to verify the MCR real install path and version."
echo "-------------------------------------------------------"

echo "Dump VersionInfo.xml"
cat $MCR_MASTER_PATH/VersionInfo.xml
echo "-------------------------------------------------------"


echo "Install path:" $MCR_MASTER_PATH
echo "-------------------------------------------------------"

echo "Checking MCR release. It must be $1"
if [[ "$result" == "$1" ]]; then
  echo "OK. Test passed."
else
  echo -e '\033[31m' "Error. Version found: $result" '\033[0m'
  exit 1
fi
echo "-------------------------------------------------------"

