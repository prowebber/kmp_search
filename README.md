# KMP (Knuth-Morris-Pratt) String Search Algorithm


![Python Version](https://img.shields.io/badge/Python-3.6-green?style=flat)

| Param            | Complexity (worst-case) |
|------------------|:-----------------------:|
| Time Complexity  |         _O(n)_          |
| Space Complexity |    O(_len(pattern)_)    |


### When to Use
* If you're searching multiple strings for the same match pattern
* If you're searching large blobs of text

### When _Not_ to Use
* If you're searching a single string less than several thousand characters
* If the match pattern is only a few chars


## How KMP Works
A drawback to Naive searches is the match pattern must searched from `pattern[0]` whenever the 
current character doesn't match the search text.

KMP works by pre-building a "lookup" table that specifies index positions of repeat sequences
in the match pattern.  This way whenever there is a mismatch the pattern can search from position
`pattern[n]` instead of `pattern[0]` whenever possible.

The below example explains how KMP handles searching for the text "ASSASSIN".

```
ASSASSIN    Match Pattern
00012300    LMP Index (Lookup table)
```

| Index | Char | LMP | When this Char Doesn't Match |
|:-----:|:----:|:---:|------------------------------|
|   0   |  A   |  0  | Start point                  |
|   1   |  S   |  0  | Search from index `0`        |
|   2   |  S   |  0  | Search from index `0`        |
|   3   |  A   |  1  | Search from index `1`        |
|   4   |  S   |  2  | Search from index `2`        |
|   5   |  S   |  3  | Search from index `3`        |
|   6   |  I   |  0  | Search from index `0`        |
|   7   |  N   |  0  | Search from index `0`        |

You can see the lookup table specifies an LMP value for each character in the match pattern.  The LMP value indicates
the index position to restart the search in the event of a mismatch.


