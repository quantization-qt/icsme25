import java.util.*;
import java.text.SimpleDateFormat;
import java.text.ParseException;

class Problem {
    /**
     * Given a date in the format "MM dd yyyy", return the weekday of the date.
     * 
     * Example:
     * >>> convertDatesToWeekdays("11 15 1997")
     * "November 15, 1997 is a Saturday"
     * >>> convertDatesToWeekdays("01 01 2000")
     * "January 1, 2000 is a Saturday"
     * >>> convertDatesToWeekdays("07 04 1998")
     * "July 4, 1998 is a Saturday"
     */
    public static String convertDatesToWeekdays(String date)  {
        // Write your code here.
        String[] dateParts = date.split(" ");
        String month = dateParts[0];
        int day = Integer.parseInt(dateParts[1]);
        int year = Integer.parseInt(dateParts[2]);
        Calendar calendar = Calendar.getInstance();
        calendar.set(year, (Integer.parseInt(month) - 1), day);
        int dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK);
        String[] weekDays = { "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" };
        String weekDay = weekDays[dayOfWeek - 1];
        return String.format("%s %d, %d is a %s", month, day, year, weekDay);
    }
    public static void main(String[] args) {
        // Test the function with different test cases
        assert convertDatesToWeekdays("02 05 2024").equals("February 5, 2024 is a Monday");
        assert convertDatesToWeekdays("01 12 2023").equals("January 12, 2023 is a Thursday");
        assert convertDatesToWeekdays("09 14 2013").equals("September 14, 2013 is a Saturday");
        System.out.println("All tests passed");
    }
}