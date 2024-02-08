/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    chars = {}
    for (i = 0; i < s.length; i++) {
        if (!(s[i] in chars)) {
            chars[s[i]] = 0;
        }
        chars[s[i]]++;
    }
    for (i = 0; i < s.length; i++) {
        if (chars[s[i]] === 1) {
            return i;
        }
    }
    return -1;
};
