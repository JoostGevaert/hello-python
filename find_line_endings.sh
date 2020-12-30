ASCII=$(for f in $(find . -type f)
  do file $f
done | grep "ASCII text")

CRLFS=$(echo "$ASCII" | grep 'CRLF')
N_CRLFS=$(echo "$CRLFS" | wc -l)
echo This directory contains these $N_CRLFS files with CRLF line endings
echo "$CRLFS"
echo

LFS=$(echo "$ASCII" | grep -v 'CRLF')
N_LFS=$(echo "$LFS" | wc -l)
echo "This directory contains these $N_LFS files with LF (or no) line endings"
echo "$LFS"
