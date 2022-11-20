input=".env/config.txt"
while read line
do
    eval export $line
done< "$input"
