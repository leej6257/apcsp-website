!/bin/bash


echo -e "Content-type: text/html\n\n"

echo "<h1>Raspberry Pi Status: $rpi10@sp1b</h1>"

echo "<h2>Host Info</h2>"
echo "<li>Host name : $ rpi10@sp1b</li>"
echo "<li>IP Address: $ 172.19.200.199</li>"
echo "<li>OS name:    $ Raspbian GNU/Linux 9 (stretch)</li>"

echo "<h2>Who is logged in</h2>"
echo "<pre>$(who -a)</pre>"

echo "<h2>Performance Summary</h2>"
echo "<pre>$(top -bn1 | head -n 5)</pre>"

echo "<h2>Top 5 Processes by CPU</h2>"
echo "<pre>$(ps -aux --sort=-pcpu --columns 90 | head -n 6)</pre>"

echo "<h2>Top 5 Processes by Memory</h2>"
echo "<pre>$(ps -aux --sort=-pmem --columns 90 | head -n 6)</pre>"
