<?php

$test = "   line 1     
     line 2 with blanks at end          
     line 3 with tabs at end			";

print $test;

$regex = '/(^[ \t]*|[ \t]*$)/m';
$res = preg_replace($regex, "=", $test);
print $res;
