def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from rod {source} to rod {destination}")
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from rod {source} to rod {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source)

# Example usage
n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
# Time Complexity: O(2^n)
# Space Complexity: O(n)
# where n is the number of disks.   
# Example usage:
# n = 3
# tower_of_hanoi(n, 'A', 'C', 'B')
# Output:
# Move disk 1 from rod A to rod C
# Move disk 2 from rod A to rod B
# Move disk 1 from rod C to rod B
# Move disk 3 from rod A to rod C
# Move disk 1 from rod B to rod A
# Move disk 2 from rod B to rod C
# Move disk 1 from rod A to rod C       
# where n is the number of disks.   
