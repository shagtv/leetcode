<?php

class Solution {

    /**
     * @param String[] $words
     * @return String
     */
    function firstPalindrome($words) {
        foreach($words as $word) {
            if ($word == strrev($word)) {
                return $word;
            }
        }
        return '';
    }
}


$givenWords = ['abc', 'car', 'ada', 'racecar', 'cool'];
$expected = 'ada';
$result = (new Solution())->firstPalindrome($givenWords);
assert($result === $expected);
