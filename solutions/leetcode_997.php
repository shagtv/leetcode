<?php

class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $trust
     * @return Integer
     */
    function findJudge($n, $trust) {
        if ($n === 1) return 1;
        $votes = [];
        $voters = [];
        foreach ($trust as $t) {
            $voters[$t[0]] = true;
            if (!isset($votes[$t[1]])) {
                $votes[$t[1]] = 1;
            } else {
                $votes[$t[1]]++;
            }
        }
        foreach ($votes as $v => $count) {
            if (empty($voters[$v]) && $count === $n - 1) {
                return $v;
            }
        }
        return -1;
    }
}

$givenN = 3;
$givenTrust = [[1, 3], [2, 3], [3, 1]];
$expected = -1;

$solution = new Solution();
$result = $solution->findJudge($givenN, $givenTrust);
if ($result != $expected) {
    echo "$result not equals $expected\n";
}