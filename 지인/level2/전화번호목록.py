def solution(phone_book):
    if len(phone_book) == 1:
        return True
    else:
        phone_book.sort(key=lambda x: len(x))
        print(phone_book)
        for i in range(len(phone_book)):
            for j in range(i+1, len(phone_book)):
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    return False
    return True