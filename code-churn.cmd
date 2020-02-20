git log --all --numstat --date=short --pretty=format:'--%h--%ad--%aN' > logfile.txt
java -jar .\app-standalone.jar -l logfile.txt -c git2  --input-encoding UTF16 -r 30 -a entity-churn