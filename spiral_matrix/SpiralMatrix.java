/*Print a matrix in spiral order 
Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output: 
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
*/

class SpiralMatrix {
	
	public void printSpiralMatrix(int[][] matrix) {
		int numRows = matrix.length;
		int numCols = matrix[0].length;

		int minRow = 0;
		int maxRow = numRows-1;
		int minCol = 0;
		int maxCol = numCols-1;

		//because we start with going through the whole first row
		String direction = "right";
		boolean finished = false; 
		while(!finished) {
			switch(direction) {
				case "right": 
					for(int i = minCol; i <= maxCol; i++){
						System.out.println(matrix[minRow][i]);
					}

					minRow++;

					if (minRow > maxRow) finished = true;
					direction = "down";
					break;

				case "left": 
					for (int i = maxCol; i >= minCol; i--) {
						System.out.println(matrix[maxRow][i]);
					}	

					maxRow--;

					if (maxRow < minRow) finished = true;
					direction = "up";		
					break;

				case "up": 
					for (int i = maxRow; i >= minRow; i--) {
						System.out.println(matrix[i][minCol]);
					}

					minCol++;

					if (minCol > maxCol) finished = true;
					direction = "right";
					break;

				case "down": 
					for (int i = minRow; i <= maxRow; i++) {
						System.out.println(matrix[i][maxCol]);
					}
					maxCol--;
					if (maxCol < minCol) if (maxCol <= minCol) finished = true;
					direction = "left";
					break;
			}
		}
	}

	public static void main (String[] args) throws java.lang.Exception {
		int[][] matrix = {{1, 2, 3},
							{4, 5, 6},
				 			{7, 8, 9}};
		SpiralMatrix sm = new SpiralMatrix();
		//test on nxn
		System.out.println("Matrix: ");
		sm.printSpiralMatrix(matrix);
		//test on 1x2

		System.out.println("Matrix1: ");
		int[][] matrix1 = {{1}, 
							{2}};
		sm.printSpiralMatrix(matrix1);

		System.out.println("Matrix2: ");
		int[][] matrix2 = {{1, 2, 3, 4, 5}, 
							{6, 7, 8, 9, 10}, 
							{11, 12, 13, 14, 15}};
		sm.printSpiralMatrix(matrix2);

		System.out.println("Matrix3: ");
		int[][] matrix3 = {{1, 2, 3, 4, 5}, 
							{6, 7, 8, 9, 10}, 
							{11, 12, 13, 14, 15}, 
							{16, 17, 18, 19, 20}, 
							{21, 22, 23, 24, 25}, 
							{26, 27, 28, 29, 30}, 
							{31, 32, 33, 34, 35}};
		sm.printSpiralMatrix(matrix3);

    }
}