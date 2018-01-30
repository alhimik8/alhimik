#!/bin/bash
# Before using - change please
# user="--username=USER" and  pass="--password=PASS"
# to real ones
##
# usage: svnexport.sh start_revision end_revision"
##


SETCOLOR_SUCCESS="echo -en \\033[1;32m"
SETCOLOR_FAILURE="echo -en \\033[1;31m"
SETCOLOR_NORMAL="echo -en \\033[0;39m"
if [ $# -lt 2 ] ; then
 echo "usage:  svnexport.sh start_revision end_revision";
 svn log -v $user $pass |less
 exit 0
fi

user="--username=USER"
pass="--password=PASS"
rev_start=$1
rev_end=$2
export_dir=./svn_export/$rev_end
echo -n "Make export of changed files? (y/n) "
read item
case "$item" in
    y|Y) echo "Yes  «y»"
        ;;
    n|N) echo "No «n»"
        exit 0
        ;;
   *) echo "Wrong answer - cancelling"
        exit 0
        ;;
    esac
mkdir -p $export_dir
svn diff --summarize -r $rev_start:$rev_end $user $pass
echo "Copying..." && 
cp -a --parents `svn diff --summarize -r $rev_start:$rev_end $user $pass | awk '{print $2}'` $export_dir 
if [ $? -eq 0 ]; then
    $SETCOLOR_SUCCESS
    echo -n "$(tput hpa $(tput cols))$(tput cub 6)[OK]"
    $SETCOLOR_NORMAL
    echo
else
    $SETCOLOR_FAILURE
    echo -n "$(tput hpa $(tput cols))$(tput cub 6)[fail]"
    $SETCOLOR_NORMAL
    echo
fi
echo 'All files are copied to the' $export_dir
du -sh $export_dir
