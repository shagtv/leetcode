class Solution {

    /**
     * @param String $s
     * @return String
     */
    function frequencySort($s) {
        $chars = [];
        for ($i = 0; $i < strlen($s); $i++) {
            if (empty($chars[$s[$i]])) $chars[$s[$i]] = 0;
            $chars[$s[$i]]++;
        }
        arsort($chars, true);

        $result = '';
        foreach ($chars as $c => $num) {
            if (!$num) break;
            $result .= str_repeat($c, $num);
        }

        return $result;
    }
}
