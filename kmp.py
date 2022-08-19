# Python Files
# Project Files


def search(pat=None, text=None, lps=None):
	"""
	This will return the index position of the 1st matched character (if a match is found). If
	a match is *not* found, it will return -1.
	- 'pat' and 'text' arguments are required
	- If desired, you can pre-generate the `lps` lookup table and supply it as an
	  argument.  This allows you to search multiple texts for the same pattern without
	  the lookup table being re-generated each search.
	
	:param str pat:     The text pattern to find
	:param str text:    The text to search
	:param list lps:    Optional LPS list (if not supplied it will be generated)
	"""
	p, s = len(pat), len(text)  # Size of (match, text) strings
	
	# Generate the LPS lookup table (if not supplied)
	if not lps:
		lps = gen_lps_map(pat=pat)
	
	"""
	Check for matches
	1)  Step through each character of the search text until the 1st char in the pattern is matched
	2a) If all characters in the pattern are matched, return the index position of 1st char matched
	2b) If the pattern is partially matched use the 'lookup table' to see if the past few chars
	    match any other characters the match pattern.  If so, re-evaluate from that position (rather
	    than index[0]).  If not, re-check the pattern from index[0].
    2c) If the end of the search text is reached without a positive match, return -1 indicating
        no match was found.
	"""
	i = ii = 0
	while (s - i) >= (p - ii):              # While the remaining search text has more characters than the match pattern
		if pat[ii] == text[i]:              # When the search AND pattern chars are equal in the correct sequence
			i += 1                          # Step to the next text char
			ii += 1                         # Step to the next pattern char
		if ii == p:                         # If the match pattern is fully matched
			return i - ii                   # Return the index position where first matched char occurred
		elif i < s and pat[ii] != text[i]:  # If the current char doesn't match the pattern
			if ii != 0:                     # If the previous character matched the pattern
				ii = lps[ii - 1]            # Search the pattern starting at the previously matched index
			else:
				i += 1
	return -1


def gen_lps_map(pat=None):
	"""
	Generate the LPS lookup table/map used in the search
	- TLDR: Find similarities in the pattern text.  Create a lookup table containing the index
	  positions of all repeat chars and sequences in the pattern relative to the pattern text.
	  
    This table isn't expensive to build, but it is an extra step in the search process.  Because
    of this the naive search algorithm is normally a better choice when searching short strings.
	
	:param str pat: Pattern to match
	"""
	n, i, p = 0, 1, len(pat)        # Length of lps, index of 2nd char in text, length of pattern
	lps = [0] * p                   # Create a list of '0' values the size of 'p'
	while i < p:                    # Loop through the indices of the match pattern (starting at 1)
		if pat[i] == pat[n]:
			n += 1
			lps[i] = n
			i += 1
		else:
			if n == 0:
				lps[i] = 0
				i += 1
			else:
				n = lps[n - 1]
	return lps


if __name__ == "__main__":
	text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
	pattern = "occaecat"
	
	first_match = search(pat=pattern, text=text)
	print(f"Match found at position: {first_match}")
