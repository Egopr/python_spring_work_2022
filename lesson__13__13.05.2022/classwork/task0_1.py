# def identity(nums):
#     return nums
# print (identity([1,2,3,4,5]))

# def power_(nums, pow):
#     step = [i**pow for i in nums]
#     return step
#
# print(power_([1,2,3,4,5,6],2))

# def evens(nums):
#     chet = [i for i in nums if i%2 == 0]
#     return chet
# print(evens([1,2,3,4,5,6,7,8,9]))

# strok = 'the quick brown fox jumps over the lazy dog'
# def words_not_the(sentence, exception):
#     word = sentence.split(' ')
#     schet = [len (i) for i in word if i!=exception]
#     return schet
# print (words_not_the(strok,'the'))


# def vowels(word):
#     letter = ['a', 'e', 'i', 'o', 'u']
#     small = word.lower()
#     glas = [i for i in small if i in letter]
#     return glas
# print(vowels('mathemAtics'))

dfg = ['one', 'two', 'three']
def mas_to_slov(mass):
    slov = [{x,y} for x in range(len(mass)) for y in mass ]
    return slov
print(mas_to_slov(dfg))
