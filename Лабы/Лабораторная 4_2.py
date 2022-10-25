# Реализовать функцию delete, принимающую список и индекс, по которому надо удалить элемент.
def delete(list_, index=None):
    if index is None:
        index = list_[-1]
    list_ = list_[:index] + list_[index + 1:]
    return list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
