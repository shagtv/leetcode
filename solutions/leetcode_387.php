<?php

class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function firstUniqChar($s) {
        $chars = [];
        for ($i = 0; $i < strlen($s); $i++) {
            $chars[$s[$i]] = ($chars[$s[$i]] ?? 0) + 1;
        }
        for ($i = 0; $i < strlen($s); $i++) {
            if ($chars[$s[$i]] === 1) {
                return $i;
            }
        }
        return -1;
    }
}
