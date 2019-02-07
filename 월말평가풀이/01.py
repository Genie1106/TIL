# 나만의 단어장 만들기

class Word:
    def __init__(self):
        self.wordbook={}

    def add(self,en,ko):
        self.wordbook.update({en:ko})
        # self.wordbook[en] = ko

    def delete(self,en):
        if en in self.wordbook:
            del self.wordbook[en]
            # self.wordbook.pop(en)
            return True 
        return False

    def print(self):
        for x,y in self.wordbook.items():
            print(f"{x}: {y}")


if __name__ == "__main__":
    my_book = Word() 
    my_book.add('apple', '사과') 
    my_book.add('banana', '바나나') 
    my_book.add('cherry', '체리') 
    my_book.add('durian', '두리안') 
    my_book.print() 
    print(my_book.delete('cherry')) 
    print(my_book.delete('durian')) 
    print(my_book.delete('egg')) 
    my_book.print()