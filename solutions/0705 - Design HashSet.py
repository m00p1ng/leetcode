from typing import List

class MyHashSet:
    def __init__(self):
        self.list: List[bool] = [False]*((10**6)+10)

    def add(self, key: int) -> None:
        self.list[key] = True

    def remove(self, key: int) -> None:
        self.list[key] = False

    def contains(self, key: int) -> bool:
        return self.list[key]


if __name__ == "__main__":
    myHashSet = MyHashSet();
    myHashSet.add(1);      # set = [1]
    myHashSet.add(2);      # set = [1, 2]
    myHashSet.contains(1); # return True
    myHashSet.contains(3); # return False, (not found)
    myHashSet.add(2);      # set = [1, 2]
    myHashSet.contains(2); # return True
    myHashSet.remove(2);   # set = [1]
    myHashSet.contains(2); # return False, (already removed)
