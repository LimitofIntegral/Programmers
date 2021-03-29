def solution(new_id):
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.']
    id = new_id.lower()

    temp = ''
    for i in id:
        if i in arr:
            temp += i

    temp_ = ''
    for i in range(len(temp)):
        if temp[i] != '.':
            temp_ += temp[i]
        else:
            if temp[i - 1] != '.':
                temp_ += temp[i]
            else:
                pass

    if len(temp_) != 0:
        if temp_[0] == '.':
            temp_ = temp_[1:]
    else:
        pass

    if len(temp_) != 0:
        if temp_[-1] == '.':
            temp_ = temp_[:len(temp_) - 1]
    else:
        pass

    if temp_ == '':
        temp_ = 'a'

    if len(temp_) > 15:
        temp_ = temp_[0:15]
        if temp_[-1] == '.':
            temp_ = temp_[0:14]

    if len(temp_) <= 2:
        while len(temp_) != 3:
            temp_ += temp_[-1]

    return temp_