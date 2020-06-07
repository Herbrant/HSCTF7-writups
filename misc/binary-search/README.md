# Binary Word Search

My little brother who is in kindergarten was given this to him by his teacher. He wasn't able to solve it, but can you?
Note: 0 is black, 1 is white. The entire flag is hidden inside the word search, including flag{}. The flag may also be backwards or diagonally hidden.

## Solution

You have to take the pixel value and see all the image as a matrix.
Then you have to find the string 'flag' in the matrix (binary search).
You can check out search.py file and execute it:

```
python search.py
```