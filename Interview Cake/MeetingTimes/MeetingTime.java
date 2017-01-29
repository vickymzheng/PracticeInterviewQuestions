import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.ArrayList;
class MeetingTime {
	private int _startTime;
	private int _endTime; 

	public MeetingTime(int startTime, int endTime) {
		_startTime = startTime;
		_endTime = endTime;
	}

	public int getStartTime() {
		return _startTime;
	}

	public int getEndTime() {
		return _endTime; 
	}

	public void setEndTime (int endTime) {
		_endTime = endTime;
	}
	public void setStartTime(int startTime) {
		_startTime = startTime;
	}
}

class MeetingCondenser {
	public MeetingTime[] condenseMeetingTimes(MeetingTime[] meetingTimes) {
		int numTimes = meetingTimes.length; 
		Comparator<MeetingTime> meetingComparator = new MeetingTimeComparator(); 
		PriorityQueue<MeetingTime> timesByStart = new PriorityQueue<MeetingTime>(numTimes, meetingComparator);
		for (int i = 0; i < numTimes; i++) {
			timesByStart.add(meetingTimes[i]);
		}
		MeetingTime[] meetingTimesByStart = new MeetingTime[numTimes];
		for(int i = 0; i < numTimes; i++) {
			meetingTimesByStart[i] = timesByStart.poll();
		}

		ArrayList<MeetingTime> condensedTimes = new ArrayList<MeetingTime>(); 
		
		MeetingTime previousMeeting = meetingTimesByStart[0];
		condensedTimes.add(new MeetingTime(previousMeeting.getStartTime(), previousMeeting.getEndTime()));
		for (int i = 1; i < numTimes; i++) {
			MeetingTime currentMeeting = meetingTimesByStart[i];
			
			if (currentMeeting.getStartTime() <= previousMeeting.getEndTime()) {
				previousMeeting.setEndTime(Math.max(currentMeeting.getEndTime(), previousMeeting.getEndTime()));
			}
			else {
				condensedTimes.add(new MeetingTime(previousMeeting.getStartTime(), previousMeeting.getEndTime()));
				previousMeeting = currentMeeting;
			}

		}
		MeetingTime[] answer = new MeetingTime[condensedTimes.size()];
		return condensedTimes.toArray(answer);
	}
	public MeetingCondenser () {

	}
}

class myCode {
	public static void main (String[] args) throws java.lang.Exception {
		MeetingTime[] test0 = new MeetingTime[3]; 
		MeetingTime schedule0 = new MeetingTime(1, 2);
		MeetingTime schedule1 = new MeetingTime(2, 5); 
		MeetingTime schedule2 = new MeetingTime(3, 4); 
		MeetingCondenser worker = new MeetingCondenser(); 
		test0[0] = schedule0;
		test0[1] = schedule1;
		test0[2] = schedule2; 

		MeetingTime[] condensedTimes = worker.condenseMeetingTimes(test0);
		int numTimes = condensedTimes.length;

		for (int i = 0; i < numTimes; i++) {
			System.out.println("Start Time: " + condensedTimes[i].getStartTime() + " End Time: " + condensedTimes[i].getEndTime());
		}

	}
}

class MeetingTimeComparator implements Comparator<MeetingTime> {
	@Override 
	public int compare(MeetingTime m1, MeetingTime m2) {
		return m1.getStartTime() - m2.getStartTime();
	}
}