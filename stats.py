def get_num_words(file_contents):
    words = file_contents.split(" ")
    return len(words)

def get_char_count(content):
    dict = {}
    for ch in content:
        ch = ch.lower()
        if ch in dict:
            dict[ch] =  dict.get(ch) + 1
        else:dict[ch] = 1
    return dict


def sort_on(items):
    return items["count"]

def sortList(counts) : 
    list = []

    for item in counts:
        list.append({"word" : item , "count" : counts[item] })
    list.sort(reverse = True, key = sort_on)
    return list