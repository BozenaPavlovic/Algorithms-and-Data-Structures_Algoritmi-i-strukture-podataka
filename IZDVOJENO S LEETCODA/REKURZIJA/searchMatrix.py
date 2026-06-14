def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    # Početna pozicija: gornji desni kut
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Element je prevelik, eliminiraj cijeli trenutni stupac
        else:
            row += 1  # Element je premali, eliminiraj cijeli trenutni red

    return False