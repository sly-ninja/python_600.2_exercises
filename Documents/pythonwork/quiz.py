def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    
    """
    play_list = []
    total_size = 0

    def getKey(song):
        return song[2]

    song_list_copy = sorted(songs, key = getKey)
    if songs[0][2] <= max_size:
        play_list.append(songs[0][0])
        total_size += songs[0][2]
        song_list_copy.remove(songs[0])
    else:
        return play_list
    
    for i in range(len(song_list_copy)):
        if (song_list_copy[0][2] + total_size) <= max_size:
            play_list.append(song_list_copy[0][0])
            total_size += song_list_copy[0][2]
            song_list_copy.remove(song_list_copy[0])

    print('play list', play_list)
    return play_list


# song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 20)


def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    


def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    pass