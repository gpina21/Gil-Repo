from datetime import date

SPORTS_FACTS = [
    "Wilt Chamberlain scored 100 points in a single NBA game on March 2, 1962.",
    "Cal Ripken Jr. played in 2,632 consecutive MLB games from 1982 to 1998.",
    "The 1972 Miami Dolphins went 17-0 and are still the NFL's only perfect season, Super Bowl included.",
    "Wayne Gretzky has more career NHL assists (1,963) than any other player has total points.",
    "Usain Bolt's 100m world record of 9.58 seconds was set in Berlin in 2009.",
    "The Chicago Cubs won the 2016 World Series, ending a 108-year championship drought.",
    "Michael Phelps won 8 gold medals at the 2008 Beijing Olympics.",
    "Joe DiMaggio got a hit in 56 straight games in 1941, a record that still stands.",
    "The Boston Celtics won 8 NBA titles in a row, from 1959 to 1966.",
    "James Naismith invented basketball in 1891 in Springfield, Massachusetts, using peach baskets.",
    "In the first Super Bowl (January 15, 1967), the Green Bay Packers beat the Kansas City Chiefs 35-10.",
    "Nolan Ryan threw 7 no-hitters, the most in MLB history.",
    "Tom Brady won 7 Super Bowls, more than any single NFL franchise.",
    "Ichiro Suzuki had 262 hits in 2004, the MLB single-season record.",
    "Rickey Henderson stole 1,406 bases in his career, the MLB record by a wide margin.",
    "Jack Nicklaus won 18 major golf championships, the most ever.",
]

name = "Gil"
today = date.today()

# Pick a different fact each day, cycling through the list.
fact = SPORTS_FACTS[today.toordinal() % len(SPORTS_FACTS)]

print(f"Hello, {name}! Today is {today.strftime('%A, %B %d, %Y')}.")
print(f"Sports fact of the day: {fact}")
