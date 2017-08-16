def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    
    """
    first_song = songs[0]
    songs_copy = songs[1:]
    play_list = []
    total_size = 0

    play_list.append(songs[0][0])
    
    if first_song[2] > max_size:
        return []
    
    for i in range(len(songs_copy)):
        while total_size <= max_size:
            if songs_copy == []:
                break
            
            next_song = min(songs_copy, key=lambda item:item[2])
            print(next_song)
            
            if next_song[2] + total_size <= max_size:
                play_list.append(next_song[0])
                total_size += next_song[2]
                print(songs_copy)
                songs_copy.remove(next_song)
                
            else:
                break
            
        return play_list
    
#    def getKey(song):
#        return song[2]
#
#    song_list_copy = sorted(songs, key = getKey)
#    if songs[0][2] <= max_size:
#        play_list.append(songs[0][0])
#        total_size += songs[0][2]
#        song_list_copy.remove(songs[0])
#    else:
#        return play_list
#    
#    for i in range(len(song_list_copy)):
#        if (song_list_copy[0][2] + total_size) <= max_size:
#            play_list.append(song_list_copy[0][0])
#            total_size += song_list_copy[0][2]
#            song_list_copy.remove(song_list_copy[0])
#
#    print('play list', play_list)
#    return play_list


#print(song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 3))
#print(song_playlist([('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)], 10))


def greedySum(integer_list, sum):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    total = 0
    
    for item in integer_list:
        multiplier = sum // item
        value = multiplier * item 
        
        if value == sum: 
            return total + multiplier
        
        if value < sum:
            total += multiplier  
            sum -= value  
            
        else: 
            return 'no solution'
        
    return 'no solution'

#greedySum([1], 20) 
    # 20
#print(greedySum([10, 9, 8, 1], 20))
    #2
#print(greedySum([10, 5, 1], 14))
    #5

def max_contig_sum(integer_list):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """

    max_ending_here = max_so_far = 0
    
    for item in integer_list:
        max_ending_here = max(0, max_ending_here + item)
        max_so_far = max(max_so_far, max_ending_here)
        
    return max_so_far

print(max_contig_sum([-2, -3, 4, -1, -2, 1, 5, -3]))