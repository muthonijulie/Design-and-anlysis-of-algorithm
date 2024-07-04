def lcs(string1, string2):
    m, n = len(string1), len(string2)
    # Create a 2D array to store lengths of longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Length of LCS is in dp[m][n]
    lcs_length = dp[m][n]
    
    # Construct the LCS sequence
    lcs_sequence = []
    i, j = m, n
    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            lcs_sequence.append(string1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    # The sequence is constructed backwards, so reverse it
    lcs_sequence.reverse()
    
    return lcs_length, ''.join(lcs_sequence)

# Example usage
string1 = "AGGTAB"
string2 = "GXTXAYB"

# Get the LCS length and sequence
lcs_length, lcs_sequence = lcs(string1, string2)
print(f"LCS Length: {lcs_length}")
print(f"LCS Sequence: {lcs_sequence}")