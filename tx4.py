class File:
    def __init__(self, name, size=0):
        self.filename = name
        self.size = size

    def verify_filename(self, filename):
        if not isinstance(filename, str):
            raise ValueError("File must be a string")
        if not filename.endswith(".txt"):
            raise ValueError("File name must end with .txt")

    def verify_size(self, size):
        if not isinstance(size, int) or size < 0:
            raise ValueError("Size must be a positive integer")

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        self.verify_filename(value)
        self.__filename = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.verify_size(value)
        self.__size = value

    def __eq__(self, other: "File") -> bool:
        return self.size == other.size

    def __ne__(self, other: "File") -> bool:
        return self.size != other.size

    def __lt__(self, other: "File") -> bool:
        return self.size < other.size

    def __gt__(self, other: "File") -> bool:
        return self.size > other.size

    def __le__(self, other: "File") -> bool:
        return self.size <= other.size

    def __ge__(self, other: "File") -> bool:
        return self.size >= other.size

    def __repr__(self) -> str:
        return f"File(name={self.name}, size={self.size})"


# Пример использования
file1 = File(name="file1.txt", size=1024)
file2 = File(name="file2.txt", size=2048)

print(file1 == file2)  # False
print(file1 < file2)  # True
print(file1 >= file2)  # False
