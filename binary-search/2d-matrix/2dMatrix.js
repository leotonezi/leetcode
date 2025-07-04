function matrixSearch(matrix, target) {
    let left = 0;
    let n = matrix[0].length;
    let right = matrix.length * n - 1;

    while(left <= right) {
        let mid = Math.floor((left + right) / 2);
        let midElement = matrix[Math.floor(mid / n)][mid % n];

        if(midElement === target) {
            return true;
        }
        if(midElement < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return false;
}

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]];

console.log(matrixSearch(matrix, 23));