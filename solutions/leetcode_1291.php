<?php

class Solution {

    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer[]
     */
    function sequentialDigits($low, $high) {
        $nums = [
            12,23,34,45,56,67,78,89,
            123,234,345,456,567,678,789,
            1234,2345,3456,4567,5678,6789,
            12345,23456,34567,45678,56789,
            123456,234567,345678,456789,
            1234567,2345678,3456789,
            12345678,23456789,
            123456789
        ];
        $result = [];
        foreach ($nums as $num) {
            if ($num < $low) {
                continue;
            }
            if ($num > $high) {
                break;
            }
            $result[] = $num;
        }
        return $result;
    }
}

$givenLow = 1000;
$givenHigh = 13000;
$expected = [1234, 2345, 3456, 4567, 5678, 6789, 12345];

$solution = new Solution();
$result = $solution->sequentialDigits($givenLow, $givenHigh);
assert($result === $expected);
