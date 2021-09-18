def asteroid_collision(ast):
    if len(ast) == 0:
        # Base case if empty : return
        return ast

    if len(ast) == 1:
        # Base case if has one element -> no collision occur
        return ast

    if len(ast) == 2:
        # Base case
        # If has 2 elements, calculate the collision result and return the result
        left = ast[0]
        right = ast[-1]
        if left < 0 and right < 0:
            # (<--- & <---) no collision occur
            return ast
        if left > 0 and right > 0:
            # (---> & --->) no collision occur
            return ast
        if left < 0 and right > 0:
            # (<--- & --->) no collision occur
            return ast

        if left > 0 and right < 0:
            # Collide (---> & <---)
            # Compare size and return the residue
            if abs(left) > abs(right):
                ast.pop(-1)
                return ast
            if abs(left) < abs(right):
                ast.pop(-2)
                return ast
            if abs(left) == abs(right):
                # Both collided
                ast.pop()
                ast.pop()
                return ast

    else:
        left = asteroid_collision(ast[:-1])
        if len(left) == 0:
            return [] + [ast[-1]]
    right = ast[-1]

    # Base case

    if left[-1] < 0 and right < 0:
        return left+[right]
    if left[-1] > 0 and right > 0:
        return left+[right]
    if left[-1] < 0 and right > 0:
        return left+[right]

    if left[-1] > 0 and right < 0:
        # Collide
        if abs(left[-1]) > abs(right):
            return left
        if abs(left[-1]) < abs(right):
            left.pop()
            left.append(right)
            return asteroid_collision(left)
        if abs(left[-1]) == abs(right):
            left.pop()
            return left


if __name__ == "__main__":
    x = input("Enter Input : ").split(",")
    x = list(map(int, x))
    print(asteroid_collision(x))
