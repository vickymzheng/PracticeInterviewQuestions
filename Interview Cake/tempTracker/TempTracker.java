class TempTracker {
	private int[] _tempCounts = new int[111];
	private int numItems = 0;
	private int _maxTemp;
	private int _minTemp; 
	private int _sumOfAllTemps = 0;
	private int _modeIndex = 0;

	public void insert(int temp) {
		if (numItems == 0) {
			_maxTemp = temp;
			_minTemp = temp;
		}

		else {
			if (_maxTemp < temp) _maxTemp = temp;
			if (temp < _minTemp) _minTemp = temp;
		}

		_tempCounts[temp]++;
		numItems++;

		//resizing array if it runs out of capacity
		_sumOfAllTemps = _sumOfAllTemps + temp;
		if (_tempCounts[temp] > _tempCounts[_modeIndex]) {
			_modeIndex = temp;
		}

	}

	public int getMax() {
		return _maxTemp;
	}

	public int getMin() {
		return _minTemp;
	}

	public float getMean() {
		float mean = (float) _sumOfAllTemps / numItems;
		return mean;
	}

	public int getMode(){
		return _modeIndex;
	}

	public TempTracker() {
		
	}
}

class PreOptTempTracker {
	private int[] _temperatures;
	private int capacity = 2;
	private int numItems = 0;
	private int _maxTemp;
	private int _minTemp; 

	public void insert(int temp) {
		_temperatures[numItems] = temp;
		numItems++;
		if (numItems >= capacity) {
			int[] holder = new int[capacity*2];
			for (int i = 0; i < numItems; i++) {
				holder[i] = _temperatures[i];
			}
			_temperatures = holder;
			capacity = capacity*2;
		}
	}

	public int getMax() {
		int max = _temperatures[0];
		for(int i = 0; i < numItems; i++) {
			if (max < _temperatures[i]) {
				max = _temperatures[i];
			}
		}
		return max;
	}

	public int getMin() {
		int min = _temperatures[0];
		for(int i = 0; i < numItems; i++) {
			if (_temperatures[i] < min) {
				min = _temperatures[i];
			}
		}
		return min;
	}

	public float getMean() {
		int sum = 0; 
		for (int i = 0; i < numItems; i++) {
			sum = sum + _temperatures[i];
		}

		float mean = (float) sum / numItems;
		return mean;
	}

	public int getMode(){
		int[] bin = new int[111];
		for(int i = 0; i < numItems; i++){
			bin[_temperatures[i]]++;
		}
		int mode_index = 0;
		int mode_count = bin[0];
		for (int i = 0; i < 111; i++) {
			if (bin[i] > mode_count) {
				mode_index = i;
			}
		}

		return mode_index;
	}

	public PreOptTempTracker() {
		_temperatures = new int[capacity];
	}
}

class myCode {
	public static void main (String[] args) throws java.lang.Exception
    {
    	TempTracker temp = new TempTracker();
    	temp.insert(32);
    	temp.insert(1);
    	temp.insert(5);
    	temp.insert(32);
    	temp.insert(5);
    	temp.insert(32);
    	temp.insert(1);

    	System.out.println("Max: " + temp.getMax());
    	System.out.println("Min: " + temp.getMin());
    	System.out.println("Mean: " + temp.getMean());
    	System.out.println("Mode: " + temp.getMode());


    }
}