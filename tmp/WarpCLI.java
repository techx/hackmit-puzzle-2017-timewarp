package warp;

import java.time.Instant;
import java.time.temporal.ChronoUnit;

public class WarpCLI {
    private static final String ANSWER = "Mar 03 0699 03:45 PM";
    private static final long START_EPOCH = 8041680000L;

    public static void main(String[] args) {
        Instant now = Instant.now();
        Instant start = Instant.ofEpochSecond(START_EPOCH);
        Instant end  = start.plus(1, ChronoUnit.DAYS);
        if(now.isAfter(start) && now.isBefore(end)) System.out.println("You got it! The answer is: " + ANSWER);
        else System.out.println("It's not your time ;)");
    }
}