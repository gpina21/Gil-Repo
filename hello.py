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

TEAM_FACTS = [
    "49ers: San Francisco has won 5 Super Bowls, in the 1981, 1984, 1988, 1989 and 1994 seasons.",
    "49ers: Joe Montana threw 11 touchdowns and zero interceptions across his four Super Bowls.",
    "49ers: Jerry Rice holds the NFL career records for receptions, receiving yards and receiving touchdowns.",
    "49ers: 'The Catch' was Dwight Clark's grab of a Joe Montana pass to beat Dallas in the January 1982 NFC Championship.",
    "49ers: Steve Young threw 6 touchdown passes in Super Bowl XXIX, a Super Bowl record.",
    "49ers: Their 55-10 win over Denver in Super Bowl XXIV is still the biggest blowout in Super Bowl history.",
    "49ers: The team started in 1946 in the All-America Football Conference and joined the NFL in 1950.",
    "49ers: Head coach Bill Walsh is credited with creating the 'West Coast offense.'",
    "49ers: Levi's Stadium in Santa Clara opened as the team's home in 2014.",
    "Braves: The Braves are the only franchise to win the World Series in three cities: Boston (1914), Milwaukee (1957) and Atlanta (1995, 2021).",
    "Braves: The franchise dates back to 1871, making it the oldest continuously operating team in American pro sports.",
    "Braves: Hank Aaron hit home run No. 715 on April 8, 1974, passing Babe Ruth's career record.",
    "Braves: Atlanta won 14 straight division titles from 1991 to 2005 (not counting the strike-shortened 1994 season).",
    "Braves: In 1991 the Braves went 'worst to first,' from last place in 1990 to the National League pennant.",
    "Braves: Greg Maddux won 4 straight Cy Young Awards from 1992 to 1995, the last three with Atlanta.",
    "Braves: Atlanta beat the Houston Astros in 6 games to win the 2021 World Series.",
    "Braves: Chipper Jones was the No. 1 overall draft pick in 1990 and played his whole 19-season career in Atlanta.",
    "Braves: Truist Park opened as the team's home ballpark in 2017.",
]

name = "Gil"
today = date.today()

# Pick a different fact each day, cycling through the list.
fact = SPORTS_FACTS[today.toordinal() % len(SPORTS_FACTS)]
team_fact = TEAM_FACTS[today.toordinal() % len(TEAM_FACTS)]

print(f"Hello, {name}! Today is {today.strftime('%A, %B %d, %Y')}.")
print(f"Sports fact of the day: {fact}")
print(f"Your teams: {team_fact}")
