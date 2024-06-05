pyfiglet -f big "$argv[1]" | sed 's:^:# :' | pbcopy
echo "Term '$argv[1]' is now on clipboard."
