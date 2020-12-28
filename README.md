# EMR-Statistics-Monitor

Monitor the stats of min instances running on EMR. 
Sample only monitors stats for Core INstances running.

Idea is to fetch the stats from Cloudwatch and ultimately intelligently retry if there are failures due to spot terminations.
