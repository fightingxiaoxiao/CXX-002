mkdir -p ./del_blank

for I in {0..15}
do
    echo "Deleting processor$I"
    rsync --delete-before -d ./del_blank/ ./processor$I/
    rm -r ./processor$I
done